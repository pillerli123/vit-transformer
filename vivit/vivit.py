import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
import skvideo.io
import os
import cv2

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

import io
import imageio
import ipywidgets
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras import backend as K




## add surveillance fight dataset from the github



##  load, resize and trim the videos

def fram_crop_center(video,cropf):
    f,_,_,_ =video.shape
    startf=f//2 -cropf//2
    return video[startf:startf+cropf,:,:,:]

fights=[]
nofights=[]

surv_fights=[]
surv_no_fights=[]

video_dims=[]


## fight data

for filename in os.listdir('/kaggle/input/movies-fight-detection-dataset/Peliculas/fights'):
    f = os.path.join('/kaggle/input/movies-fight-detection-dataset/Peliculas/fights', filename)
    # checking if it is a file
    video = skvideo.io.vread(f)
    video_dims.append(video.shape)
    L = []

    # resize video dimensions
    for i in range(video.shape[0]):
        frame = cv2.resize(video[i], (128, 128), interpolation=cv2.INTER_CUBIC)
        L.append(frame)

    video = np.asarray(L)

    # center crop video to have consistent video frame number
    video = frame_crop_center(video, 42)

    fights.append(video)

for filename in os.listdir('/kaggle/working/fight-detection-surv-dataset/fight'):
    f = os.path.join('/kaggle/working/fight-detection-surv-dataset/fight', filename)
    # checking if it is a file
    video = skvideo.io.vread(f)
    video_dims.append(video.shape)

    L = []
    for i in range(video.shape[0]):
        frame = cv2.resize(video[i], (128, 128), interpolation=cv2.INTER_CUBIC)
        L.append(frame)

    video = np.asarray(L)
    video = frame_crop_center(video, 42)

    surv_fights.append(video)

## none fight data

for filename in os.listdir('/kaggle/input/movies-fight-detection-dataset/Peliculas/noFights'):
    f = os.path.join('/kaggle/input/movies-fight-detection-dataset/Peliculas/noFights', filename)
    # checking if it is a file
    video = skvideo.io.vread(f)
    video_dims.append(video.shape)

    L = []
    for i in range(video.shape[0]):
        frame = cv2.resize(video[i], (128, 128), interpolation=cv2.INTER_CUBIC)
        L.append(frame)

    video = np.asarray(L)
    video = frame_crop_center(video, 42)

    nofights.append(video)

for filename in os.listdir('/kaggle/working/fight-detection-surv-dataset/noFight'):
    f = os.path.join('/kaggle/working/fight-detection-surv-dataset/noFight', filename)
    # checking if it is a file
    video = skvideo.io.vread(f)
    video_dims.append(video.shape)

    L = []
    for i in range(video.shape[0]):
        frame = cv2.resize(video[i], (128, 128), interpolation=cv2.INTER_CUBIC)
        L.append(frame)

    video = np.asarray(L)
    video = frame_crop_center(video, 42)

    surv_no_fights.append(video)


## Video duration and dimension analysis

data=pd.DataFrame(video_dims,columns=["fram_length","height","width","channels"])
data.describe()

## aggregate data and create lables

surv_fights=[video for video in surv_fights if video.shape[0]==42]
surv_no_fights=[video for video in surv_no_fights if video.shape[0]==42]

videos=fights+surv_fights+nofights+surv_no_fights
videos=np.asarray(videos)

labels=np.concatenate([np.ones(len(fights)+len(surv_fights)),np.zeros(len(nofights)+len(surv_no_fights))])


del fights
del nofights
del surv_fights
del surv_no_fights



## train , test , val split
X_train, X_test, y_train, y_test = train_test_split(videos, labels, test_size=0.2, random_state=2334)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.1, random_state=124567)


print(X_train.shape)
print(X_val.shape)
print(X_test.shape)

# set vivit model hyperparameters

## set seed for reproducibility
SEED=77
os.environ["TF_CUDNN_DETERMINISTIC"]="1"
tf.random.set_seed(SEED)

# Data
DATASET_NAME="fight/nofights"
BATCH_SIZE=4
AUTO=tf.data.AUTOTUNE
INPUT_SHAPE=(42,128,128,3)
NUM_CLASSES=2

# OPTIMIZER
LEARNING_RATE=1e-4
WEIGHT_DECAY=1e-5

# training
EPOCHS=20

# TUBELET EMBEDDING
PATCH_SIZE=(8,8,8)
NUM_PATCHES=(INPUT_SHAPE[0]//PATCH_SIZE[0])**2

## VIVIT architecture
Layer_norm_eps=1e-6
PROJECTION_DIM=64
NUM_HEAD=2
NUM_LAYERS=2

# preprocess and prepare dataloader

@tf.function
def preprocess(frames: tf.Tensor, label: tf.Tensor):
    """Preprocess the frames tensors and parse the labels"""
    # Preprocess images
    frames = tf.image.convert_image_dtype(
        frames[
            ..., tf.newaxis
        ],  # The new axis is to help for further processing with Conv3D layers
        tf.float32,
    )

    # Parse label
    label = tf.cast(label, tf.float32)
    return frames, label

def prepare_dataloader(
        videos:np.ndarray,
        labels:np.ndarray,
        loader_type:str="train",
        batch_size:int=BATCH_SIZE,

):
    '''Untility funciton to prepare dataloader'''
    dataset=tf.data.Dataset.from_tensor_slices((videos,labels))

    if loader_type=="train":
        dataset=dataset.shuffle(BATCH_SIZE*2)

    dataloader=(
        dataset.map(preprocess,num_parallel_calls=tf.data.AUTOTUNE)
        .batch(batch_size)
        .prefetch(tf.data.AUTOTUNE)


    )
    return dataloader

trainloader=prepare_dataloader(X_train,y_train,"train")
validloader=prepare_dataloader(X_val,y_val,"valid")
testloader=prepare_dataloader(X_test,y_test,"test")


# define some models classes
class TubeletEmbedding(layers.layer):
    def __init__(self,embed_dim,patch_size,**kwargs):
        super().__init__(**kwargs)
        self.projection=layers.Conv3D(
            filters=embed_dim,
            kernel_size=patch_size,
            strides=patch_size,
            padding="VALID",

        )
        self.flatten=layers.Reshape(target_shape=(-1,embed_dim))

    def call(self,videos):
        projected_pathes=self.projection(videos)
        flattened_pathes=self.flatten(projected_pathes)
        return flattened_pathes

class PositionalEncoder(layers.Layer):
    def __init__(self,embed_dim,**kwargs):
        super().__init__(**kwargs)
        self.embed_dim=embed_dim

    def build(self, input_shape):
        _, num_tokens, _ = input_shape
        self.position_embedding = layers.Embedding(
            input_dim=num_tokens, output_dim=self.embed_dim
        )
        self.positions = tf.range(start=0, limit=num_tokens, delta=1)





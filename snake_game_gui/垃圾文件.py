
def method1():
    video_writer = cv2.VideoWriter('gameplay.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, (1920, 1080))

    # Create threads to run GUI game and capture screen
    game_thread = threading.Thread(target=start_game)
    capture_thread = threading.Thread(target=capture_screen)

    # Start threads
    game_thread.start()
    capture_thread.start()

    # Wait for threads to finish
    game_thread.join()
    capture_thread.join()

    # Release video writer object
    video_writer.release()
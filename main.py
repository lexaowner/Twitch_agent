import sys
import av
from streamlink import Streamlink
import cv2

def play_stream(url):
    # Create a Streamlink session
    session = Streamlink()

    # Get available streams for the specified URL
    streams = session.streams(url)

    if not streams:
        print("Стрим не найден по URL.")
        return

    # Choose the stream with the best quality
    stream = streams["best"]

    # Get the URL for streaming the video
    stream_url = stream.url

    print(f"Открытие стрима: {stream_url}")
    print(f"Для остановки нажмите CTRL+C")

    # Open the stream using pyAV
    container = av.open(stream_url)

    # Find the video stream
    video_stream = next(s for s in container.streams if s.type == 'video')

    # Create a window for playback using OpenCV
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)

    # Read and display frames in real-time
    for frame in container.decode(video_stream):
        # Convert frame to numpy array
        img = frame.to_ndarray(format='rgb32')

        # Display the frame
        cv2.imshow('Video', img)

        # Press 'q' to exit the player
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close the window and release resources
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # if len(sys.argv) != 2:
    #     print("Использование: python play_stream.py <ссылка_на_стрим>")
    #     sys.exit(1)
    #
    # stream_url = sys.argv[1]
    stream_url = input('Вставьте ссылку на стрим например (https://www.twitch.tv/stream): ')
    play_stream(stream_url)
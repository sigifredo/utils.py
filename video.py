import cv2
import os


def extract_frames(video_path, output_folder, video_width=None, video_height=None):
    cap = cv2.VideoCapture(video_path)

    frame_count = 0
    success = True

    while success:
        success, frame = cap.read()

        if success:
            frame_path = os.path.join(output_folder, f'frame_{frame_count:05d}.png')

            if not os.path.exists(frame_path):
                if not video_width is None and not video_height is None:
                    frame = cv2.resize(frame, (video_width, video_height))

                cv2.imwrite(frame_path, frame)
                frame_count += 1

    cap.release()
    print(f'✅ {frame_count} frames extraídos a la carpeta: "{output_folder}"')

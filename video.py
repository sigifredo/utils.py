import cv2
import numpy as np
import os
import PIL.Image


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


def save_video(video_path: str, frames: list[PIL.Image.Image], frame_rate: int = 15) -> None:
    height = frames[0].height
    width = frames[0].width

    fourcc = cv2.VideoWriter_fourcc(*'X264')
    video_writer = cv2.VideoWriter(video_path, fourcc, frame_rate, (width, height))

    for frame in frames:
        np_frame = np.array(frame)
        cv2_frame = cv2.cvtColor(np_frame, cv2.COLOR_RGB2BGR)
        video_writer.write(cv2_frame)

    video_writer.release()

    print(f'✅ Video guardado en: {video_path}')

from moviepy.editor import VideoFileClip
import os


def convert_mp4_to_mp3(input_file_path, output_directory):
    try:

        video_clip = VideoFileClip(input_file_path)

        base_name = os.path.splitext(os.path.basename(input_file_path))[0]

        output_file_path = os.path.join(output_directory, f"{base_name}.mp3")

        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file_path)

        audio_clip.close()
        video_clip.close()

        print(f"Pomyślnie skonwertowano {input_file_path} na {output_file_path}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    input_file_path = "C:\\scierzka\\do\\twójplik.mp4"
    output_directory = "C:\\twoja\\ścieżka\\docelowa"

    convert_mp4_to_mp3(input_file_path, output_directory)

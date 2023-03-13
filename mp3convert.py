import os
import pytube
import subprocess

def download_youtube_video(link, output_path=None):
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    default_output_path = os.getcwd() # set default output path to current working directory
    if output_path:
        output_path = os.path.expanduser(output_path)
    else:
        output_path = default_output_path
    stream.download(output_path=output_path, filename= audio + exto)
    input_file_path = os.path.join(output_path, audio + exti)
    output_file_path = os.path.join(output_path, audio + exto)
    subprocess.call(['ffmpeg', '-i', input_file_path, '-vn', '-acodec', 'libmp3lame', '-y', output_file_path])
    os.remove(input_file_path)

link = input("Enter the YouTube video link: ")
output_path = input("Enter the output directory path (default is current working directory): ")
audio = input("Enter name for the audio, without extension: ")
exti = ".mp4"
exto = ".mp3"
download_youtube_video(link, output_path)
import os
import pytube
import subprocess
import tkinter as tk
from tkinter import filedialog

def download_youtube_video(link, output_path=None, audio="", exti=".mp4", exto=".mp3"):
    yt = pytube.YouTube(link)
    stream = yt.streams.filter(only_audio=True).first()
    default_output_path = os.getcwd() # set default output path to current working directory
    if output_path:
        output_path = os.path.expanduser(output_path)
    else:
        output_path = default_output_path
    stream.download(output_path=output_path, filename=audio + exto)
    input_file_path = os.path.join(output_path, audio + exti)
    output_file_path = os.path.join(output_path, audio + exto)
    subprocess.call(['ffmpeg', '-i', input_file_path, '-vn', '-acodec', 'libmp3lame', '-y', output_file_path])
    os.remove(input_file_path)

def browse_output_path():
    output_path = filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_path)

def download_video():
    link = link_entry.get()
    output_path = output_path_entry.get()
    audio = audio_entry.get()
    exti = ".mp4"
    exto = ".mp3"
    download_youtube_video(link, output_path, audio, exti, exto)
    status_label.config(text="Download complete!")

# create the main window
root = tk.Tk()
root.title("YouTube Video Downloader")

# create the input fields
link_label = tk.Label(root, text="YouTube Video Link:")
link_label.grid(row=0, column=0, padx=5, pady=5)
link_entry = tk.Entry(root, width=50)
link_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

output_path_label = tk.Label(root, text="Output Directory:")
output_path_label.grid(row=1, column=0, padx=5, pady=5)
output_path_entry = tk.Entry(root, width=50)
output_path_entry.grid(row=1, column=1, padx=5, pady=5)
browse_button = tk.Button(root, text="Browse...", command=browse_output_path)
browse_button.grid(row=1, column=2, padx=5, pady=5)

audio_label = tk.Label(root, text="Audio Name:")
audio_label.grid(row=2, column=0, padx=5, pady=5)
audio_entry = tk.Entry(root, width=50)
audio_entry.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# create the download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.grid(row=3, column=1, padx=5, pady=5)

# create the status label
status_label = tk.Label(root, text="")
status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# start the GUI
root.mainloop()

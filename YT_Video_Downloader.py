from tkinter import *
from tkinter import filedialog
import subprocess
import os
import shutil

def check_ffmpeg():
    if shutil.which("ffmpeg") is None:
        print("WARNING: ffmpeg not found. The downloaded format may not be the best available.")
        print("Install ffmpeg for better video/audio processing: https://github.com/yt-dlp/yt-dlp#dependencies")
    else:
        print("ffmpeg is installed and ready to use.")

check_ffmpeg()


root = Tk()
root.geometry('800x400')  
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text='Copy the link of the video you want to download from YouTube',
      font='arial 17 bold', bg='lightblue', fg='darkblue').pack(fill='x', pady=10)

link = StringVar()

Label(root, text='Paste Link Below & Hit Download Button:', font='arial 15 bold').pack(pady=20)
Entry(root, width=50, textvariable=link).pack(pady=10)

def Downloader():
    try:
        video_url = str(link.get())  
        if not video_url.strip():
            Label(root, text='ERROR: Please enter a valid URL', font='arial 15', fg='red').pack(pady=10)
            return
        
        download_path = filedialog.askdirectory()  
        if not download_path:
            Label(root, text='Download Cancelled', font='arial 15', fg='orange').pack(pady=10)
            return

        subprocess.run([
            'yt-dlp',
            '-o', f'{download_path}/%(title)s.%(ext)s',  
            video_url
        ], check=True)

        Label(root, text='DOWNLOADED', font='arial 15 bold', bg='lightgreen', fg='darkgreen').pack(pady=10)

    except subprocess.CalledProcessError as e:
        Label(root, text=f'ERROR: Download failed ({e})', font='arial 15', fg='red').pack(pady=10)
    except Exception as e:
        Label(root, text=f'ERROR: {e}', font='arial 15', fg='red').pack(pady=10)


Button(root, text='DOWNLOAD', font='arial 15 bold', bg='orange', fg='white',
       padx=20, pady=5, command=Downloader).pack(pady=20)

root.mainloop()

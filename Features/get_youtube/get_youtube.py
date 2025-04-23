# stopped working as of 21.04.2025
from pytube import YouTube
import os

url_youtube = 'https://www.youtube.com/watch?v=X8z54kWKowg'

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)
    
if __name__ == "__main__":
    downloadYouTube(url_youtube, './videos/Downloaded')
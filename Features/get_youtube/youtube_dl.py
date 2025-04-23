import yt_dlp

url = 'https://www.youtube.com/watch?v=88vJbxrxYfM&t'  # your video URL

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # prefer best video and audio separately, fallback to best
    'merge_output_format': 'mp4',          # final output container
    'outtmpl': './videos/Downloaded/%(title)s.%(ext)s',  # output filename template
    'noplaylist': True                     # download only the single video, no playlist
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

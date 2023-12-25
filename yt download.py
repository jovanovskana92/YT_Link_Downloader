from pytube import YouTube

url = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"

yt = YouTube(url)

yt.streams.get_highest_resolution().download()
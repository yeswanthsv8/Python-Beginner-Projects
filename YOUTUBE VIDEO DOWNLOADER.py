"""
Modules:
pytube
YouTube

Functions:
title
thumbnail_url
my_video.streams.get_highest_resolution()
download()
"""

from pytube import YouTube
url='https://www.youtube.com/watch?v=q8JtWDTdKuE'
my_video=YouTube(url)

print(my_video.title)
print(my_video.thumbnail_url)

my_video=my_video.streams.get_highest_resolution()
print(my_video.download())

from pytube import Playlist

plyList = ("Enter the link of playlist you want to download!")

print(f'Downloading : {plyList.title}')

for video in plyList.videos:
    video.streams.first().download()
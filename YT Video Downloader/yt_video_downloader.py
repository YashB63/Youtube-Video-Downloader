from pytube import YouTube

link = "Enter the Link of the video you want to download"

youtube_one = YouTube(link)

#print(youtube_one.title)
#print(youtube_one.thumbnail_url)

videos = youtube_one.streams.all() #All format Download

#videos = youtube_one.streams.filter(only_audio=True) #Only Audio Download

vids = list(enumerate(videos))

for i in vids:
    print(i)

strm = int(input("enter: "))
videos[strm].download()
print('Successfully')
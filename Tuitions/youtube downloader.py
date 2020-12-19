import pytube
url='https://www.youtube.com/watch?v=ZtsX7kJ7zss&list=WL&index=1'

youtube = pytube.YouTube(url)
streams = youtube.streams.all()
for i in streams:
    print(i)
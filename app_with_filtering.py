from pytubefix import YouTube
from pytubefix.cli import on_progress

link = input("Entrez le lien de la vidéo Youtube: ") 
print(link)
video = YouTube(link, on_progress_callback=on_progress)
print(video)
print(f"Téléchargement de : {video.title}")
stream = video.streams.filter(res='1080p')
audio = video.streams.filter(only_audio=True)
print(audio)
print(stream)
hdstream = video.streams.get_by_itag(299)
hdaudio = video.streams.get_by_itag(251)
print(hdstream)
print(hdaudio)
hdstream.download()
hdaudio.download()
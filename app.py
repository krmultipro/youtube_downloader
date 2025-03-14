from pytubefix import YouTube
from pytubefix.cli import on_progress

link = input("Entrez le lien de la vidéo Youtube: ") 
print(link)

video = YouTube(link, on_progress_callback=on_progress)
print(video)

print(f"Téléchargement de : {video.title}")

stream = video.streams.get_highest_resolution()
print(stream)

stream.download()
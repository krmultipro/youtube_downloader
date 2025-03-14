import streamlit as st
from pytubefix import YouTube
import os

st.set_page_config(page_title="YouTube Downloader", page_icon="📹")

st.title("📥 Téléchargeur YouTube")
st.write("Entrez un lien YouTube pour télécharger la vidéo.")

# Champ pour entrer le lien
link = st.text_input("🔗 Lien YouTube", placeholder="Collez le lien ici...")

if st.button("Télécharger"):
    if link:
        try:
            st.info("Analyse du lien...")
            video = YouTube(link)
            stream = video.streams.get_highest_resolution()

            st.success(f"✅ Vidéo trouvée : {video.title}")

            # Intégration correcte de la vidéo YouTube
            video_id = link.split("v=")[-1]  # Extraire l'ID de la vidéo YouTube
            embed_url = f"https://www.youtube.com/embed/{video_id}"

            st.components.v1.html(f"""
                <iframe width="700" height="400" src="{embed_url}" frameborder="0" allowfullscreen></iframe>
            """, height=450)

            st.write(f"📏 Résolution : {stream.resolution}")
            st.write(f"🎶 Audio : {stream.audio_codec}")

            # Téléchargement avec dossier spécifique
            download_folder = "downloads"
            os.makedirs(download_folder, exist_ok=True)  # Crée le dossier si inexistant
            filepath = stream.download(output_path=download_folder)

            st.balloons()
            st.success("Téléchargement terminé ! 🎉")

            # Ajout d'un lien pour télécharger la vidéo depuis Streamlit
            with open(filepath, "rb") as f:
                st.download_button(label="📥 Télécharger la vidéo", data=f, file_name=os.path.basename(filepath))

        except Exception as e:
            st.error(f"Erreur : {e}")
    else:
        st.warning("Veuillez entrer un lien YouTube valide.")

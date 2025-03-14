from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress

class YouTubeDownloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Téléchargeur YouTube")
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Entrez le lien YouTube :")
        layout.addWidget(self.label)
        
        self.entry = QLineEdit()
        layout.addWidget(self.entry)
        
        self.button = QPushButton("Télécharger")
        self.button.clicked.connect(self.telecharger_video)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def telecharger_video(self):
        lien = self.entry.text()
        if not lien:
            QMessageBox.warning(self, "Erreur", "Veuillez entrer un lien YouTube valide.")
            return
        
        try:
            video = YouTube(lien, on_progress_callback=on_progress)
            stream = video.streams.get_highest_resolution()
            stream.download()
            QMessageBox.information(self, "Succès", f"Téléchargement terminé : {video.title}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Une erreur est survenue : {str(e)}")

app = QApplication(sys.argv)
window = YouTubeDownloader()
window.show()
sys.exit(app.exec())

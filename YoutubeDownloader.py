from pytube import YouTube, Playlist
import os

def descargaList():
    
        # URL de la lista de reproducción de YouTube que deseas descargar
        playlist_url = "https://www.youtube.com/watch?v=d0ipbK7btxI&list=PLSlpnbEqrjc8y2SgM0U7oT45ldHr6BFTq"

        # Crear un objeto Playlist
        playlist = Playlist(playlist_url)

        # Carpeta donde se guardarán los archivos MP3 descargados
        output_folder = "mp3_downloads"

        # Asegúrate de que la carpeta de salida exista o créala si no existe
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Iterar a través de los videos de la lista de reproducción
        for video_url in playlist.video_urls:
            try: 
                yt = YouTube(video_url)
                
                # Filtrar las streams disponibles para obtener solo el audio en formato MP4
                audio_stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
                
                # Descargar el audio en formato MP4
                audio_stream.download(output_path=output_folder)
                
                # Cambiar la extensión del archivo descargado a .mp3
                base_filename, _ = os.path.splitext(audio_stream.default_filename)
                os.rename(
                    os.path.join(output_folder, audio_stream.default_filename),
                    os.path.join(output_folder, base_filename + '.mp3')
                )
                
                print(f"Se ha descargado el audio de '{yt.title}' como {base_filename}.mp3")
            except Exception as e:
                print(f"Se produjo un error al descargar {video_url}: {e}")

descargaList()

import sys
import subprocess
from pathlib import Path
import shutil


def instalar_pacote(pacote):
    """Instala um pacote via pip."""
    print(f"Instalando '{pacote}'...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade", pacote]
    )


# ==========================
# Garante que yt-dlp exista
# ==========================
try:
    import yt_dlp
except ImportError:
    instalar_pacote("yt-dlp")
    import yt_dlp


# ==========================
# Garante que FFmpeg exista
# ==========================
def garantir_ffmpeg():
    if shutil.which("ffmpeg") is not None:
        return

    print("\nFFmpeg não encontrado.")
    print("Tentando instalar automaticamente...\n")

    try:
        instalar_pacote("imageio-ffmpeg")
        import imageio_ffmpeg

        ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

        # Faz o yt-dlp usar esse executável
        return ffmpeg

    except Exception as e:
        print("Não foi possível instalar o FFmpeg automaticamente.")
        print(e)
        sys.exit(1)


FFMPEG_LOCATION = garantir_ffmpeg()


def coletar_links():
    print("Cole os links do Google Drive.")
    print("Pressione ENTER em branco para iniciar o download.\n")

    links = []

    while True:
        link = input("> ").strip()

        if not link:
            break

        links.append(link)

    return links


def baixar_mp3(link):
    pasta = Path.cwd()

    opcoes = {
        "format": "bestaudio/best",
        "outtmpl": str(pasta / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }

    if FFMPEG_LOCATION:
        opcoes["ffmpeg_location"] = FFMPEG_LOCATION

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([link])

        print("✓ Concluído\n")

    except Exception as e:
        print("✗ Erro:")
        print(e)
        print()


def main():
    links = coletar_links()

    if not links:
        print("Nenhum link informado.")
        return

    print(f"\nBaixando {len(links)} arquivo(s)...\n")

    for i, link in enumerate(links, 1):
        print(f"[{i}/{len(links)}]")
        baixar_mp3(link)

    print("Todos os downloads finalizaram.")


if __name__ == "__main__":
    main()
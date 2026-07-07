# Google Drive Audio Downloader

Script em Python para baixar automaticamente o áudio de arquivos compartilhados no Google Drive e convertê-los para MP3.

## Funcionalidades

- Recebe múltiplos links do Google Drive via terminal.
- Finaliza a entrada quando uma linha vazia é enviada.
- Baixa apenas o áudio de cada arquivo.
- Converte automaticamente para MP3.
- Salva os arquivos na mesma pasta onde o script é executado.
- Instala automaticamente as dependências necessárias (`yt-dlp` e `imageio-ffmpeg`) caso não estejam disponíveis.

## Requisitos

- Python 3.9 ou superior.
- Conexão com a internet.

Nenhuma instalação manual de bibliotecas é necessária.

## Como usar

Execute o script:

```bash
python baixar_drive_mp3.py
```

Cole um link por linha:

```text
https://drive.google.com/file/d/XXXXXXXX/view
https://drive.google.com/file/d/YYYYYYYY/view
```

Quando terminar, pressione **Enter** em uma linha vazia para iniciar os downloads.

## Saída

Os arquivos MP3 serão salvos na mesma pasta do script.

## Observações

- Os arquivos do Google Drive precisam estar compartilhados com permissão de acesso.
- O nome do MP3 será baseado no nome original do arquivo.
- O download é realizado utilizando `yt-dlp` e a conversão para MP3 através do FFmpeg.
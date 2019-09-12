from __future__ import unicode_literals
import youtube_dl
import os

def adapt():
    for i in os.listdir():
        if len(i.split()) >= 2:
            complete_name_list = i.split()
            complete_name_list[-1] = ".mp3"
            complete_name = complete_name_list[1] + complete_name_list[-1]
            os.rename(i, complete_name)
        else:
            print("No names to change")


def download(url):
    song_folder = "C:\\Users\\Usuario\\Desktop\\Music"

    download_options = {
    "format" : "bestaudio/best",
    "outtmpl" : "%(title)s.%(ext)s",
    "nocheckercertificate" : True,
    "postprocessors" : [{
        "key" : "FFmpegExtractAudio",
        "preferredcodec" : "mp3",
        "preferredquality" : "192"
    }],
}

    if not os.path.exists(song_folder):
        os.mkdir(song_folder)
        os.chdir(song_folder)
    else:
        os.chdir(song_folder)
    with youtube_dl.YoutubeDL(download_options) as dl:
        dl.download([url])

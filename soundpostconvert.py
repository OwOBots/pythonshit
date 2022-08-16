# vars
from curses import endwin
from tkinter import E
import subprocess
import requests
from urllib.parse import unquote
from os.path import splitext
from urllib.parse import urlparse
video = input("the name of the webm= ")
audio = input("audio url= ")
audiodecoded = unquote(audio)
videogif = video
codec = "libvpx-vp9"
outputfile = input("what name do you want= ")


def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'


ifaudionotogg = get_ext(audiodecoded)

if ifaudionotogg.endswith('.mp3'):
    subprocess.run(
        f"ffmpeg -i {video} -i {audiodecoded} -c:v {codec} {outputfile}")
elif ifaudionotogg.endswith('.ogg'):
    subprocess.run(
        f"ffmpeg -i {video} -i {audiodecoded} -c {codec} {outputfile}")
elif ifaudionotogg.endswith('.wav'):
    subprocess.run(
        f"ffmpeg -i {video} -i {audiodecoded} -c:v {codec} {outputfile}")
else:
    print('somethings wrong')
# vars
from curses import endwin
import os
import sys
from tkinter import E, Scale
import subprocess
import requests
from urllib.parse import unquote
from os.path import splitext
from urllib.parse import urlparse
video = input("the name of the webm= ")
audio = input("audio url= ")
audiodecoded = unquote(audio)
codec = "copy"
codemp3 = "libvpx-vp9"
outputfile = input("what name do you want= ")
#this is just used in the png checker
#outputpng = input("what ext do you want= ")



def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'




        

ifaudionotogg = get_ext(audiodecoded)
ifvideogif = video
def audiostuff():
    if ifaudionotogg.endswith('.mp3'):
        subprocess.run(
        f"ffmpeg -i {video} -i {audiodecoded} -c:v {codemp3} {outputfile}")
    elif ifaudionotogg.endswith('.ogg'):
        subprocess.run(
        f"ffmpeg  -i {video} -i {audiodecoded} -c {codec} {outputfile}")
    elif ifaudionotogg.endswith('.wav'):
        subprocess.run(
        f"ffmpeg -i {video} -i {audiodecoded} -c:v {codec} {outputfile}")
    else:
        print('somethings wrong')
def videochecker():
    if ifvideogif.endswith('.png'):
        scale = input("format is x:x= ")
        subprocess.run(
        f"ffmpeg  -loop 1 -r 1 -i {video} -i {audiodecoded} -c:v {codemp3} -t 00:06:04 -pix_fmt yuv420p -vf scale={scale} {outputfile}")    
    else:
        audiostuff()

videochecker()

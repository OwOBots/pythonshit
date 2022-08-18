# vars
import subprocess
from urllib.parse import unquote
import wget
from os.path import splitext
from urllib.parse import urlparse
import os
video = input("the name of the webm= ")
audio = input("audio url= ")
audiodecoded = unquote(audio)
codec = "copy"
codemp3 = "libvpx-vp9"
outputfile = input("what name do you want= ")
# this is just used in the png checker
#outputpng = input("what ext do you want= ")


def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'


ifaudionotogg = get_ext(audiodecoded)
ifaudiolocal = get_ext(audio)
ifvideogif = video

# this dont work
def convertifnotsupported():
    if audiodecoded.startswith('https://'):
        filename = wget.download(audiodecoded)
        subprocess.run(
            f"ffmpeg -i {filename} -c:a libvorbis out.ogg")
    elif not audiodecoded.startswith('https://'):
        subprocess.run(
            f"ffmpeg -i {audio} -c:a libvorbis out.ogg")
    else:
        audiostuff()


def audiostuff():
    if audiodecoded.startswith('https://'):
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
    else:
        localfile()


def videochecker():
    if ifvideogif.endswith('.png'):
        scale = input("format is x:x= ")
        time = input("how long is your audio")
        subprocess.run(
            f"ffmpeg  -loop 1 -r 1 -i {video} -i {audiodecoded} -c:v {codemp3} -t {time} -pix_fmt yuv420p -vf scale={scale} {outputfile}")
    elif ifvideogif.endswith('.gif'):
        scale = input("format is x:x= ")
        time = input("how long is your audio= ")
        subprocess.run(
            f"ffmpeg -ignore_loop 0 -i {video} -i {audiodecoded} -c:v libvpx -crf 12 -b:v 500K -auto-alt-ref 0 {outputfile}")
    else:
        audiostuff()


def localfile():
    if ifaudiolocal.endswith('.mp3'):
        subprocess.run(
            f"ffmpeg -i {video} -i {audio} -c:v {codemp3} {outputfile}")
    elif ifaudiolocal.endswith('.ogg'):
        subprocess.run(
            f"ffmpeg -i {video} -i {audio} -c:v {codec} {outputfile}")
    elif ifaudiolocal.endswith('.flac'):
        convertifnotsupported()
        subprocess.run(
            f"ffmpeg -i {video} -i out.ogg -c:v {codec} {outputfile}")
    else:
        print('uh oh someone did a fucky wucky')


videochecker()

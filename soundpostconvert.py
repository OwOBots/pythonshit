import glob
import subprocess
from urllib.parse import urlparse
from urllib.parse import unquote
from os.path import splitext
import os
import pathlib
import fileformats

video = input('Wheres your webm?= ')
audio = input('Wheres your audio?= ')
output = input('Name pls= ')
codemp3 = "libvpx-vp9"
codec = "copy"
audiodecoded = unquote(audio)

def suffix():
    project_files = glob.glob('*.webm') + glob.glob('*.png') + glob.glob('*.gif')
    file_path = video
    extension = pathlib.Path(file_path).suffix
def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'
extra = get_ext(video)




audioinput = get_ext(audiodecoded)
localaudioinput = get_ext(audio)
def png():
    if video.endswith('.png'):
        print('egg')
        fileformats.merge_audio_and_png(video,audiodecoded,output)
        quit()
    else:
            pass
        

def realvideos():
    if video.endswith('.webm'):
            time = input("the format for time is XX:XX:XX= ")
            subprocess.run(
            f'ffmpeg -v quiet -hide_banner -stats -t {time} -i "{video}"  -i {audiodecoded} -c:v {codemp3} -movflags fast  -y {output}')
            quit()
    else:
        pass

def videoshit(): 
    if video.endswith('.gif'):
        fileformats.merge_audio_and_gif(video,audiodecoded,output)
        quit()
    else:
        pass
png()
videoshit()
realvideos()
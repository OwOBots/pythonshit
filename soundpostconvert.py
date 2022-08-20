import glob
import subprocess
from urllib.parse import urlparse
from urllib.parse import unquote
from os.path import splitext
import os
import pathlib
import gif

video = input('Wheres your webm?= ')
audio = input('Wheres your audio?= ')
output = input('Name pls= ')
codemp3 = "libvpx"
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
def videotest():
    if video.endswith('.png'):
                time = input("the format for time is XX:XX:XX= ")
                subprocess.run(
                f'ffmpeg -framerate 30 -i "{video}" -i {audiodecoded} -t {time} -c:v {codemp3} -pix_fmt yuv420p  -movflags fast -y {output}')
                quit()
    else:
            pass
        

def realvideos():
    if video.endswith('.webm'):
            time = input("the format for time is XX:XX:XX= ")
            subprocess.run(
            f"ffmpeg -t {time} -i {video}  -i {audiodecoded} -c:v {codemp3} -movflags fast  -y {output}")
            quit()
    else:
        pass

def videoshit():
    video 
    if video.endswith('.gif'):
        gif.merge_audio_and_gif(video,audiodecoded,output)
        quit()
    else:
        pass
videotest()
videoshit()
realvideos()

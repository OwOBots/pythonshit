import glob
import subprocess
from urllib.parse import urlparse
from urllib.parse import unquote
from os.path import splitext
import pathlib
video = input('Wheres your webm?= ')
audio = input('Wheres your audio?= ')
codemp3 = "libvpx"
codec = "copy"
audiodecoded = unquote(audio)
output = input('Name pls= ')
project_files = glob.glob('*.webm') + glob.glob('*.png') + glob.glob('*.gif')
file_path = video
extension = pathlib.Path(file_path).suffix
def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext  # or ext[1:] if you don't want the leading '.'


audioinput = get_ext(audiodecoded)
localaudioinput = get_ext(audio)
def videotest():
    print('png')
    for ext in project_files:
        if ext.endswith('.png'):
                time = input("the format for time is XX:XX:XX= ")
                subprocess.run(
                f"ffmpeg -framerate 30 -i {video} -i {audiodecoded} -t {time} -c:v {codemp3} -pix_fmt yuv420p  -movflags fast -y {output}")
        break
       
def realvideos():
    print('webm')
    for ext in project_files:
        if ext.endswith('.webm'):
            time = input("the format for time is XX:XX:XX= ")
            subprocess.run(
            f"ffmpeg -t {time} -i {video}  -i {audiodecoded} -c:v {codemp3} -movflags fast  -y {output}")
        break


videotest()
realvideos()

from asyncio.log import logger
import subprocess

def merge_audio_and_gif(video_path: str, audio_path: str, outputfile: str) -> None:
    """ Combines audio and gifs into a single file
        
    """
    time = input("hows longs the audio?= ")
    
    video = video_path
    audio = audio_path
    output = outputfile
    try:
       subprocess.run(
            #todo: fix transparency 
            f"ffmpeg -ignore_loop 0 -t {time} -i {video}  -i {audio}  -c:v libvpx  -auto-alt-ref 0 -pix_fmt yuva420p -crf 12 -b:v 500K  {outputfile}")
    except FileNotFoundError:
        logger.error('FileNotFound, ensure ffmpeg is installed.')
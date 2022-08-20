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
            f"ffmpeg  -v warning -stats  -hide_banner -ignore_loop 0 -t {time} -i {video}  -i {audio}  -c:v libvpx  -auto-alt-ref 0 -pix_fmt yuva420p -crf 12 -b:v 500K -y {outputfile}")
    except FileNotFoundError:
        logger.error('FileNotFound, ensure ffmpeg is installed.')
def merge_audio_and_png(video_path: str, audio_path: str, outputfile: str) -> None:
    """ Combines audio and gifs into a single file
        
    """
    time = input("hows longs the audio?= ")
    
    video = video_path
    audio = audio_path
    output = outputfile
    try:
       subprocess.run(
                f'ffmpeg -v warning -hide_banner -stats -framerate 30 -i "{video}" -i {audio} -t {time} -c:v libvpx -pix_fmt yuv420p  -movflags fast -y {output}')
    except FileNotFoundError:
        logger.error('FileNotFound, ensure ffmpeg is installed.')
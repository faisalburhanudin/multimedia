import subprocess

from celery import shared_task


@shared_task
def resize_video_360p(fp, fp_output):
    subprocess.call([
        "ffmpeg",

        # input file
        "-i",  fp,

        # using x264 codex
        "-codec:v", "libx264",

        # high profile
        "-profile:v", "high",

        # slow for better compression
        "-preset", "slow",

        # 500k video bitrate
        "-b:v", "500k",

        # Very useful for web - setting this to bitrate and 2x bitrate gives good results.
        "-maxrate", "500k",
        "-bufsize", "1000k",

        # scale video to 360
        "-vf", "scale=-1:360",

        # using all cpu
        "-threads", "0",

        # encode audio using libfdk_aac
        "-codec:a", "libfdk_aac",

        # audio bitrate
        "-b:a", "128k",

        # file path output file
        fp_output
    ])

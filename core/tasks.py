import os
import tempfile
import subprocess

from django.core.files import File
from celery import shared_task

from core.models import Content


@shared_task
def resize(content_id, file_path):
    fp_output = os.path.join(tempfile.gettempdir(), ".".join(os.path.basename(file_path).split(".")[:-1]) + ".mp4")
    resize_video_360p(file_path, fp_output)

    filename = os.path.basename(fp_output)

    content = Content.objects.get(id=content_id)
    with open(fp_output, "rb") as out:
        content.content_type = "video/mp4"
        content.attachment.save(filename, File(out))


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

        # audio bitrate
        "-b:a", "128k",

        "-strict", "-2",

        # file path output file
        fp_output
    ])

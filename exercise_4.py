
from asyncio import subprocess


def resize(image, output_dir, ratio):

  subprocess.run(["ffmpeg", "-i", image, "-vf", f"scale=iw*{ratio}:ih*{ratio}", str(output_dir / f"resized_{ratio}.jpeg")])


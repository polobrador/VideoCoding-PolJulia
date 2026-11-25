
import subprocess
from pathlib import Path



def resize(image, output_dir, ratio):

  subprocess.run(["ffmpeg", "-i", image, "-vf", f"scale=iw*{ratio}:ih*{ratio}", str(output_dir / f"resized_{ratio}.jpeg")])

resize("images/input.jpeg", Path("images"), 0.5)
resize("images/input.jpeg", Path("images"), 0.25)
resize("images/input.jpeg", Path("images"), 0.125)

def resize_sws(image, output_dir, ratio):

  subprocess.run(["ffmpeg", "-i", image, "-vf", f"scale=iw*{ratio}:ih*{ratio}", "-sws_flags", "lanczos", str(output_dir / f"resized_{ratio}_sws.jpeg")])

resize_sws("images/input.jpeg", Path("images"), 0.5)
resize_sws("images/input.jpeg", Path("images"), 0.25)
resize_sws("images/input.jpeg", Path("images"), 0.125)

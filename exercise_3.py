
import cv2
import numpy as np
import subprocess
import shutil
from pathlib import Path

INPUT_IMAGE = "images/input.jpeg"
OUTPUT_DIR = Path("images")

OUTPUT_DIR.mkdir(exist_ok=True)

image = cv2.imread(INPUT_IMAGE)

img_yuv = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(img_yuv) 
U_blur = cv2.GaussianBlur(u, (0, 0), sigmaX=15)
V_blur = cv2.GaussianBlur(v, (0, 0), sigmaX=15)
Y_blur = cv2.GaussianBlur(y, (0, 0), sigmaX=15)

chroma_blurred = cv2.merge([y, U_blur, V_blur])
luma_blurred = cv2.merge([Y_blur, u, v])

chroma_result = cv2.cvtColor(chroma_blurred, cv2.COLOR_YUV2BGR)
luma_result = cv2.cvtColor(luma_blurred, cv2.COLOR_YUV2BGR)


cv2.imwrite(str(OUTPUT_DIR / "chroma_blurred.jpeg"), chroma_result)
cv2.imwrite(str(OUTPUT_DIR / "luma_blurred.jpeg"), luma_result)
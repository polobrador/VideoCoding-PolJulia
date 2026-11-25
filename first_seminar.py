import cv2
import numpy as np
import subprocess
import shutil
from pathlib import Path
import scipy



#EXERCISE 2:
class ColorTranslator:
    @staticmethod
    def rgb_to_yuv(rgb_color):
        r = rgb_color[0]
        g = rgb_color[1]
        b = rgb_color[2]

        Y = 0.257*r + 0.504*g + 0.098*b + 16
        Cb = -0.148 * r - 0.291 * g + 0.439 * b + 128
        Cr = 0.439 * r - 0.368 * g - 0.071 * b + 128

        return (Y, Cb, Cr)

    @staticmethod
    def yuv_to_rgb(yuv_color):
        y = yuv_color[0]
        u = yuv_color[1]
        v = yuv_color[2]

        b = 1.164 * (y - 16) + 2.018 * (u - 128)
        g = 1.164 * (y - 16) - 0.813 * (v - 128) - 0.391 * (u - 128)
        r = 1.164 * (y - 16) + 1.596 * (v - 128)
        return (r,g,b)


ct = ColorTranslator
rgb = (222, 100, 32)
yuv = ct.rgb_to_yuv(rgb)
rgb2 = ct.yuv_to_rgb(yuv)
print("Initial rgb color: ", rgb)
print("Obtained yuv color: ", yuv)
print("Obteined rgb color: ", rgb2)


#EXERCISE 3:
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



#EXERCISE 4:
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




#EXERCISE 5:
ZIGZAG_ORDER = [
    0, 1, 8, 16, 9, 2, 3, 10,
    17, 24, 32, 25, 18, 11, 4, 5,
    12, 19, 26, 33, 40, 48, 41, 34,
    27, 20, 13, 6, 7, 14, 21, 28,
    35, 42, 49, 56, 57, 50, 43, 36,
    29, 22, 15, 23, 30, 37, 44, 51,
    58, 59, 52, 45, 38, 31, 39, 46,
    53, 60, 61, 54, 47, 55, 62, 63
    ]

def zigzag(matrix):    
    return matrix.flatten()[ZIGZAG_ORDER].tolist()

def inverse_zigzag(arr):
    block = np.zeros(64)
    block[ZIGZAG_ORDER] = arr
    return block.reshape(8, 8)

#To check it works:
#m = np.arange(64).reshape(8, 8)
#print(zigzag(m))
#print(inverse_zigzag(ZIGZAG_ORDER))

#EXERCISE 6
class dct:
    JPEG_LUMINANCE = np.array([
    [16, 11, 10, 16, 24, 40, 51, 61],
    [12, 12, 14, 19, 26, 58, 60, 55],
    [14, 13, 16, 24, 40, 57, 69, 56],
    [14, 17, 22, 29, 51, 87, 80, 62],
    [18, 22, 37, 56, 68, 109, 103, 77],
    [24, 35, 55, 64, 81, 104, 113, 92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103, 99]
    ])
    
    
    def encode(block):
        dct_coeffs = scipy.fftpack.dct(block)
        return dct_coeffs


    def decode(arr):
        return scipy.fftpack.idct(arr)


    

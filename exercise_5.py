#code from: https://github.com/MrBled/JPEG_tutorial_Image-Video_Processing/blob/main/jpeg-tutorial-standalone.py
import numpy as np
import scipy

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


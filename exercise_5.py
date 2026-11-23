#code from: https://github.com/MrBled/JPEG_tutorial_Image-Video_Processing/blob/main/jpeg-tutorial-standalone.py
import numpy as np

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
    return matrix.flatten()[ZIGZAG_ORDER]

def inverse_zigzag(arr):
    """Convert a 1D zig-zag-ordered array back to 8x8 block."""
    block = np.zeros(64)
    block[ZIGZAG_ORDER] = arr
    return block.reshape(8, 8)

#To check it works:
#m = np.arange(64).reshape(8, 8)
#print(zigzag(m))
#print(inverse_zigzag(ZIGZAG_ORDER))
import numpy as np
import scipy
from exercise_5 import zigzag, inverse_zigzag, ZIGZAG_ORDER
 
def encode(s: list) -> list:
    result = []
    n = len(s)
    i = 0

    while i < n:

        # Count occurrences of current character
        count = 1
        while i < n - 1 and s[i] == s[i + 1]:
            count += 1
            i += 1

        # Append character and its count to result list
        if count > 1:
            vec = [s[i], count]
            result.append(vec)
        else:
            result.append(s[i])
            
        i += 1

    return result

m = np.array([
    0, 0, 0, 0, 3, 3, 3, 10,
    17, 24, 32, 25, 18, 11, 4, 5,
    12, 19, 26, 33, 40, 48, 41, 34,
    27, 20, 13, 6, 7, 14, 21, 28,
    35, 42, 49, 56, 57, 50, 43, 36,
    29, 22, 15, 15, 15, 15, 15, 15,
    58, 59, 52, 45, 31, 31, 31, 46,
    53, 60, 61, 54, 55, 55, 55, 55,
]).reshape(8, 8)

m_zigzag = zigzag(m)
encoded = encode(m_zigzag)
print("Zigzag of m: ", m_zigzag)
print("Encoded: ", encoded)


def decode(s: list) -> list:
    result = []

    for i in s:
        if isinstance(i, list):
            value = i[0]
            reps = i[1]
            for j in range(reps):
            # Append character and its count to result list
                result.append(value)
        else:
            result.append(i)

    return result


decoded = decode(encoded)
print("Decoded: ", decoded)
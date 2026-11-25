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
        vec = [s[i], count]
        result.append(vec)

        i += 1

    return result

m = np.arange(64).reshape(8, 8)
m_zigzag = zigzag(m)
encoded = encode(m_zigzag)
print("Zigzag of m: ", m_zigzag)
print("Encoded: ", encoded)


def decode(s: list) -> list:
    result = []
    n = len(s)

    for i in range(n):
        value = s[i][0]
        reps = s[i][1]
        for j in range(reps):
        # Append character and its count to result list
            result.append(value)

    return result
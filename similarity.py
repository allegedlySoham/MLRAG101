import math;
import numpy as np
def cosine_similarity(a,b):
    dotproduct = np.dot(a,b)
    magnitudeA = math.sqrt(sum(x**2 for x in a))
    magnitudeB = math.sqrt(sum(x**2 for x in b))
    similarity = dotproduct/(magnitudeA*magnitudeB)
    return similarity;
import re
import numpy as np
import scipy.spatial.distance

file_obj = open("sentences.txt")

lines = []
for line in file_obj:
    if (len(line) > 0):
        lines.append(line.lower())

tokens = []
for line in lines:
    t = re.split('[^a-z]', line)
    t = filter(lambda token: token, t)
    tokens.append(t)


word_index = {}
cur_index = 0

for tokens_array in tokens:
    for token in tokens_array:
        if (not (token in word_index)):
            word_index[token] = cur_index
            cur_index = cur_index + 1

matrix = np.array([])
for tokens_array in tokens:
    freq = np.zeros(len(word_index))
    for token in tokens_array:
        freq[word_index[token]] = freq[word_index[token]] + 1
    matrix = np.append(matrix, freq)

matrix = matrix.reshape((len(tokens), len(word_index)))

cos = []
for index in xrange(0, len(matrix)):
    cos.append((scipy.spatial.distance.cosine(matrix[0], matrix[index]), index))

cos.sort()
print cos
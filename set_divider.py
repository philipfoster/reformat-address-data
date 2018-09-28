from pprint import pprint
import random


lines = []
with open('opennlp-converted.txt', 'r') as inFile:
    lines = inFile.readlines()

random.shuffle(lines)

# 90% of the total file (total = 9403)
num_train = 9403

train_set = lines[:num_train]
test_set = lines[num_train:]

with open('train_set.txt', 'w') as outfile:
    for line in train_set:
        outfile.write('%s' % line)

with open('test_set.txt', 'w') as outfile:
    for line in test_set:
        outfile.write('%s' % line)


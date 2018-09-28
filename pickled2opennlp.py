# This program will convert a pickled dataset from https://onethinglab.com/2018/03/05/extracting-addresses-from-text/ into
# a format suitable to be imported for OpenNLP to train a TokenNameFinderModel
#
# Note: The output isn't *quite* suitable to be used directly. The easiest way to fix this is to use a find-and-replace tool built into
# your text editor, and replace the following regex with an empty string: (^b('|"))|(("|')$)|`|''


import pickle

file = open("IOB_tagged_addresses.pkl", "rb")

# load pickle file into an array
pickleExport = []
pickleExport.append(pickle.load(file))
pickleExport = pickleExport[0]

file.close()

sentences = []

for words in pickleExport: # sentence
    sentence = ''
    lastWasInside = False
    for taggedWord in words: # individual tagged word
        if taggedWord[1] == 'O':
            # Not part of address
            if lastWasInside:
               sentence += taggedWord[0][0] + ' <END> ' 
            else:
                sentence += taggedWord[0][0] + ' '
            lastWasInside = False
        elif taggedWord[1] == 'B-GPE': 
            # beginning of address
            if lastWasInside:
                sentence += ' <END> <START:address> ' + taggedWord[0][0] + ' '
            else:
                sentence += ' <START:address> ' + taggedWord[0][0] + ' '
            lastWasInside = True
        elif taggedWord[1] == 'I-GPE':
            lastWasInside = True
            sentence += taggedWord[0][0] + ' '     
    sentences.append(sentence)


file = open('train_set.txt', 'w')
for s in sentences:
    ascii = s.encode('ascii', 'ignore')
    file.write('%s\n' % ascii)



file.close()

# pprint(sentences)

import pickle
from pprint import pprint

# Data source: https://onethinglab.com/2018/03/05/extracting-addresses-from-text/
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


file = open('opennlp-converted.txt', 'w')
for s in sentences:
    ascii = s.encode('ascii', 'ignore')
    file.write('%s\n' % ascii)



file.close()

# pprint(sentences)

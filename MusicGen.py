'''
Project Name: Simple programmable music synthesis module
File name: MusicGen.py
Author: SenthilRaj D.
Date: 13/12/2017
'''

# Imports required python packages
import re
import os
from pysine import sine

# Get current working directory
dirpath = os.getcwd()
file_name = 'tone.txt'

# Open input file
fp = open(dirpath+'/'+file_name,'r')

# Read chords and frequency
line = fp.read()
read_data = line.split('\n')

# Parse the chords and frequency values in list format.
chords = re.findall('[A-Z,a-z,0-9]+',read_data[0])
freq = re.findall('[0-9]+',read_data[1])
print(chords, freq)

# If frequency is not present, set the default values
if not freq:
    choices = {'Sa': 523, 'Ri': 587, 'Ga': 659, 'Ma': 698, 'Pa': 784, 'dha': 880, 'ni': 988,'0':0}
    freq = []
    for i in range(len(chords)):
        freq.append(choices[chords[i]])
        sine(frequency=freq[i], duration=1.0)
    print(freq)




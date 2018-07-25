# Extract all of the repetitive elements from a genome scaffolds according to the location of each element.
#!/usr/bin/python

import sys
import re

FASTA= sys.argv[1]
RE_file= sys.argv[2]

#fasta = open(r'test.fa.txt', 'U')

fasta= open(FASTA, 'U') # universal newlines mode
fasta_dict= {}
for line in fasta:
    line= line.strip() #Returns a copy of the string with the leading and trailing characters removed.
    if line == '':
        continue
    if line.startswith('>'):
        seqname= line.lstrip('>') #Remove '>' at begining position. Returns a copy of the string with leading characters removed.
       # seqname= re.sub('\..*', '', seqname)
        fasta_dict[seqname]= ''
    else:
        fasta_dict[seqname] += line
fasta.close()
#print fasta_dict

rep = open(RE_file, 'U')
for line in rep:
    line= line.strip().split('\t')
    outname= line[4] + ':' + line[5] + '-' + line[6] + '_' + line[10]
    print '>' + outname
    s= int(line[5])
    e= int(line[6])
    print fasta_dict[line[4]][s:e]
rep.close()
sys.exit()

# python extract_repetitive_elements.py genome_scaff.fa ids.txt > result.fasta

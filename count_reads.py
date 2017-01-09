# -*- coding: utf-8 -*-
"""
Count reads for samples specified in a mapping file
Usage: python count_reads.py -i UPA_5000sq.fastq -m map.txt -c Acidification_study_strict -w acidification

Created on Jan 09 2015

@author: VanessaRM
"""


from Bio import SeqIO
import pandas as pd
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('-i', '--fastq_input', help='The path to the input fastq file', required=True)
parser.add_argument('-m', '--map', help='The path to the mapping file', required=True)
parser.add_argument('-c', '--column', help='The column to base the counts', required=True)
parser.add_argument('-w', '--wanted', help='The the identifier', required=True)


args = parser.parse_args()
fastq_input = args.fastq_input
mapping_file_input = args.map
col = args.column
ident = args.wanted


store_wanted_samples = []


map_file = pd.read_table(mapping_file_input)
for index,row in map_file.iterrows():
    if getattr(row,col) == ident: #getattr(row,col) is the same as row.col
        store_wanted_samples.append(row[0])
   
        
counter = 0        
for seq_record in SeqIO.parse(fastq_input , "fastq"):
    sample_full =  seq_record.id.split("_")
    sample_ID = sample_full[0]
    if sample_ID in store_wanted_samples:
        counter += 1
    
print("")
print ("%i reads in your file" %(counter,))
print("")



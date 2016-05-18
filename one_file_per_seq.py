# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 13:44:00 2015

"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-i', '--input_fasta', help='The path to the input fasta file with CDSs sequences', required=True)
args = parser.parse_args()
input_fasta = args.input_fasta


for seq_record in SeqIO.parse(input_fasta, "fasta"):
    new_id = seq_record.id + ".fas"
    SeqIO.write(seq_record,new_id, "fasta")
    
    
    

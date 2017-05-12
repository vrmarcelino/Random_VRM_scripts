#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:18:09 2017

@author: VanessaRM
"""

#import modules
from Bio import Entrez
from Bio import SeqIO
from argparse import ArgumentParser

Entrez.email = "vrmarcelino@gmail.com" # tell NCBI who you are


parser = ArgumentParser()
parser.add_argument('-i', '--input_GIs', help='The path to the list of genebank accession numbers', required=True)
args = parser.parse_args()


AssNumbers_open = open(args.input_GIs, "r")
AssNumbers = AssNumbers_open.read().split(',')

handle = Entrez.efetch(db="nuccore", id=AssNumbers, rettype="gb", retmode="text")

# transform to Seq records and save in different files:
records = SeqIO.parse(handle, "gb")

for seq_record in records:
    print (seq_record.id)
    new_id = seq_record.id + ".gb"
    SeqIO.write(seq_record,new_id,"gb")


print ("Done!")

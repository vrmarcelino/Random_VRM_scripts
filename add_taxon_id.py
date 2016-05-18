# -*- coding: utf-8 -*-
"""
Put species names on reference dataset (RDP format)
Created on Sat Aug 29 08:58:12 2015

@author: VanessaRM
"""

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

input_fasta = "reference_sequences_aligned.fna"
taxon_name = "id_to_taxonomy_map.txt"

new_aln = []
# Create a dictionary with sequence IDs:
dict_taxons = {}
tax = open(taxon_name, "r" )
for line in tax:
    identifier_1 = line.replace('\t',';')
    identifier_split = identifier_1.split(';')
    seq_id = str(identifier_split[0])
    print seq_id
    species = identifier_split[-1]
    print species
    
    dict_taxons ['%s' %seq_id] = [species]
    
    
for seq_record in SeqIO.parse(input_fasta, "fasta"):
    
    seq = str(seq_record.seq)    
    
    take_out_dot = seq_record.id.split('.')
    seq_wo_dot = take_out_dot[0] 
    
    if seq_wo_dot in dict_taxons.viewkeys():
        new_id = str(seq_wo_dot) + str(dict_taxons[seq_wo_dot])
        print new_id
        
        new_record = SeqRecord(Seq(seq), id= new_id, description='')
        new_aln.append(new_record)

count = SeqIO.write(new_aln,"Aln_with_tax_names.fasta", "fasta")
print""
print "Done. Saved %i sequences in the aln file." % (count)
print""


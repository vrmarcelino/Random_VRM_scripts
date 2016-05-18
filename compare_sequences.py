# compare CDSs files and point out differences in the genes
# 14 - 01 - 2015

from Bio import SeqIO

new_genome = "Derbesia_sp_WEST4838.fasta"
old_genome = "old_Derbesia_sp_WEST4838.fasta"

store_news = {}
store_old = {}

#store info about the new genome
for seq_record in SeqIO.parse(new_genome , "fasta"):
	gene = seq_record.id
	seq = seq_record.seq
	store_news[gene] = seq

# Check how it differs from the old one:
for seq_record in SeqIO.parse(old_genome , "fasta"):
	if seq_record.id in store_news:
		new_id = seq_record.id
		if str(seq_record.seq) in store_news[new_id]:
			print "seq ok"
		if len(str(seq_record.seq)) == len(store_news[new_id]):
			print "lenght ok"
		else:
			print ""
			print "changes detected in %s" %(new_id)
			print ""
	else:
		print "gene %s not in new database" %(seq_record.id)



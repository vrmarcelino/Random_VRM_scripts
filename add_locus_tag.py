## ENA chloroplast genome submission
## This script adds the locus tag to each Gene and CDS annotation
## the locus tag prefix can be obtained from Webin (study section)

### Rules: Locus tags should be assigned to all protein coding and non-coding genes such as structural RNAs.
# /locus_tag should appear on gene, mRNA, CDS, intron, exon, tRNA, rRNA, etc. 
# We discourage the use of the /locus_tag qualifier on repeat_region and misc_feature features 
# The same /locus_tag should be used for all components of a single gene. 
# For example, all of the exons, CDS, mRNA and gene features for a particular gene would have the same /locus_tag. 


from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
import re
from argparse import ArgumentParser


# Define input and output variables:
parser = ArgumentParser()
parser.add_argument('-i', '--input_file', help='The path to the genome embl file', required=True)
parser.add_argument('-p', '--locus_tag_prefix', help='The prefix of your locus tag', required=True)

args = parser.parse_args()
genome_file = args.input_file
locus_prefix = str(args.locus_tag_prefix)

#locus_prefix = "BN5726" # Webin
#genome_file = "Ostreobium_quekettii_SAG699.embl"

original_genome = SeqIO.read(genome_file, "embl")
x = 0
final_features = []
store_tags = {}

for f in original_genome.features:
	# find "genes related stuff", exclude misc_features and repeats:
	if re.search ('gene', str(f)) != None:
		# loop through qualifiers and check if gene is in our dictionary (but exclude gene products)
		for key, value in list(f.qualifiers.iteritems()): 
			if key == 'gene':
				if str(value) in store_tags:
					f.qualifiers["locus_tag"] = store_tags[str(value)]
				else:
					x = x + 1
					store_tags[str(value)] = "%s_%s" % (locus_prefix, x)
					f.qualifiers["locus_tag"] = store_tags[str(value)]

# Save it
with open("genome_w_tags.embl","w") as for_ena:
    SeqIO.write(original_genome, for_ena, "embl")

print "Done! Tagged genome file saved as genome_w_tags.embl"

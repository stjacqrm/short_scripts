#!/usr/bin/env python3

# Description: Remove specific fastas from a multi fasta file using a custom made table (tsv)
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov

####################################################################
###                     Helpful hints                            ###
### Use grep "^>" fasta.fasta to help generate the table         ###
### Example lookup table line: what_you_want_gone                ###
####################################################################

from Bio import SeqIO
import argparse
import csv

parser=argparse.ArgumentParser(description="program that removes specific fastas from a multi-fasta file")
parser.add_argument("-i", help="input fasta", type= str, required=True)
parser.add_argument("-t", help="tsv file with fasta headers of fastas to be removed", required=True)
parser.add_argument("-o", help="output fasta")
args = parser.parse_args()

# create an output file
newfasta=open(args.o,'w')

# prep the header tsv
header_set=set(line.strip() for line in open(args.t))

# do the actual work
fasta_files=open(args.i)
fasta_file=SeqIO.parse(fasta_files, "fasta")
for seq in fasta_file:
    try:
        header_set.remove(seq.name)
    except KeyError:
        newfasta.write(seq.format("fasta"))
        continue

if len(header_set) != 0:
    print(len(header_set),'of the headers from list were not identified in the input fasta file.', file=sys.stderr)

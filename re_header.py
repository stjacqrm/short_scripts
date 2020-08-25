#!/usr/bin/env python3

# Description: Replace specific headers from a fasta file using a custom made lookup table (tsv)
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov


####################################################################
###                     Helpful hints                            ###
### Use grep "^>" fasta.fasta to help generate that lookup table ###
### Example lookup table line: >old_header  >new_header          ###
####################################################################


import argparse
import csv

parser=argparse.ArgumentParser(description="program that replaces fasta headers")
parser.add_argument("-i", help="input fasta", type= str, required=True)
parser.add_argument("-l", help="tsv file with replacement header lines", required=True)
parser.add_argument("-o", help="output fasta")
args = parser.parse_args()

# create an output file
newfasta=open(args.o,'w')

# load lookup table into dict format
lookup_dict = {}
with open(args.l) as lookup_handle:
    lookup_list = csv.reader(lookup_handle, delimiter='\t')
    for entry in lookup_list:
        lookup_dict[entry[0]] = entry[1]
        print("table lookup functioning")

# read in the fasta file line by line and replace the header if it is in the lookup table
fasta_file=open(args.i)
for line in fasta_file:
    line = line.rstrip("\n")
    print("space stripped after line")
    if line.startswith('>'):
        print("string starts with '>'")
        if line in lookup_dict.keys():
            print("original fasta header was identified in the new header tsv file")
            newname = lookup_dict[line]
            newfasta.write(newname+"\n")
            print("newname was found and is being incorporated into the fasta file")
        else:
            print("original fasta header not in the new header tsv file")
            newfasta.write(line+"\n")
            print("no new name was identified, original name was correct")
    else:
        newfasta.write(line+"\n")
        print("no fastas needed a change")

print("all fasta files were reheaded and saved to " + args.o)

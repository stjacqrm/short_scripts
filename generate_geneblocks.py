#!/usr/bin/env python

# Description: Create data vizualisations of genbank files
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov

####################################################################
###                     Helpful hints                            ###
###    use BCBio (chapmanb) script (gff_to_gb.py) to get gb      ###
###           visit github.com/champanb for more                 ###
####################################################################

import sys
import argparse
from geneblocks import CommonBlocks, load_record, DiffBlocks
import matplotlib.pyplot as plt
import Bio


parser=argparse.ArgumentParser(description="Create data vizualisations of genbank files")
parser.add_argument("-r", help="gb file for reference genome", type= str, required=True)
parser.add_argument("-q", help="gb file for query genome", required=True)
parser.add_argument("-o", help="output file",default="genome_map_differences.png")
args = parser.parse_args()

seq_1 = load_record(args.r)
seq_2 = load_record(args.q)

# FIND COMMON BLOCKS AND DIFFS
common_blocks = CommonBlocks.from_sequences({str(args.r): seq_1, str(args.q): seq_2})
diff_blocks = DiffBlocks.from_sequences(seq_1, seq_2)

# PLOT EVERYTHING
fig, axes = plt.subplots(3, 1, figsize=(20, 20))
common_blocks.plot_common_blocks(axes=axes[:-1])
diff_blocks.plot(ax=axes[-1], separate_axes=False)
axes[-1].set_xlabel("Changes in seq2 vs. seq1")
fig.savefig(args.o, bbox_inches='tight')

#!/usr/bin/env python

# Description: trying to get a good output for sars stuff
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov

####################################################################
###                     Helpful hints                            ###
###             read a good book when stressed                   ###
####################################################################

import sys
import argparse
from geneblocks import CommonBlocks, load_record, DiffBlocks
from collections import defaultdict, OrderedDict
import matplotlib.pyplot as plt
import Bio
import numpy as np
from Bio import SeqIO
from dna_features_viewer import BiopythonTranslator
from dna_features_viewer import GraphicRecord
from dna_features_viewer import CircularGraphicRecord
from dna_features_viewer import GraphicFeature
import tempfile
import subprocess


parser=argparse.ArgumentParser(description="Create data vizualisations of genbank files")
parser.add_argument("-r", help="gb file for reference genome", type= str, required=True)
parser.add_argument("-q", help="gb file for query genome", required=True)
parser.add_argument("-o", help="output file",default= "genome_map")
args = parser.parse_args()

# make the custom translator
class CommonBlocksRecordTranslator(BiopythonTranslator):

    label_fields = [
        "Name",
        "note",
        "gene",
        "product",
        "source",
        "locus_tag",
        "label",
    ]

    ignored_features_types = ("diff_equal","CDS","mRNA","source")
    default_box_color = None


    def compute_feature_color(self, feature):
        if feature.qualifiers.get("is_block", False):
            return BiopythonTranslator.compute_feature_color(self, feature)
        elif feature.type == "gene":
            return "green"
        elif feature.type == "exon":
            return "blue"
        elif feature.type == "note":
            return "pink"
        elif feature.type == "mRNA_with_minus_1_frameshift":
            return "gold"
        else:
            return "grey"

    @staticmethod
    def compute_feature_box_linewidth(f):
        return 1 if f.qualifiers.get("is_block", False) else 0

    @staticmethod
    def compute_feature_fontdict(f):
        return {"fontsize": 12 if f.qualifiers.get("is_block", False) else 9}

    def compute_feature_label(self, feature):
        if feature.type == 'CDS':
            return None
        elif feature.type == "mRNA":
            return None
        elif feature.type == "source":
            return None
        elif feature.type == "exon":
            return "exon"
        elif feature.type == "mRNA_with_minus_1_frameshift":
            return "frameshift"
        else:
            return BiopythonTranslator.compute_feature_label(self, feature)

def diff_blocks_to_csv(self, target_file=None):
    """Write the diff blocks into a CSV file.
    If a target CSV file is provided the result is written to that file.
    Otherwise the result is returned as a string.
    The columns of the CSV file are "block", "size", "locations", and
    sequence.
    """
    csv_content = "\n".join(
        ["block;size;locations;sequence"]
        + [
            ";".join(
                [
                    block_name,
                    str(len(data["sequence"])),
                    " ".join(
                        [
                            "%s(%d, %d, %d)" % (cst, start, end, strand)
                            for (cst, (start, end, strand)) in data["locations"]
                        ]
                    ),
                    data["sequence"],
                ]
            )
            for block_name, data in self.diff_blocks.items()
        ]
    )
    if target_file:
        with open(target_file, "w+") as f:
            f.write(csv_content)
    else:
        return csv_content

cr = CommonBlocksRecordTranslator()
# load the reference genbank file with custom translator and produce a genome map of JUST the reference genome
seq_1 = cr.translate_record(args.r)
seq_1.ticks_resolution = 1000
ax, _ = seq_1.plot(figure_width=30)
ax.figure.tight_layout()
ax.figure.savefig("ref_genome_map.png")

# load the query genbank file with custom translator and produce a genome map of JUST the query genome
seq_2 = cr.translate_record(args.q)
seq_2.ticks_resolution = 1000
ax, _ = seq_2.plot(figure_width=30)
ax.figure.tight_layout()
ax.figure.savefig("query_genome_map.png")

# load the genbank files as records
seq_1 = load_record(args.r)
seq_2 = load_record(args.q)

# filter the records based on new translators
#translator_class  = CommonBlocksRecordTranslator()
#translator_class  = DiffRecordTranslator()

# identify the commonblocks and the diffblocks
common_blocks = CommonBlocks.from_sequences({str(args.r): seq_1, str(args.q): seq_2})
diff_blocks = DiffBlocks.from_sequences(seq_1, seq_2)
print(diff_blocks)
diff_blocks.diff_blocks_to_csv(target_file="blocks.csv")

# plot commonblocks and diff blocks
fig, axes = plt.subplots(3, 1, figsize=(30, 20))
common_blocks.plot_common_blocks(axes=axes[:-1])
diff_blocks.plot(ax=axes[-1], separate_axes=False)
axes[-1].set_xlabel("Changes in seq2 vs. seq1")
fig.savefig(args.o +".png", bbox_inches='tight')

# write commom blocks to a csv
common_blocks.common_blocks_to_csv(target_file=args.o+"_common_blocks.csv")

# write mutations to a csv

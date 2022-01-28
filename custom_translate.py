#!/usr/bin/env python

# Description: trying to fix vigor output file fire
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov

####################################################################
###                     Helpful hints                            ###
###                 get plenty of sleep                          ###
####################################################################

import sys
import argparse
from dna_features_viewer import BiopythonTranslator

parser=argparse.ArgumentParser(description="trying to fix vigor output file fire")
parser.add_argument("-g", help="gb file", required=True)
parser.add_argument("-o", help="output file",default="fixed_genbank_file.png")
args = parser.parse_args()

class MyCustomTranslator(BiopythonTranslator):
    label_fields = [
        "Name",
        "note",
        "gene",
        "product",
        "source",
        "locus_tag",
        "label",
    ]


    def compute_feature_color(self, feature):
        if feature.type == "gene":
            return "green"
        elif feature.type == "exon":
            return "blue"
        elif feature.type == "mRNA_with_minus_1_frameshift":
            return "gold"
        else:
            return "red"

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

    def compute_filtered_features(self, features):
        """Do not display repeated information. The visual is no longer useful with so much data."""
        return [
            feature for feature in features
            if (feature.type != "CDS")
            if (feature.type != "mRNA")
            if (feature.type != "source")
        ]


graphic_record = MyCustomTranslator().translate_record(args.g)
print(graphic_record)
ax, _ = graphic_record.plot(figure_width=30)
ax.figure.tight_layout()
ax.figure.savefig(args.o)

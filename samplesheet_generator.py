#!/usr/bin/env python3

import fnmatch
import os
import csv
import argparse


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)

parser=argparse.ArgumentParser(description="program that automatically makes a samplesheet")
parser.add_argument("--reads", help="input reads", type= dir_path, required=True)
parser.add_argument("--out", help="output samplesheet", default="sampleSheet.csv")
args = parser.parse_args()


class sample_values:
    def __init__(self,id):
        self.id = id
        self.fastq_1 = "NA"
        self.fastq_2 = "NA"


dr = (args.reads)

samples = {}


for root, dirs, files in os.walk(dr):
    for file in files:
        id = file.split("_")[0]
        sample = sample_values(id)

        for file in fnmatch.filter(files, "*_R1_*.fastq.gz"):
            mini_id = file.split("_")[0]
            if mini_id == id:
              sample.fastq_1 = os.path.abspath(os.path.join(root, file))

        for file in fnmatch.filter(files, "*_R2_*.fastq.gz"):
            mini_id = file.split("_")[0]
            if mini_id == id:
              sample.fastq_2 = os.path.abspath(os.path.join(root, file))

        samples[id] = sample

with open(args.out, 'w') as f:
  writer = csv.writer(f,delimiter=',')
  writer.writerow(["sample","fastq_1", "fastq_2"])
  for id in samples:
        sample = samples[id]
        writer.writerow([sample.id,sample.fastq_1,sample.fastq_2])

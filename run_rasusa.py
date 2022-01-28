#!/usr/bin/python

import subprocess

subprocess.Popen(
    'docker run --rm=True -u $(id -u):$(id -g) -v $PWD:/data staphb/rasusa rasusa -c 35 -g 29 -i *_R1_L001.fastq.gz '
    '-i *_R2_L001.fastq.gz -o *_40_R1_L001.fastq.gz -o *_40_R2_L001.fastq.gz',
    shell=True)

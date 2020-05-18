#!/usr/bin/env python3

# world's smallest python script brought to you by Rachael St. Jacques
import shutil
import os
import sys

dr = sys.argv[1]

for root, dirs, files in os.walk(dr):
    for file in files:
        if file == "contigs.fa":
            spl = root.split("/"); newname = spl[-1]; sup = ("/").join(spl[:-1])
            newname_fasta = shutil.copy(root+"/"+file, sup+"/"+newname+".fasta")
            try:
                os.mkdir('assembly_fasta_files')
            except OSError:
                pass
            shutil.move(newname_fasta, 'assembly_fasta_files')

#!/usr/bin/env python3

# Description: A script that converts a directory of bam files into a table of readcounts.
# Authors: Logan Fink and Rachael St. Jacques
# email: logan.fink@dgs.virginia.gov, rachael.stjacques@dgs.virginia.gov


####################################################################
###                     Helpful hints                            ###
### Use grep "^>" fasta.fasta to help generate that lookup table ###
### Example lookup table line: >old_header  >new_header          ###
####################################################################


import argparse
import os
import subprocess
import sys
import glob

parser = argparse.ArgumentParser(description="A script that converts output of readcounts into a table.")
parser.add_argument("-i", help="path to the directory of bam files", required=True)
parser.add_argument("-f", help="path to the reference fasta file", required=True)
parser.add_argument("-o", help="input read-counts file", default="readcounts.tsv")
args = parser.parse_args()

Mutations = {}
MutationsNum = {}
MutationsA = {}
MutationsC = {}
MutationsT = {}
MutationsG = {}
multiIsoOutbreakDict = {}

dir = args.i
for i in os.listdir(dir):
    subprocess.run([sys.executable, "bam-readcount -w 1 -f " + args.f, "print('ocean')"])


with open(final.readcounts, 'r') as f:
    flines = f.readlines()
    for n in range(len(flines)):
        line = flines[n]
        linest = line.strip()
        linesp = linest.split('\t')
        if len(linesp) == 1:
            m = int(n + 1)
            try:
                while len(flines[m].split('\t')) > 2:
                    lime = flines[m]
                    limest = lime.strip()
                    limesp = limest.split('\t')
                    A = limesp[5].split(":")[1]
                    Amqual = limesp[5].split(":")[2]
                    Abqual = limesp[5].split(":")[3]
                    C = limesp[6].split(":")[1]
                    Cmqual = limesp[6].split(":")[2]
                    Cbqual = limesp[6].split(":")[3]
                    G = limesp[7].split(":")[1]
                    Gmqual = limesp[7].split(":")[2]
                    Gbqual = limesp[7].split(":")[3]
                    T = limesp[8].split(":")[1]
                    Tmqual = limesp[8].split(":")[2]
                    Tbqual = limesp[8].split(":")[3]
                    Mutations[str(linesp)] = [limest]
                    MutationsNum[str(linesp)] = [limesp[3]]
                    if int(A) > 0:
                        MutationsNum[str(linesp)] += [["A", A, Amqual, Abqual]]
                    if int(C) > 0:
                        MutationsNum[str(linesp)] += [["C", C, Cmqual, Cbqual]]
                    if int(G) > 0:
                        MutationsNum[str(linesp)] += [["G", G, Gmqual, Gbqual]]
                    if int(T) > 0:
                        MutationsNum[str(linesp)] += [["T", T, Tmqual, Tbqual]]
                    MutationsA[str(linesp)] = [A, Amqual, Abqual]
                    MutationsC[str(linesp)] = [C, Cmqual, Cbqual]
                    MutationsG[str(linesp)] = [G, Gmqual, Gbqual]
                    MutationsT[str(linesp)] = [T, Tmqual, Tbqual]
                    m = int(m + 1)
            except:
                break

'''
for i in MutationsNum:
    if int(MutationsA[i][0])>0:
        print(i, MutationsNum[i], "A ", MutationsA[i][0])
    if int(MutationsC[i][0])>0:
        print(i, MutationsNum[i], "C ", MutationsC[i][0])
    if int(MutationsG[i][0])>0:
        print(i, MutationsNum[i], "G ", MutationsG[i][0])
    if int(MutationsT[i][0])>0:
        print(i, MutationsNum[i], "T ", MutationsT[i][0])
'''
# Make uniq lists of isolates and mutations
isolatesss = []
mutsss = []
for i in MutationsNum:
    ist = i.strip("[").strip("]").strip("'")
    isp = ist.split(" ")
    isolatesss += [isp[0]]
    mutsss += [isp[1]]

isolates = list(set(isolatesss))
muts = list(set(mutsss))

# Make a pairwise dictionary to start making the matrix
pairwise = {}
for x in range(len(isolates)):
    pairwise[isolates[x]] = ['0'] * len(muts)
    for y in range(len(muts)):
        strt = str("['")
        mid = str(" ")
        clse = str("']")
        if strt + str(isolates[x]) + mid + str(muts[y]) + clse in MutationsNum:
            pairwise[isolates[x]][y] = str(MutationsNum[strt + str(isolates[x]) + mid + str(muts[y]) + clse])
print(muts)
for item in pairwise:
    print(item, pairwise[item])

strmuts = []
for i in muts:
    print(i)
    strmuts += [str(i)]
print(strmuts)

# Write the matrix
with open(args.o, 'w') as w:
    w.write(' ' + '\t' + '\t'.join(strmuts) + '\n')
    for i in pairwise:
        w.write(str(i) + '\t' + '\t'.join(pairwise[i]) + '\n')

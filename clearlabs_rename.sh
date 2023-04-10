#!/bin/bash

echo 'Extracting Files'
tar xf *.tar

echo 'Fixing Filenames'
for fname in *; do
  name="${fname%\.*}"
  extension="${fname#$name}"
  newname="${name//./_}"
  newfname="$newname""$extension"
  if [ "$fname" != "$newfname" ]; then
    #echo mv "$fname" "$newfname"
    mv "$fname" "$newfname"
  fi
done

for fname in *\ *; do 
  mv "$fname" "${fname// /_}"; 
done

echo 'Sorting files into appropriate directories'
mkdir fasta && mv *.fasta fasta
mkdir fastq && mv *.fastq fastq
mkdir bam && mv *.bam bam
mkdir index_bam && mv *.bai index_bam
mkdir vcf && mv *.vcf vcf
mkdir metrics && mv *.csv metrics

echo 'Moving directories into data'
mkdir data
mv bam data
mv fasta data
mv fastq data
mv index_bam data
mv vcf data

echo 'Removing tar file'
rm *.tar

echo 'Done'

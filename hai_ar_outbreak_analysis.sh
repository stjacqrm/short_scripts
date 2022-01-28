#!/bin/bash


staphb-wf hickory reads;
cd hickory_results && cp *.fasta centroid_ref.fasta && cp centroid_ref.fasta .. && cd ..;

staphb-wf dryad main -cg -s -r centroid_ref.fasta --config dryad_config.config -ar --report reads;

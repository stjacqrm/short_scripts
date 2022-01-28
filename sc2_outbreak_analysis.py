#!/usr/bin/env python3

import subprocess
import shutil
import os
import glob
import csv
import argparse
from gooey import GooeyParser

@Gooey
def main():
    parser = argparse.ArgumentParser(description='SC2 outbreak analysis pipeline.')
    parser.add_argument('--output','-o', type=str, help="output directory", required=True, default="sc2_analysis_resutls", widget='MultiFileSaver')
    parser.add_argument('--monroe_run','-r', type=str, help="path to Monroe run", required=True, widget='DirChooser')
    parser.add_argument('--analysis_samples','-s', type=str, help="path to analysis samples file in tsv format", required=True, widget='FileChooser')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

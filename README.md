# short_scripts

Just some short scripts that solve the world's smallest bioinformatics problems.

## Getting Started

### Prerequisites

What dependencies you need to run short_scripts

```
python3.6+
```

### Installing Dependencies

#### Installing python3.6+
First, check your version of python

```
$ python -v
```

If you don't have python3.6+, use Anaconda to install:

```
$ sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6
$ wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
$ bash Anaconda3-2019.10-Linux-x86_64.sh
$ source ~/.bashrc
```

### Installing the code

To get short_scripts, clone this repository:

```
$ git clone https://github.com/stjacqrm/short_scripts.git
```

## Current scripts

#### Changerator

```
changerator.py
```
Changerator is there for you when you've used a genome assembler that creates a directory with a contigs.fa file, but you would REALLY like for that file to be name {name_of_your_directory}.fasta and moved to a better directory.

Using changerator is super easy.

```
changerator.py /path/to/assembly/
```
Just direct the script to the directory containing all of your assembler output directories.

#### Re_header

```
re_header.py -h
```
Re_header.py is useful for those instances where you want to change some (or all) of the fasta headers in a multi fasta file. You need a tsv file with the old/original fasta header and the new header.


tsv example:
```
>old_fasta_1.fasta  >new_fasta_1.fasta
>old_fasta_2.fasta  >new_fasta_2.fasta
```

To run re_header.py:

```
$ re_header.py -i <input.fasta> -t <new_header.tsv> -o <output.fasta>
```

#### Remove_fasta.py

```
remove_fasta.py -h
```

Remove_fasta takes in a tsv file with a list of fastas you *don't* want in your multi fasta file.

When you're writing the tsv file, only write the header, not the ">" character.


tsv example:
```
dont_want_this1
dont_want_this2
dont_want_this3
```

To run remove_fasta.py:

```
$ remove_fasta.py -i <input.fasta> -t <fastas_to_remove.tsv> -o <output.fasta>
```
## Authors

* **Rachael St. Jacques** - *Me* - [stjacqrm](https://github.com/stjacqrm)

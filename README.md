# random_scripts

Just some short scripts that solve the world's smallest bioinformatics problems.

## Getting Started

### Prerequisites

What dependencies you need to run random_scripts

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

To get random_scripts, clone this repository:

```
$ git clone https://github.com/stjacqrm/random_scripts.git
```

## Current scripts

Currently, there's just the one.

```
changerator.py
```
Changerator is there for you when you've used a genome assembler that creates a directory with a contigs.fa file, but you would REALLY like for that file to be name {name_of_your_directory}.fasta and moved to a better directory.

Using changerator is super easy.

```
changerator.py /path/to/assembly/
```
Just direct the script to the directory containing all of your assembler output directories. 

## Authors

* **Rachael St. Jacques** - *Me* - [stjacqrm](https://github.com/stjacqrm)

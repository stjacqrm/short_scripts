#!/usr/bin/env python

# Description: draw V3 primers to help visualize problem regions in genomes
# Authors: Rachael St. Jacques and StackOverflow
# email: rachael.stjacques@dgs.virginia.gov

####################################################################
###                     Helpful hints                            ###
###              stillness is always within                      ###
####################################################################


import argparse
from dna_features_viewer import GraphicFeature, GraphicRecord

parser = argparse.ArgumentParser(description="Create data visualizations of V3 primer regions and problem genomes")
# parser.add_argument("-r", help="gb file for reference genome", type= str, required=True)
# parser.add_argument("-q", help="gb file for query genome", required=True)
parser.add_argument("-o", help="output file", default="V3_primers.png")
args = parser.parse_args()

# generate the primers as their own seq
features = [
    GraphicFeature(start=31, end=410, color="#ffd700", label="1"),

    GraphicFeature(start=2827, end=3210, color="#ffd700", label="10"),

    GraphicFeature(start=3145, end=3531, color="#ffd700", label="11"),

    GraphicFeature(start=3461, end=3853, color="#ffd700", label="12"),

    GraphicFeature(start=3772, end=4164, color="#ffd700", label="13"),

    GraphicFeature(start=4055, end=4450, color="#ffd700", label="14"),

    GraphicFeature(start=4295, end=4696, color="#ffd700", label="15"),

    GraphicFeature(start=4637, end=5017, color="#ffd700", label="16"),

    GraphicFeature(start=4940, end=5321, color="#ffd700", label="17"),

    GraphicFeature(start=5258, end=5644, color="#ffd700", label="18"),

    GraphicFeature(start=5564, end=5957, color="#ffd700", label="19"),

    GraphicFeature(start=321, end=726, color="#ffd700", label="2"),

    GraphicFeature(start=5868, end=6272, color="#ffd700", label="20"),

    GraphicFeature(start=6168, end=6550, color="#ffd700", label="21"),

    GraphicFeature(start=6467, end=6873, color="#ffd700", label="22"),

    GraphicFeature(start=6719, end=7117, color="#ffd700", label="23"),

    GraphicFeature(start=7036, end=7415, color="#ffd700", label="24"),

    GraphicFeature(start=7306, end=7694, color="#ffd700", label="25"),

    GraphicFeature(start=7627, end=8019, color="#ffd700", label="26"),

    GraphicFeature(start=7944, end=8341, color="#ffd700", label="27"),

    GraphicFeature(start=8250, end=8661, color="#ffd700", label="28"),

    GraphicFeature(start=8596, end=8983, color="#ffd700", label="29"),

    GraphicFeature(start=643, end=1028, color="#ffd700", label="3"),

    GraphicFeature(start=8889, end=9271, color="#ffd700", label="30"),

    GraphicFeature(start=9205, end=9585, color="#ffd700", label="31"),

    GraphicFeature(start=9478, end=9858, color="#ffd700", label="32"),

    GraphicFeature(start=9785, end=10171, color="#ffd700", label="33"),

    GraphicFeature(start=10077, end=10459, color="#ffd700", label="34"),

    GraphicFeature(start=10363, end=10763, color="#ffd700", label="35"),

    GraphicFeature(start=10667, end=11074, color="#ffd700", label="36"),

    GraphicFeature(start=11000, end=11394, color="#ffd700", label="37"),

    GraphicFeature(start=11307, end=11693, color="#ffd700", label="38"),

    GraphicFeature(start=11556, end=11949, color="#ffd700", label="39"),

    GraphicFeature(start=944, end=1337, color="#ffd700", label="4"),

    GraphicFeature(start=11864, end=12256, color="#ffd700", label="40"),

    GraphicFeature(start=12111, end=12490, color="#ffd700", label="41"),

    GraphicFeature(start=12418, end=12802, color="#ffd700", label="42"),

    GraphicFeature(start=12711, end=13096, color="#ffd700", label="43"),

    GraphicFeature(start=13006, end=13400, color="#ffd700", label="44"),

    GraphicFeature(start=13320, end=13699, color="#ffd700", label="45"),

    GraphicFeature(start=13600, end=13984, color="#ffd700", label="46"),

    GraphicFeature(start=13919, end=14299, color="#ffd700", label="47"),

    GraphicFeature(start=14208, end=14601, color="#ffd700", label="48"),

    GraphicFeature(start=14546, end=14926, color="#ffd700", label="49"),

    GraphicFeature(start=1243, end=1651, color="#ffd700", label="5"),

    GraphicFeature(start=14866, end=15246, color="#ffd700", label="50"),

    GraphicFeature(start=15172, end=15560, color="#ffd700", label="51"),

    GraphicFeature(start=15482, end=15886, color="#ffd700", label="52"),

    GraphicFeature(start=15828, end=16209, color="#ffd700", label="53"),

    GraphicFeature(start=16119, end=16510, color="#ffd700", label="54"),

    GraphicFeature(start=16417, end=16833, color="#ffd700", label="55"),

    GraphicFeature(start=16749, end=17152, color="#ffd700", label="56"),

    GraphicFeature(start=17066, end=17452, color="#ffd700", label="57"),

    GraphicFeature(start=17382, end=17761, color="#ffd700", label="58"),

    GraphicFeature(start=17675, end=18062, color="#ffd700", label="59"),

    GraphicFeature(start=1574, end=1964, color="#ffd700", label="6"),

    GraphicFeature(start=17967, end=18348, color="#ffd700", label="60"),

    GraphicFeature(start=18254, end=18672, color="#ffd700", label="61"),

    GraphicFeature(start=18597, end=18979, color="#ffd700", label="62"),

    GraphicFeature(start=18897, end=19297, color="#ffd700", label="63"),

    GraphicFeature(start=19205, end=19616, color="#ffd700", label="64"),

    GraphicFeature(start=19549, end=19939, color="#ffd700", label="65"),

    GraphicFeature(start=19845, end=20255, color="#ffd700", label="66"),

    GraphicFeature(start=20173, end=20572, color="#ffd700", label="67"),

    GraphicFeature(start=20473, end=20890, color="#ffd700", label="68"),

    GraphicFeature(start=20787, end=21169, color="#ffd700", label="69"),

    GraphicFeature(start=1876, end=2269, color="#ffd700", label="7"),

    GraphicFeature(start=21076, end=21455, color="#ffd700", label="70"),

    GraphicFeature(start=21358, end=21743, color="#ffd700", label="71"),

    GraphicFeature(start=21659, end=22038, color="#ffd700", label="72"),

    GraphicFeature(start=21962, end=22346, color="#ffd700", label="73"),

    GraphicFeature(start=22263, end=22650, color="#ffd700", label="74"),

    GraphicFeature(start=22517, end=22903, color="#ffd700", label="75"),

    GraphicFeature(start=22798, end=23214, color="#ffd700", label="76"),

    GraphicFeature(start=23123, end=23522, color="#ffd700", label="77"),

    GraphicFeature(start=23444, end=23847, color="#ffd700", label="78"),

    GraphicFeature(start=23790, end=24169, color="#ffd700", label="79"),

    GraphicFeature(start=2182, end=2592, color="#ffd700", label="8"),

    GraphicFeature(start=24079, end=24467, color="#ffd700", label="80"),

    GraphicFeature(start=24392, end=24789, color="#ffd700", label="81"),

    GraphicFeature(start=24697, end=25076, color="#ffd700", label="82"),

    GraphicFeature(start=24979, end=25369, color="#ffd700", label="83"),

    GraphicFeature(start=25280, end=25673, color="#ffd700", label="84"),

    GraphicFeature(start=25602, end=25994, color="#ffd700", label="85"),

    GraphicFeature(start=25903, end=26315, color="#ffd700", label="86"),

    GraphicFeature(start=26198, end=26590, color="#ffd700", label="87"),

    GraphicFeature(start=26521, end=26913, color="#ffd700", label="88"),

    GraphicFeature(start=26836, end=27227, color="#ffd700", label="89"),

    GraphicFeature(start=2506, end=2904, color="#ffd700", label="9"),

    GraphicFeature(start=27142, end=27533, color="#ffd700", label="90"),

    GraphicFeature(start=27447, end=27854, color="#ffd700", label="91"),

    GraphicFeature(start=27785, end=28172, color="#ffd700", label="92"),

    GraphicFeature(start=28082, end=28464, color="#ffd700", label="93"),

    GraphicFeature(start=28395, end=28779, color="#ffd700", label="94"),

    GraphicFeature(start=28678, end=29063, color="#ffd700", label="95"),

    GraphicFeature(start=28986, end=29378, color="#ffd700", label="96"),

    GraphicFeature(start=29289, end=29693, color="#ffd700", label="97"),

    GraphicFeature(start=29487, end=29866, color="#ffd700", label="98"),

    GraphicFeature(start=29865, end=29869, color="#33ffee", label="dropout_of_concern"),

    GraphicFeature(start=241, end=241, color="#ffcccc", label="C241T"),
    GraphicFeature(start=1059, end=1059, color="#ffcccc", label="C1059T"),
    GraphicFeature(start=3037, end=3037, color="#ffcccc", label="C3037T"),
    GraphicFeature(start=4675, end=4675, color="#ffcccc", label="A4675G"),
    GraphicFeature(start=10319, end=10319, color="#ffcccc", label="C10319T"),
    GraphicFeature(start=10868, end=10868, color="#ffcccc", label="C10868T"),
    GraphicFeature(start=11832, end=11832, color="#ffcccc", label="C11832T"),
    GraphicFeature(start=14408, end=14408, color="#ffcccc", label="C14408T"),
    GraphicFeature(start=18424, end=18424, color="#ffcccc", label="A18424G"),
    GraphicFeature(start=19086, end=19086, color="#ffcccc", label="G19086T"),
    GraphicFeature(start=21304, end=21304, color="#ffcccc", label="C21304T"),
    GraphicFeature(start=22313, end=22313, color="#ffcccc", label="C22313T"),
    GraphicFeature(start=23403, end=23403, color="#ffcccc", label="A23403G"),
    GraphicFeature(start=25563, end=25563, color="#ffcccc", label="G25563T"),
    GraphicFeature(start=25907, end=25907, color="#ffcccc", label="G25907T"),
    GraphicFeature(start=27964, end=27964, color="#ffcccc", label="C27964T"),
    GraphicFeature(start=28472, end=28472, color="#ffcccc", label="C28472T"),
    GraphicFeature(start=28869, end=28869, color="#ffcccc", label="C28869T"),
    GraphicFeature(start=29200, end=29200, color="#ffcccc", label="C29200T"),
    GraphicFeature(start=29870, end=29870, color="#ffcccc", label="C29870A"),

    GraphicFeature(start=28465, end=28465, color="#cffccc", label="N:P67S"),
    GraphicFeature(start=28861, end=28861, color="#cffccc", label="N:P199L"),
    GraphicFeature(start=138, end=138, color="#cffccc", label="ORF14:Q46*"),
    GraphicFeature(start=1051, end=1051, color="#cffccc", label="ORF1a:T265I"),
    GraphicFeature(start=10312, end=10312, color="#cffccc", label="ORF1a:L3352F"),
    GraphicFeature(start=11824, end=11824, color="#cffccc", label="ORF1a:A3856V"),
    GraphicFeature(start=14412, end=14412, color="#cffccc", label="ORF1b:P314L"),
    GraphicFeature(start=18429, end=18429, color="#cffccc", label="ORF1b:N1653D"),
    GraphicFeature(start=19089, end=19089, color="#cffccc", label="ORF1b:K1873N"),
    GraphicFeature(start=21309, end=21309, color="#cffccc", label="ORF1b:R2613C"),
    GraphicFeature(start=25554, end=25554, color="#cffccc", label="ORF3a:Q57H"),
    GraphicFeature(start=25899, end=25899, color="#cffccc", label="ORF3a:G172V"),
    GraphicFeature(start=27956, end=27956, color="#cffccc", label="ORF8:S24L"),
    GraphicFeature(start=22306, end=22306, color="#cffccc", label="S:P251S"),
    GraphicFeature(start=23395, end=23395, color="#cffccc", label="S:D614G"),

    GraphicFeature(start=256, end=21545, strand=+1, color="blue", label="ORF1ab"),
    GraphicFeature(start=21553, end=25374, strand=+1, color="blue", label="S"),
    GraphicFeature(start=25383, end=26210, strand=+1, color="blue", label="ORF3a"),
    GraphicFeature(start=26235, end=26462, strand=+1, color="blue", label="E"),
    GraphicFeature(start=26513, end=27181, strand=+1, color="blue", label="M"),
    GraphicFeature(start=27192, end=27377, strand=+1, color="blue", label="ORF6"),
    GraphicFeature(start=27384, end=27749, strand=+1, color="blue", label="ORF7a"),
    GraphicFeature(start=27746, end=27877, strand=+1, color="blue", label="ORF7b"),
    GraphicFeature(start=27884, end=28249, strand=+1, color="blue", label="ORF8"),
    GraphicFeature(start=28264, end=29523, strand=+1, color="blue", label="N"),
    GraphicFeature(start=29548, end=29664, strand=+1, color="blue", label="ORF10")

]

record = GraphicRecord(sequence_length=30000, features=features)
ax, _ = record.plot(figure_width=150)
ax.figure.savefig(args.o)

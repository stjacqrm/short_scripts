#!/bin/bash

#----------
# Defaults
#----------

output_dir='sc2_outbreak_results'
quantitative='FALSE'
monroe_run=''
analysis_samples=''


#-------
# Usage
#-------

display_usage() {
  echo -e "\nUsage: $0 -o 'output_dir' -r 'monroe_run' -s 'analysis_samples'\n"
  echo -e "  -o  output directory."
  echo -e "      Default: sc2_outbreak_results"
  echo -e "  -r  path to monroe run."
  echo -e "      Default: ''"
  echo -e "  -s  samples to analyze in tsv format."
  echo -e "      Default: ''"
  echo -e "  -h  Displays this help message\n"
  echo -e "sc2_outbreak_analysis.sh"
  echo -e "This script is part of an SC2 outbreak analysis pipeline and produces "
  echo -e "quantitative and graphical reports.\n"
  exit
}


#---------
# Options
#---------

while getopts "o:r:s:h" opt; do
  case $opt in
    o) output_dir=${OPTARG%/};;
    r) monroe_run=$OPTARG;;
    s) analysis_samples=$OPTARG;;
    h) display_usage;;
   \?) #unrecognized option - show help
      echo -e \\n"Option -$OPTARG not allowed."
      display_usage;;
  esac
done


#---------------------
# Prep the assemblies
# directory and
# multi.fasta file
#---------------------

cp -r $monroe_run/assemblies .;
cp -r $monroe_run/monroe_s* .;
cp monroe* monroe_stats.csv;
cp $analysis_samples assemblies;
cd assemblies && ls -1 | grep -v -x -f $analysis_samples | xargs -d "\n" -P 0 rm -f;
cp /wgs_analysis/sc2_refs/VA-DCLS-0001_consensus.fasta .;
cp /wgs_analysis/sc2_refs/MN908947.3.fasta .;
mv MN908947.3.fasta MN908947.3.fasta1
sed '/^>/ s/ .*//' MN908947.3.fasta1 > MN908947.3.fasta;
cat *.fasta > multi.fasta && mv multi.fasta .. && cd ..;


#------------------
# Analyze SC2 data
#------------------

docker run --rm=True -u $(id -u):$(id -g) -v $(pwd):/data staphb/pangolin pangolin --version > pangolin_version;
docker run --rm=True -u $(id -u):$(id -g) -v $(pwd):/data staphb/pangolin pangolin multi.fasta;
docker run -it --rm -u 1000 --volume="${PWD}:/seq" nextstrain/nextclade:0.14.4 nextclade --version > nextclade_version;
docker run -it --rm -u 1000 --volume="${PWD}:/seq" nextstrain/nextclade:0.14.4 nextclade --input-fasta '/seq/multi.fasta' --output-csv '/seq/nextclade_result.csv';
staphb-wf monroe cluster_analysis assemblies;


#-------------------------
# Generate results report
#-------------------------

mkdir tmp
cp nextclade_result.csv tmp;
cp nextclade_version tmp
cp pangolin_version tmp
cp lineage_report.csv tmp;
cp monroe_stats.csv tmp;
cd tmp

sed 's/;/,/g' nextclade_result.csv > next.csv;
awk -F, '{print $1,$2}' next.csv > next2.csv;
cp next2.csv next2.csv.copy
awk 'BEGIN {FS=" "; OFS=","}; {print $2 "_" $3}' next2.csv > cleaned_clade_column
sed -i 1d next2.csv;
sed -i 1d cleaned_clade_column
sed -i 's/\ /,/g' next2.csv
sed -i 's/\t /,/g' next2.csv
sed -i 's/\ /,/g' cleaned_clade_column
sed -i 's/\t /,/g' cleaned_clade_column
cut -f1 -d ',' next2.csv > sample_names
paste -d ',' sample_names cleaned_clade_column > next3.csv
awk -F, '{print $1,$2}' lineage_report.csv > pango.csv;
sed -i 1d pango.csv;
sed -i 's/\ /,/g' pango.csv

paste -d ',' next3.csv pango.csv > results_report_1.csv
cut -d, -f3 --complement results_report_1.csv > results_report
{ echo 'Name,clade,lineage,pangolin_version,nextclade_version,monroe_status,collection_date'; cat results_report; } > results_report.csv

nextcladeversion=$(<nextclade_version)
pangoversion=$(<pangolin_version)
echo $nextcladeversion > ncv1.txt
sed -e "s/\r//g" ncv1.txt > ncv.txt
echo $pangoversion > pcv.txt
sed -i 's/pangolin //g' pcv.txt
sed -i 's/ //g' ncv.txt
sed -i 's/ /,/g' ncv.txt
sed -i 's/\t /,/g' ncv.txt
sed -i 's/ /,/g' pcv.txt
sed -i 's/\t /,/g' pcv.txt

for i in results_report.csv; do
  sed -i '1s/^/pangolin_version,/; 2,$s/^/\pangoversion,/' "$i";
  awk 'BEGIN{getline l < "pcv.txt"}/pangoversion/{gsub("pangoversion",l)}1' "$i" > tmp && mv tmp "$i";
  sed -i '1s/^/nextclade_version,/; 2,$s/^/\pextversion/' "$i";
  awk 'BEGIN{getline l < "ncv.txt"}/pextversion/{gsub("pextversion",l)}1' "$i" > tmp && mv tmp "$i";
  sed -i 's/0.14.43/0.14.4,3/g' "$i";
  sed -i '1s/^/monroe_status,/; 2,$s/^/\PASS,/' "$i";
  awk 'BEGIN {FS=","; OFS=","} {print $4,$5,$6,$2,$3,$1,$10}' "$i" > tmp && mv tmp "$i";
done

cp results_report.csv results_report

join -t ',' -1 1 -2 1 -o 0,2.7 <(sort -t ',' -k7,7 results_report) <(sort -t ',' -k1,1 monroe_stats.csv) > monroe_pass_2
cp monroe_pass_2 monroe_pass
cp monroe_pass ..
rm monroe_stats.csv
#awk -F, 'NR==FNR{a[$2]=$1;next}{print a[$1],$1;}' results_report monroe_pass_2 > results_report_maybe
#cp results_* ..

for f in *; do
  if [ ! "$(echo ${f} | grep -o '_report.csv')" ];
  then rm "${f}";
  fi;
done

mv * .. && cd ..
rm -r tmp

#-----------------
# Organize output
#-----------------

cd monroe_results && cp *.pdf .. && cd ..;
rm monroe_stats.csv
mkdir $output_dir && mv monroe_pass $output_dir && mv assemblies $output_dir && mv multi.fasta $output_dir && mv monroe* $output_dir && mv *.pdf $output_dir && mv pangolin_version $output_dir && mv nextclade_version $output_dir && mv lineage_report.csv  $output_dir && mv nextclade_result.csv $output_dir;
mkdir $output_dir/analysis_results
cd $output_dir && mv monroe_pass analysis_results && mv multi.fasta analysis_results && mv monroe_summary* analysis_results && mv *.pdf analysis_results && mv pangolin_version analysis_results && mv nextclade_version analysis_results && mv lineage_report.csv analysis_results && mv nextclade_result.csv analysis_results && cd ..;
mv results_report.csv $output_dir/analysis_results
cd $output_dir/analysis_results
mkdir nextclade_results && mv nextclade_result.csv nextclade_results && mv nextclade_version nextclade_results;
mkdir pangolin_results && mv pangolin_version pangolin_results && mv lineage_report.csv pangolin_results;

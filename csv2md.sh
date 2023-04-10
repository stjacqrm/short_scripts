#!/bin/bash -e



############################################################
# Help                                                     #
############################################################
Help()
{
   # Display Help
   echo "converts simple csv file to markdown table."
   echo
   echo "Syntax: csv2md.sh [-|t|i|o|h]"
   echo "options:"
   echo "h     Print this Help."
   echo "i     Input csv file."
   echo "o     Name of output md file."
   echo "c     Number of columns."
   exit
}

############################################################
############################################################
# Main program                                             #
############################################################
############################################################

# Get the options
while getopts ":i:o:c:h" option; do
   case $option in
      i) input=$OPTARG;;
      o) output=$OPTARG;;
      c) columns=$OPTARG;;
      h) Help;;
     \?) #unrecognized option - show help
        echo -e \\n"Option -$OPTARG not allowed."
   esac
done

echo "Adding row under header"

HEADER1=''
HEADER2=''

for p in $(seq 1 $columns); do
  HEADER1="$HEADER1 $p |"
  HEADER2="$HEADER2 :---: ,"
done

awk -v s="$HEADER2" 'NR == 2 { print s} { print }' $input > intermediate_file

echo "Formatting Table"

sed -e 's/^/|\ /g' -e 's/,/\ |\ /g' -e 's/$/\ |/g' intermediate_file > intermediate_file2
sed '2 s/.$//' intermediate_file2 > $output


echo "Removing intermediate files"
rm -rf intermediate_file intermediate_file2

echo "Done, completed converstion of $input to $output."

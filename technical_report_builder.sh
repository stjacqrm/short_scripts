#!/bin/bash -e

# Help                                                     
Help()
{
   # Display Help
   echo "converts markdown file to pdf for technical reports"
   echo
   echo "Syntax: technical_report_builder.sh [-|t|i|o|h]"
   echo "options:"
   echo "h     Print this Help."
   echo "i     Input markdown file."
   echo "o     Name of output pdf file."
   echo "p     Path to pandoc template."
   exit
}

# Get the options
while getopts ":i:o:p:h" option; do
   case $option in
      i) input=$OPTARG;;
      o) output=$OPTARG;;
      p) path=$OPTARG;;
      h) Help;;
     \?) #unrecognized option - show help
        echo -e \\n"Option -$OPTARG not allowed."
   esac
done

echo "Converting $input to $output"
# Run Pandoc
pandoc $input -o $output --from markdown+yaml_metadata_block+raw_html --template $path --table-of-contents --toc-depth 6 --number-sections --top-level-division=chapter --highlight-style breezedark --resource-path=.:src

echo "PDF generation complete"

#!/bin/bash

if [ -z $1 ]; then
	echo -e "Please input the source directory as the first argument. \n ./PackageScript.sh <source directory> <path/BOM.txt>"
	exit 0
fi

if [ -z $2 ]; then
	echo -e "Please input the <path>/BOM.txt as the second argument. \n ./PackageScript.sh <source directory> <path/BOM.txt>"
	exit 0
fi	

cd $1

ls -lrt | awk 'NR!= 1 {print $9}' > filenames.txt
sed -i '$ d' filenames.txt
difference_from_bom=$(fgrep -vf filenames.txt $2 | wc -l)
if [ $difference_from_bom -gt 0 ]; then
	echo "Below files are missing in the packaging area...EXITING..."
	fgrep -vf filenames.txt $2
	exit 0 
fi

extra_files=$(fgrep -vf $2 filenames.txt | wc -l)
if [ $extra_files -gt 0 ]; then
	echo -e "WARNING!!!!! \n Please find below additional files found in packaging area \n Please add them in the BOM.txt and rerun the packaging script for them to be packaged \n Continuing to package with current BOM list"
	echo -e "ADDITIONAL FILES \n**********************"
	fgrep -vf $2 filenames.txt
	echo -e "************************ \n \n "
fi
sed -i 's/\r//g' $2
tar -cvf ArithmeticOperator.tar $(cat $2) 
gzip ArithmeticOperator.tar

rm filenames.txt 

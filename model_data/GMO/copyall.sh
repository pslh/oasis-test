#! /bin/bash
for file in ls *.csv
do  
	if [ -f in/$file ]
	then   
		cp in/$file .
	fi
done

# mapreduce-hdp

Prereq:
Data files need to be uploaded to hfs.
hadoop fs -mkdir input
hadoop fs -put [datafile] input
Run in a unix environment and make sure EOL is set to LF not CRLF.
Shebang runs python in env specifically. Change shebang for other python versions.
chmod might be needed for permissions to run the files.
chmod a+rx *.sh 
chmod a+rx *.py

Test with bash pip:
cat data.csv | ./mapper1.py | sort | ./reducer1.py | ./mapper2.py | sort | ./reducer2.py 

Run script
./hadoopscript.sh
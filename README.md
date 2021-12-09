# mapreduce-hdp

## Prereq:

- Run in a unix environment and make sure EOL is set to LF not CRLF.
- Data files need to be uploaded to hfs.
    - hadoop fs -mkdir input
    - hadoop fs -put [datafile] input
- Shebang runs python in env. Change shebang for other python alias.
- chmod might be needed for permissions to run the files.
    - chmod a+rx *.sh 
    - chmod a+rx *.py


## Run

Test with bash:
cat data.csv | ./mapper1.py | sort | ./reducer1.py | ./mapper2.py | sort | ./reducer2.py 

Run script
./hadoopscript.sh

![alt text](https://raw.githubusercontent.com/thanhdip/mapreduce-hdp/main/screenshot/hdp.png)

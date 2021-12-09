# mapreduce-hdp

Prereq:
Run in a unix environment and make sure EOL is set to LF not CRLF.
Shebang runs python3 in env specifically. Change shebang if no python3 alias.

Test with bash pip:
cat data.csv | ./mapper1.py | sort | ./reducer1.py | ./mapper2.py | sort | ./reducer2.py 

chmod a+rx hadoopscript.sh 
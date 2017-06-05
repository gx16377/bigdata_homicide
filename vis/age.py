import csv
import os,sys

file=open('../PerMonth/PerpetratorAge.csv',"r")
reader=csv.reader(file)
data={}

for line in reader:
	data.setdefault(line[0],0);
	data[line[0]]+=int(line[4]);

file.close()

print("dataMap.age={")
for k in data.keys():
        print ("\t"+str(k)+":"+str(data[k])+",")
print("}")

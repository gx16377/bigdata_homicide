import csv
import os,sys

file=open('../PerMonth/State.csv',"r")
reader=csv.reader(file)
data={}

for line in reader:
	data.setdefault(line[0],{});
	data[line[0]].setdefault(line[2],int(line[4]))
	data[line[0]][line[2]]+=int(line[4]);

file.close()

print("dataMap.States={")
for k in data.keys():
        print ("\t'"+str(k)+"':[")
        for kk in data[k].keys():
                print("\t\t"+str(data[k][kk])+",")
        print("\t],")
print("}")

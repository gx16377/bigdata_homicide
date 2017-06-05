import csv
import os,sys

file=open('../PerMonth/State.csv',"r")
reader=csv.reader(file)
data={}

for line in reader:
	data.setdefault(line[2],{});
	data[line[2]].setdefault(line[0],int(line[4]))
	data[line[2]][line[0]]+=int(line[4]);

file.close()

print("dataMap.OV={")
for k in data.keys():
        print ("\t"+str(k)+":[")
        for kk in data[k].keys():
                print("\t\t{name: '"+str(kk)+"', value: "+str(data[k][kk])+"},")
        print("\t],")
print("}")

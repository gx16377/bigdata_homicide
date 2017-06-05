import csv
import os,sys

file=open('../to刘神/victimsex_year_state.csv',"r",encoding="utf-8")
reader=csv.reader(file)
dataMale={}
dataFemale={}

for line in reader:
	if line[0][0]=='\ufeff':
		line[0]=line[0][1:]
	dataMale.setdefault(line[1],{})
	dataMale[line[1]].setdefault(int(line[0]),0)

	dataFemale.setdefault(line[1],{})
	dataFemale[line[1]].setdefault(int(line[0]),0)
	
	if line[2]=="Male":
		dataMale[line[1]][int(line[0])]+=int(line[3]);
	
	if line[2]=="Female":
		dataFemale[line[1]][int(line[0])]+=int(line[3]);

file.close()


print("dataMap.StatesVMale={")
for k in dataMale.keys():
        for i in range(1980,2015,1):
                dataMale[k].setdefault(i,0)
        print ("\t'"+str(k)+"':[")
        temp=sorted(dataMale[k].items(),key=lambda e:e[0])
        for i in temp:
                print ("\t\t"+str(i[1])+',');
        print("\t],")
print("};")


print("dataMap.StatesVFemale={")
for k in dataFemale.keys():
        for i in range(1980,2015,1):
                dataFemale[k].setdefault(i,0)
        print ("\t'"+str(k)+"':[")
        temp=sorted(dataFemale[k].items(),key=lambda e:e[0])
        for i in temp:
                print ("\t\t"+str(i[1])+',');
        print("\t],")
print("};")

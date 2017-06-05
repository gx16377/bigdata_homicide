import csv
import os,sys
files=['State', 'Relationship', 'Weapon', 'PerpetratorAge', 'PerpetratorSex', 'VictimAge', 'VictimSex']

for file in files:
	print(file)
	f=open('PerMonth/'+file+'.csv', "r",encoding="utf-8")
	rd=csv.reader(f)
	dic={}
	label=[]
	for l in rd:
		if l[0][0]=='\ufeff':
			l[0]=l[0][1:]
		
		dic[(l[1],int(l[2])*12+int(l[3]))]=int(l[4])
		if l[1] not in label:
			label.append(l[1])
		
	f.close()
	for l in label:
		#f1=open('NNdata/'+file+'_'+l+'.csv',"w",encoding="utf-8")
		sum=0
		error=set()
		for y in range(1980,2015):
			for m in range(1,13):
				zero_num=0
				for i in range(5):
					if dic.get((l,y*12+(m-i)),0)<2 and (y>1980 or m>5):
						zero_num+=1
				if zero_num==5:
					error.add(y)
				sum+=dic.get((l,y*12+m),0)
		if sum>35*12*10 and len(error)>0:
			print(l)
			print(error)
		#f1.close()
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
		if (l[0],l[1]) not in label:
			label.append((l[0],l[1]))
		
	f.close()
	f1=open('NNdata/'+file+'.csv',"w",encoding="utf-8")

	for y in range(1980,2015):
		for m in range(1,13):
			for l in label:
				if file=='State' and l[1] in ['0','8','9','17','31','49']:
					continue
				x=[l[1],str(y),str(m)]
				for i in range(1,6):
					x.append(str(dic.get((l[1],y*12+(m-i)),0)))
				for i in range(1,6):
					x.append(str(dic.get((l[1],(y-i)*12+m),0)))

				f1.write(str(dic.get((l[1],y*12+m),0))+','+','.join(x)+'\n')

	f1.close()
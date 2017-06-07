import csv
import os,sys
files=['State', 'Relationship', 'Weapon', 'PerpetratorSex', 'VictimSex']
res=['state_res','relationship_res','weapon_res','PSex_res','VSex_res']
for fi in range(len(files)):
	file=files[fi]
	print(file)
	f=open('PerMonth/'+file+'.csv', "r",encoding="utf-8")
	rd=csv.reader(f)
	label={}
	for l in rd:
		if l[0][0]=='\ufeff':
			l[0]=l[0][1:]
		
		if l[1] not in label:
			label[l[1]]=l[0]
		
	f.close()
	f1=open('res/'+res[fi]+'.csv',"r",encoding="utf-8")
	rd1=csv.reader(f1)
	f2=open('res1/'+res[fi]+'.csv',"w",encoding="utf-8")
	
	for l in rd1:
		l[0]=label.get(l[0],'')
		f2.write(','.join(l)+'\n')
	f1.close()
	f2.close()
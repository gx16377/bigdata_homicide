import csv
import os,sys

for i in range(1981,2015):
	print ("				{\n					title: {\n							text: '美国谋杀案统计"+str(i)+"'\n					},\n					series: [\n						{	\n							data:dataMap.OV["+str(i)+"]\n						}\n					]\n				},");

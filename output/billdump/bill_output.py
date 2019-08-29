import csv 
from os import listdir
from os.path import isfile, join
import statistics 
path = 'output/billdump/'
files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith( ".csv" )]
fw = open(path+'bill_sum.csv','w')
header='Model Name,Tariff,Total Bill,Standard Deviation'
fw.write(header)
for file in sorted(files) : 
	if 'bill_sum.csv' not in file : 
		bill_sum = 0
		bill_list = []
		bill_stdev = 0
		with open(path+file, newline='') as csvfile : 
			fr = csv.reader(csvfile, delimiter=',', quotechar='|')
			next(fr)
			for row in fr : 
				if 'meter_name'==row[0] :
					continue
				else : 
					bill_list.append(float(row[1]))
		bill_sum=str(round(sum(bill_list),1))
		if len(bill_list)>1 : 
			bill_stdev=str(round(statistics.stdev(bill_list),2))		
		else : 
			bill_stdev='N/A'
		if 'fixed' in file and 'IEEE_13' in file : 
			fw.write('\nIEEE 13,'+'fixed,'+bill_sum+','+bill_stdev)
		if 'fixed' in file and 'IEEE_4' in file : 
			fw.write('\nIEEE 4,'+'fixed,'+bill_sum+','+bill_stdev)
		if 'tou' in file or 'TOU' in file :
			if 'IEEE_13' in file : 
				fw.write('\nIEEE 13,'+'TOU,'+bill_sum+','+bill_stdev)
			elif 'IEEE_4' in file : 
				fw.write('\nIEEE 4,'+'TOU,'+bill_sum+','+bill_stdev)
	else : 
		continue
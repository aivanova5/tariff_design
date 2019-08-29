import csv 
import os 
import gridlabd 

path="config/"

if os.path.exists(path+"config.glm"):
	os.remove(path+"config.glm")

with open(path+'simulation_configuration.csv', newline='') as config_file : 
	fc = csv.reader(config_file, delimiter=',', quotechar='|')
	fw = open(path+'config.glm', 'w')
	fw.write('// Generated config.glm based on config/simulation_configuration.csv')
	for line in fc : 
		if 'SIMULATION START TIME' in line[0] :
			fw.write('\n#define STARTTIME=' + str(line[1]).strip(' '))
			year = line[1].strip(' ')[0:4]
		if 'SIMULATION STOP TIME' in line[0] :
			fw.write('\n#define STOPTIME=' + str(line[1]).strip(' '))
		if 'TIMEZONE' in line[0] :
			fw.write('\n#define TIMEZONE=' + str(line[1]).strip(' '))
		if 'WEATHER FILE' in line[0] : 
			fw.write('\n#define WEATHER=' + str(line[1]).strip(' '))
		if 'TARIFF'==line[0] :
			fw.write('\n#define TARIFF=' + str(line[1]).strip(' ')+'.tariff')
			tariff_type = str(line[1]).strip(' ')
		if 'BILL DUMP TIME' in line[0] : 
			fw.write('\n#define BILLDUMPTIME=' + str(line[1]).strip(' '))
		if 'FIXED PRICE WINTER' in line[0] : 
			fixed_winter=line[1].strip(' ')
		if 'FIXED PRICE SUMMER' in line[0] : 
			fixed_summer=line[1].strip(' ')
		if 'TOU OFF-PEAK PRICE WINTER' in line[0] : 
			TOU_winter=float(line[1].strip(' '))
		if 'TOU OFF-PEAK PRICE SUMMER' in line[0] : 
			TOU_summer=float(line[1].strip(' '))
		if 'TOU MULTIPLIER' in line[0] : 
			TOU_multiplier=float(line[1].strip(' '))
		if 'MODEL NAME' in line[0] : 
			model_name = line[1].strip(" ")
			if model_name=='ieee4' or model_name=='ieee13' :
				print("RUNNING MODEL : " + model_name)
			else :
				print("ERROR: model name is invalid - Choose either ieee13 or ieee4")
fw.close()
if tariff_type=='fixed' :
	if os.path.exists("input/tariff/fixed.tariff"):
		os.remove("input/tariff/fixed.tariff")
	fw_fixed = open("input/tariff/fixed.tariff",'w')
	fw_fixed.write(year+'-01-01 00:00:00,' + fixed_winter)
	fw_fixed.write('\n'+year+'-05-01 00:00:00,' + fixed_summer)
	fw_fixed.write('\n'+year+'-11-01 00:00:00,' + fixed_winter)
	fw_fixed.close()
elif tariff_type=='TOU' or tariff_type=='tou': 
	if os.path.exists("input/tariff/tou.tariff"):
		os.remove("input/tariff/tou.tariff")
	fw_tou = open("input/tariff/tou.tariff",'w')
	fw_tou.write(year+'-12-31 22:00:00,' + str(TOU_winter))
	fw_tou.write('\n+16h,' + str(TOU_winter*TOU_multiplier))
	fw_tou.write('\n+6h,' + str(TOU_winter))
	fw_tou.write('\n'+year+'-04-30 22:00:00,' + str(TOU_summer))
	fw_tou.write('\n+16h,' + str(TOU_summer*TOU_multiplier))
	fw_tou.write('\n+6h,' + str(TOU_summer))
	fw_tou.write('\n'+year+'-10-31 22:00:00,' + str(TOU_winter))
	fw_tou.write('\n+16h,' + str(TOU_winter*TOU_multiplier))
	fw_tou.write('\n+6h,' + str(TOU_winter))
	fw_tou.close()
# # RUNNING GRIDLABD 
gridlabd.command(model_name+'/'+model_name+'.glm')
gridlabd.start('wait')

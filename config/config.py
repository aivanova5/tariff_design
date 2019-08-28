import csv 
import os 

path="config/"

if os.path.exists(path+"config.glm"):
    os.remove(path+'config.glm')

with open(path+'simulation_configuration.csv', newline='') as config_file : 
	fc = csv.reader(config_file, delimiter=',', quotechar='|')
	fw = open(path+'config.glm', 'w')
	fw.write('// Generated config.glm based on config/simulation_configuration.csv')
	for line in fc : 
		if 'SIMULATION START TIME' in line[0] :
			fw.write('\n#define STARTTIME=' + str(line[1]).strip(' '))
		if 'SIMULATION STOP TIME' in line[0] :
			fw.write('\n#define STOPTIME=' + str(line[1]).strip(' '))
		if 'TIMEZONE' in line[0] :
			fw.write('\n#define TIMEZONE=' + str(line[1]).strip(' '))
		if 'TARIFF' in line[0] :
			fw.write('\n#define TARIFF=' + str(line[1]).strip(' ')+'.tariff')



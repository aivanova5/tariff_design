gridlabd --version 

if [ ! -d "output/" ] 
then
    mkdir output
fi
if [ ! -d "output/billdump" ] 
then
    mkdir output/billdump
fi
if [ ! -d "output/powerdump" ] 
then
    mkdir output/powerdump
fi
if [ ! -d "output/voltdump" ] 
then
    mkdir output/voltdump
fi
if [ ! -d "input/tariff" ] 
then
    mkdir output/tariff
fi

python3 main.py
python3 output/billdump/bill_output.py

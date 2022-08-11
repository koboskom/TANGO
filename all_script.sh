#!/usr/bin/bash
cd /mnt/c/Users/marek/Documents/projekt_mgr/data/
echo "cuting files to shots"
python cut.py
cd /home/kali/mgr/
echo "script indicators"
./mitsuScript.sh /mnt/c/Users/marek/Documents/projekt_mgr/data/shots/ ./mitsuLinuxMultithread
cd mitsu_metrics*
cp ../mitsu_csv.py .
echo "copy mean values of indicators"
python mitsu_csv.py
cp all_res.csv  /mnt/c/Users/marek/Documents/projekt_mgr/data/csv/
echo "Done"

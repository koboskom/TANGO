#!/usr/bin/python

import csv
from re import T
import pandas as pd
import os

# python script for mitsu data edition and automation process

path = os.getcwd()
csv_files = []
for file in os.listdir():
    if file.endswith(".mp4.csv"):
        filename = file.replace("(","").replace(")","").replace("-","_")
        os.rename(file, filename)
        csv_files.append(filename)
        
big_frame = pd.DataFrame(columns= ['File:', 'Blockiness:', 'SA:', 'Blockloss:', 'Blur:', 'TA:', 'Exposure(bri):',
       'Contrast:', 'Noise:', 'Slice:', 'Flickering:'])
i = 0
for file in csv_files:
    i = i+1

    cmd = 'cat {0} | tr -s "\\t" "," > {1}'.format(file, "copy" + file)
    os.system(cmd)
    df = pd.DataFrame()
    df = pd.read_csv('{}'.format("copy" + file))
    df.columns = df.columns.str.replace(' ', '')
    df.drop(['Frame:', 'Letterbox:', 'Pillarbox:', 'Blackout:', 'Freezing:', 'Interlace:'], axis=1, inplace=True)

    df2 = df.mean(axis=0)
    df2["File:"] = file.replace(".csv","").replace("results-","")
    big_frame = big_frame.append(df2, ignore_index=True)

# remove file copies
cmd2 = 'rm -rf copy*'
os.system(cmd2)
big_frame.to_csv("all_res.csv",index=False)
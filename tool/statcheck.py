#!/usr/bin/env python3

#modules
import os
import os.path as path
import csv

#list of train pnml files
filelist=[]
for root, dirs, files in os.walk("src"): # temporary link to src folder
    if not dirs:
        if "REVERSING" not in root:
            if "OTHER" not in root:
                for fname in files:
                    filelist.append(path.join(root,fname))

# extracting values from text
def extract(text):
    text = str(text)
    newtext = text.split(":")[-1].split(";")[0].strip()
    return newtext

# reading data per file
csv_data = [] # csv data collector

for file in filelist:
    with open(file,"r") as f:
        flines = f.readlines()
    startnum = 0
    endnum = 0
    for linenum in range(len(flines)): # find the item block in file
        line = flines[linenum]
        if "item" in line:
            startnum = linenum
        if "}" in line:
            if linenum > startnum:
                endnum = linenum
                continue

    datalist = [file] # list of data of this train, outputted as a line in a csv
    for text in flines[startnum:endnum]: # extracting individual data attributes
        atr = text.split(":")[0].strip()
        if  atr == "name":
            name = extract(text)
            datalist.append(name)
        if atr == "introduction_date":
            introduction_date = extract(text)
            datalist.append(introduction_date)
        if atr == "model_life":
            model_life = extract(text)
            datalist.append(model_life)
        if atr == "vehicle_life":
            veheicle_life = extract(text)
            datalist.append(veheicle_life)
        if atr == "reliability_decay":
            reliability_decay = extract(text)
            datalist.append(reliability_decay)

        if atr == "cargo_capacity":
            cargo_capacity = extract(text)
            datalist.append(cargo_capacity)
        if atr == "loading_speed":
            loading_speed = extract(text)
            datalist.append(loading_speed)
        if atr == "cost_factor":
            cost_factor = extract(text)
            datalist.append(cost_factor)
        if atr == "running_cost_factor":
            running_cost_factor = extract(text)
            datalist.append(running_cost_factor)

        if atr == "speed":
            speed = extract(text)
            datalist.append(speed)
        if atr == "track_type":
            track_type = extract(text)
            datalist.append(track_type)
        if atr == "power":
            power = extract(text)
            datalist.append(power)
        if atr == "weight":
            weight = extract(text)
            datalist.append(weight)
    csv_data.append(datalist)

headerrow = ["file","name","introduction_date","model_life","veheicle_life","reliability_decay","cargo_capacity","loading_speed","cost_factor","running_cost_factor","speed","track_type","power","weight"]

with open("traindata.csv","w") as cfile:
    w = csv.writer(cfile,delimiter=",")
    w.writerow(headerrow)
    for data in csv_data:
        w.writerow(data[0:14])

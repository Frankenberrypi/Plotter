# -*- coding: utf-8 -*-
"""
Created on Sat Nov 08 20:09:24 2014

@author: Jeff Beckman
"""
import csv
import datetime 
import time

ifile  = open('test.csv', "rb")
reader = csv.reader(ifile)
ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

dFile = open('datafile.csv','wb')
dataWriter = csv.writer(dFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

temp = 75.2
hum=54.1

for row in reader:
    print row
    writer.writerow(row)
    timeNow = datetime.datetime.now()
    dataRow = [str(timeNow), str(temp), str(hum)]
    time.sleep(5)
    dataWriter.writerow(dataRow)

ifile.close()
ofile.close()
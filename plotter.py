#!/usr/bin/python

import subprocess
import re
import time
import datetime

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

import csv

# Start some empty lists
timeBase = []
timeL = []
tempL = []
humiL = []

# Continuously append data
while(True):
  # Run the DHT program to get the humidity and temperature readings

  output = subprocess.check_output(["./Adafruit_DHT", "2302", "4"]);
  print output
  matches = re.search("Temp =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  tempC = float(matches.group(1))
  temp = tempC * 1.8 + 32
  
  # search for humidity printout
  matches = re.search("Hum =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  humidity = float(matches.group(1))

  print "Temperature: %.1f F" % temp
  print "Humidity:    %.1f %%" % humidity
  


  # Stick it in some lists
  timeNow = datetime.datetime.now()
  timeBase.append(timeNow)
  timeL = matplotlib.dates.date2num(timeBase)
  tempL.append(temp)
  humiL.append(humidity)

  # make a row
  dataRow = [timeNow, temp, humidity]

  # Open a .csv file
  with open('data.csv', 'wb') as dataFile:
      dataWriter = csv.writer(dataFile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
      dataWriter.writerow(dataRow)
      
  # Temp plot
  plt.plot(timeL,tempL)
  plt.ylim([60,85])
  plt.ylabel('Temperature, F')
  plt.xlabel('Some sort of time')
  plt.savefig('temperature.png', bbox_inches='tight')
  plt.clf()

  # Humidity plot
  plt.plot(timeL,humiL)
  plt.ylim([20,70])
  plt.ylabel('Relative Humidity, %')
  plt.xlabel('Some sort of time')
  plt.savefig('humidity.png', bbox_inches='tight')
  plt.clf()

  # Show me the data
#  print timeL
#  print tempL
#  print humiL

  # Wait 30 seconds before continuing
  print "Wrote a row to output"
  time.sleep(30)

#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

# Start some empty lists
timeBase = []
timeL = []
tempL = []
humiL = []

# Continuously append data
while(True):
  # Run the DHT program to get the humidity and temperature readings!

  output = subprocess.check_output(["./Adafruit_DHT", "2302", "4"]);
  print output
  matches = re.search("Temp =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  temp = float(matches.group(1))
  
  # search for humidity printout
  matches = re.search("Hum =\s+([0-9.]+)", output)
  if (not matches):
	time.sleep(3)
	continue
  humidity = float(matches.group(1))

  print "Temperature: %.1f C" % temp
  print "Humidity:    %.1f %%" % humidity

  # Stick it in some lists
  timeNow = datetime.datetime.now()
  timeBase.append(timeNow)
  timeL = matplotlib.dates.date2num(timeBase)
  tempL.append(temp)
  humiL.append(humidity)

  # Temp plot
  plt.plot(timeL,tempL)
  plt.ylabel('Temperature, C')
  plt.xlabel('Some sort of time')
  plt.savefig('temperature.png', bbox_inches='tight')
  plt.clf()

  # Humidity plot
  plt.plot(timeL,humiL)
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

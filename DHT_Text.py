#!/usr/bin/python

import subprocess
import re
import sys
import time
import datetime

# Open output files
outFile = "testOut.dat"
outDebug = "outDebug.dat"

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


  # Output data to file
#  fOut = open ( outFile, "a" )
#  values = [str(datetime.datetime.now()), str(temp),str( humidity)]
#  valuesStr = str(values)
#  fOut.write( valuesStr )
#  fOut.write( "\n" )
#  fOut.close()


  # Wait 30 seconds before continuing
  print "Wrote a row to output"
  time.sleep(30)

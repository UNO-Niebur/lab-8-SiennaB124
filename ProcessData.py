#ProcessData.py
#Name: Sienna Bonner
#Date: 3/26/26
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum)
    majorYear = makeMajorYear(major, year)

    output = last + "," + first + "," + student_id + "," + majorYear + "\n"
    outFile.write(output)
   

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

  

def makeID(first, last, idNum):
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "x"

  id = first[0] + last + idNum[idLen - 3: ]
  
  return id

def makeMajorYear(major, year):
  major_code = major[:3].upper()

  if year == "Freshman":
    year_code = "FR" 
  elif year == "Sophomore":
    year_code = "SO"
  elif year == "Junior":
    year_code = "JR"
  elif year == "Senior":
    year_code = "SR"
  else: 
    year_code = "UN"

  return major_code + "-" + year_code

if __name__ == '__main__': 
  main()

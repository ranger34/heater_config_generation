#!/usr/bin/env python
# -*- coding = utf-8 -*-

'''
	Fan Gu, 2015.12, python 2.7
	This python script is aimed at processing the generated combinations
	to strings that used to replace lines in the model file.
'''

import re
import os
import random

class file_process:
	# step1: choose lines that has the following strs
    def configFilter(self):
        str1 = "(-2, 2), (-2, 2), (-2, 2), (-2, 2)"
        str2 = "(2, 2), (2, 2), (2, 2), (2, 2)"
        str3 = "(-2, -2), (-2, -2), (-2, -2), (-2, -2)"
        str4 = "(0, 0), (0, 0), (0, 0), (0, 0)"
        str5 = "(2, -2), (2, -2), (2, -2), (2, -2)"
        
        with open("refer.txt", 'r') as fin1, open("step1.txt", 'a') as fout1:
            for line in fin1.readlines():
                if str1 in line or str2 in line or str3 in line or str4 in line or str5 in line:
                    fout1.write(line)

	# step2: extract the line number 
    def lineNumChoose(self):
        n = -1
        with open("step1.txt", 'r') as fin2, open("step2.txt", 'a') as fout2:
            for line in fin2.readlines():
				n += 1
				if n % 3 == 0:
					chooseline = line.split(":")[0]
					fout2.write(chooseline + '\n')

	# choose lines according to lines of step2
    def configExtract(self):
		with open("step2.txt", 'r') as fin3, open("remain.txt", 'r') as fin4, open("part2.txt", 'a') as fout3:
			for remainLine in fin4.readlines():
				remainLineBack = remainLine
				remainLineNum = remainLine.split(":")[0]

				fin3.seek(0)
				for chooseLine in fin3.readlines():
					line = chooseLine.strip()

					if line == remainLineNum:
						fout3.write(remainLineBack)

		os.remove("step1.txt")
		os.remove("step2.txt")

	# get the remain part that excluding part1 and part2
    def remainUpdate(self):
		lineArray = []
		with open("remain_new.txt", 'a') as fout4, open("remain.txt", 'r') as fin5, open("part2.txt", 'r') as fin6:
			for remainLine in fin5.readlines():
				lineArray.append(remainLine.replace("\n", ""))

			for line in lineArray:
				fin6.seek(0)
				for replaceLine in fin6.readlines():
					replaceLine = replaceLine.strip()
					if line == replaceLine:
						lineArray.remove(line)
				fout4.write(line + '\n')

	# combine 3 parts of data
    def combComplete(self):
		with open("remain_new.txt", 'r') as fin7, open("part1.txt", 'r') as fin8, open("part2.txt", 'r') as fin9, open("sample.txt", 'a') as fout5:
			for line1 in fin8.readlines():
				fout5.write(line1.split(":")[1])

			for line2 in fin9.readlines():
				fout5.write(line2.split(":")[1])

			lineArray = []
			for line3 in fin7.readlines():
				lineArray.append(line3.split(":")[1])
			randStrArray = random.sample(lineArray, 121)
		
			for line4 in randStrArray:
				fout5.write(line4)

	# generate the data that used to model checking
    def sampleGen(self):
		with open("sample.txt", 'r') as fin10, open("powerSample.txt", 'a') as fout6, open("tempLowerSample.txt", 'a') as fout7, open("tempUpperSample.txt", 'a') as fout8:
			for line in fin10.readlines():
				p_str = "/*power modify here*/{" + (line.split(",")[0])[1:] + "," + line.split(",")[1] + "}, {"\
						+ (line.split(",")[4])[1:] + "," + line.split(",")[5] + "}, {"\
						+ (line.split(",")[8])[1:] + "," + line.split(",")[9] + "}, {"\
						+ (line.split(",")[12])[1:] + "," + line.split(",")[13] + "}, {"\
						+ (line.split(",")[16])[1:] + "," + line.split(",")[17] + "}/*power end modify*/"
				tl_str = "/*lowTemp modify here*/double temp_lower[rid_t] = {" + (line.split(",")[2])[1:] + ".0,"\
						+ line.split(",")[6] + ".0," + line.split(",")[10] + ".0,"\
						+ line.split(",")[14] + ".0," + line.split(",")[18] + ".0};/*lowTemp end modify*/"
				tu_str = "/*upTemp modify here*/double temp_upper[rid_t] = {" + (line.split(",")[3])[1:] + ".0,"\
						+ line.split(",")[7] + ".0," + line.split(",")[11] + ".0,"\
						+ line.split(",")[15] + ".0, " + line.split(",")[19].strip() + ".0};/*upTemp end modify*/"

				fout6.write(p_str + '\n')
				fout7.write(tl_str + '\n')
				fout8.write(tu_str + '\n')


if __name__ == "__main__":
    fp = file_process()
#	fp.configFilter()
#    fp.lineNumChoose()
#    fp.configExtract()
#    fp.remainUpdate()
#    fp.combComplete()
#    fp.sampleGen()

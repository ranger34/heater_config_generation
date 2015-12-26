#!/usr/bin/env python
# -*- coding = utf - 8 -*-

import re
import os
import random

class file_process:
    def configFilter(self):
        fin1 = open("refer.txt", 'r')
        fout1 = open("step1.txt", 'a')
        
        str1 = "(-2, 2), (-2, 2), (-2, 2), (-2, 2)"
        str2 = "(2, 2), (2, 2), (2, 2), (2, 2)"
        str3 = "(-2, -2), (-2, -2), (-2, -2), (-2, -2)"
        str4 = "(0, 0), (0, 0), (0, 0), (0, 0)"
        str5 = "(2, -2), (2, -2), (2, -2), (2, -2)"

        while True:
            line = fin1.readline()
            if line:
                if str1 in line or str2 in line or str3 in line or str4 in line or str5 in line:
                    fout1.write(line)
            else:
                break

        fin1.close()
        fout1.close()

    def lineNumChoose(self):
        fin2 = open("step1.txt", 'r')
        fout2 = open("step2.txt", 'a')

        n = -1
        while True:
            n += 1
            line = fin2.readline()
            if line:
                if n % 5 == 0:
                    chooseline = line.split(",")[0]
                    fout2.write(chooseline + '\n')
            else:
                break

        fin2.close()
        fout2.close()

    def configExtract(self):
        fin3 = open("step2.txt", 'r')
        fin4 = open("remain.txt", 'r')
        fout3 = open("part2.txt", 'a')

        for remainLine in fin4.readlines():
            remainLineBack = remainLine
            remainLineNum = remainLine.split(":")[0]

            fin3.seek(0)
            for chooseLine in fin3.readlines():
                line = chooseLine.strip()

                if line == remainLineNum:
                    fout3.write(remainLineBack)

        fin3.close()
        fin4.close()
        fout3.close()
        
        os.remove("step1.txt")
        os.remove("step2.txt")

    def remainUpdate(self):
        fout4 = open("remain_new.txt", 'a')
        fin5 = open("remain.txt", 'r')
        fin6 = open("part2.txt", 'r')

        lineArray = []
        for remainLine in fin5.readlines():
			lineArray.append(remainLine.replace("\n", ""))

        for line in lineArray:
            fin6.seek(0)
            for replaceLine in fin6.readlines():
                replaceLine = replaceLine.strip()
                if line == replaceLine:
					lineArray.remove(line)
            fout4.write(line + '\n')

        fout4.close()
        fin5.close()
        fin6.close()

    def combComplete(self):
		fin7 = open("remain_new.txt", 'r')
		fin8 = open("part1.txt", 'r')
		fin9 = open("part2.txt", 'r')
		fout5 = open("sample.txt", 'a')

		for line1 in fin8.readlines():
			fout5.write(line1.split(":")[1])

		for line2 in fin9.readlines():
			fout5.write(line2.split(":")[1])

		lineArray = []
		for line3 in fin7.readlines():
			lineArray.append(line3.split(":")[1])
		randStrArray = random.sample(lineArray, 62)
		
		for line4 in randStrArray:
			fout5.write(line4)

		fin7.close()
		fin8.close()
		fin9.close()
		fout5.close()

		#os.remove("part1.txt")
		#os.remove("part2.txt")

    def sampleGen(self):
		fin10 = open("sample.txt", 'r')
		fout6 = open("powerSample.txt", 'a')
		fout7 = open("tempLowerSample.txt", 'a')
		fout8 = open("tempUpperSample.txt", 'a')

		for line in fin10.readlines():
			p_str = "/*power modify here*/{" + (line.split(",")[0])[1:] + "," + line.split(",")[1] + "}, {"\
					+ (line.split(",")[4])[1:] + "," + line.split(",")[5] + "}, {"\
					+ (line.split(",")[8])[1:] + "," + line.split(",")[9] + "}, {"\
					+ (line.split(",")[12])[1:] + "," + line.split(",")[13] + "}, {"\
					+ (line.split(",")[16])[1:] + "," + line.split(",")[17] + "}/*power end modify*/"
			tl_str = "/*lowTemp modify here*/double temp_lower[rid_t] = {" + (line.split(",")[2])[1:] + ".0,"\
					+ line.split(",")[6] + ".0," + line.split(",")[10] + ".0,"\
					+ line.split(",")[14] + ".0," + line.split(",")[18] + ".0}/*lowTemp end modify*/"
			tu_str = "/*upTemp modify here*/double temp_upper[rid_t] = {" + (line.split(",")[3])[1:] + ".0,"\
					+ line.split(",")[7] + ".0," + line.split(",")[11] + ".0,"\
					+ line.split(",")[15] + ".0, " + line.split(",")[19].strip() + ".0}/*upTemp end modify*/"

			fout6.write(p_str + '\n')
			fout7.write(tl_str + '\n')
			fout8.write(tu_str + '\n')

		fin10.close()
		fout6.close()
		fout7.close()
		fout8.close()

if __name__ == "__main__":
    fp = file_process()
#    fp.configFilter()
#    fp.lineNumChoose()
#    fp.configExtract()
#    fp.remainUpdate()
#    fp.combComplete()
    fp.sampleGen()

#!/usr/bin/env python
# -*- coding = utf-8 -*-

'''
	Fan Gu, 2015.12, python 2.7
	This python script is aimed at processing the predict outputs of neural network
'''

import os
import linecache

class predict_process:
	# sort the probability values
	def probSort(self):
		with open("./predictOutput.txt", 'r') as fin1, open("./predictSort.txt", 'a') as fout1:
			probList = []
			for line in fin1.readlines():
				probList.append(line.strip())

			probDict = {}
			keys = range(len(probList))
			for i in keys:
				probDict[i] = probList[i]

			aux = [(probDict[k], k) for k in keys]
			aux.sort()

			for v, k in aux:
				fout1.write(str(k) + ":" + v + "\n")

	#
	def combChoose(self):
		with open("./prediction.txt", 'r') as fin2, open("./predictSort.txt", 'r') as fin3, open("./prePower.txt", 'a') as fout2, open("./preTemp.txt", 'a') as fout3:
			lineArray = []
			for sortLine in fin3.readlines()[0:16]:
				n = sortLine.split(":")[0]
				lineArray.append(linecache.getline("./prediction.txt", int(n)))

			n = 0
			for line in lineArray:
				p_str = "/*power modify here*/{" + (line.split(",")[0]) + "," + line.split(",")[1] + "}, {"\
						+ (line.split(",")[4]) + "," + line.split(",")[5] + "}, {"\
						+ (line.split(",")[8]) + "," + line.split(",")[9] + "}, {"\
						+ (line.split(",")[12]) + "," + line.split(",")[13] + "}, {"\
						+ (line.split(",")[16]) + "," + line.split(",")[17] + "}/*power end modify*/"
				tl_str = "/*lowTemp modify here*/double temp_lower[rid_t] = {" + (line.split(",")[2])[1:] + ".0,"\
						+ line.split(",")[6] + ".0," + line.split(",")[10] + ".0,"\
						+ line.split(",")[14] + ".0," + line.split(",")[18] + ".0};/*lowTemp end modify*/"
				tu_str = "/*upTemp modify here*/double temp_upper[rid_t] = {" + (line.split(",")[3])[1:] + ".0,"\
						+ line.split(",")[7] + ".0," + line.split(",")[11] + ".0,"\
						+ line.split(",")[15] + ".0, " + line.split(",")[19].strip() + ".0};/*upTemp end modify*/"

				n += 1
				fout2.write(str(n) + ":" + '\n' + p_str + '\n')
				fout3.write(str(n) + ":" + '\n' + tl_str + '\n' + tu_str + '\n')


if __name__ == "__main__":
	pp = predict_process()
#	pp.probSort()
	pp.combChoose()

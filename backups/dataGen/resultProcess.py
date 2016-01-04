#!/usr/bin/env python
# -*- coding = utf-8 -*-

'''
	Fan Gu, 2015.12, python 2.7
	This python script is aimed at processing the result of SMC
'''

import os
import fnmatch
import shutil 

class result_process:
	global path
	path = "../final/results/"

	# samples merge
	def sampleMerge(self):
		with open("powerSample.txt", 'r') as fin2, open("tempLowerSample.txt", 'r') as fin3, open("tempUpperSample.txt", 'r') as fin1, open("replace.txt", 'a') as fout1:
			lineArray1 = []
			lineArray2 = []

			for line1 in fin2.readlines():
				lineArray1.append(line1)
			for line2 in fin3.readlines():
				lineArray2.append(line2)

			n = -1
			for line3 in fin1.readlines():
				n += 1
				mergeLine = str(n + 1) + ":" + lineArray1[n].strip('\n') + lineArray2[n].strip('\n') + line3
				fout1.write(mergeLine)

	# find files in some directory and its subdirectory
	def iterfindfiles(self, path, fnexp):
		for root, dirs, files in os.walk(path):
			for filename in fnmatch.filter(files, fnexp):
				yield os.path.join(root, filename)

	# find file, copy it and rename
	def findFileAndCopyAndRename(self):
		n = -1
		for files in self.iterfindfiles("../", "result"):
			n += 1
			name = path + "result" + str(n)
			shutil.copyfile(files, name)

	# result merge
	def resultMerge(self):
		with open("allResults", 'a') as fout2:
			files = os.listdir(path)
			for resultfile in files:
				filename = path + resultfile
				f = open(filename, 'r')
				try:
					resultContent = f.read()
					fout2.write(resultContent.replace('/\n/', '//').replace('/\nProb', '/Prob')\
							.replace('/\r\n/', '//').replace('/\r\nProb', '/Prob'))
				finally:
					f.close()

	# sort the result probability data
	def probSort(self):
		with open("allResults", 'r') as fin4, open("sortResult", 'w') as fout3:
			probArray = []
			for line in fin4.readlines():
				if line.startswith("Prob"):
					line  = (line.split(":")[1]).strip()
					probArray.append(line)

			probArray.sort(reverse = True)
			for sortedProb in probArray:
				fout3.write(sortedProb + '\n')

	# fill the result probability to the samples
	def probGeneration(self):
		with open("replace.txt", 'r') as fin6, open("allResults", 'r') as fin5, open("prob.txt", 'a') as fout4:
			probDict = {}
			for resultLine in fin5.readlines():
				if "Prob:" in resultLine:
					k = (resultLine.split("Prob:")[0]).strip()
					v = (resultLine.split("Prob:")[1]).strip()
					probDict[k] = v

			for fillLine in fin6.readlines():
				matchContent = (fillLine.split(":")[1]).strip()
				if matchContent in probDict:
					newLine = fillLine.replace(matchContent, probDict[matchContent])
					fout4.write(newLine.split(":")[1])
				else:
					fout4.write(fillLine.split(":")[1])

	# process the left samples
	def leftProcess(self):
		with open("./left samples/left", 'r') as fin7, open("./left samples/powerSample.txt", 'a') as fout6, open("./left samples/tempLowerSample.txt", 'a') as fout7, open("./left samples/tempUpperSample.txt", 'a') as fout5:
			for line in fin7.readlines():
				if "/*power modify here*/" in line:
					fout6.write(line.split(":")[1])
					
				if "/*lowTemp modify here*/" in line:
					fout7.write(line)
				
				if "/*upTemp modify here*/" in line:
					fout5.write(line)


if __name__ == "__main__":
	rp = result_process()
#	rp.sampleMerge()
#	rp.findFileAndCopyAndRename()
#	rp.probSort()
#	rp.leftProcess()
	rp.resultMerge()
	rp.probGeneration()

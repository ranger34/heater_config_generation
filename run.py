
#huangsj  Thu Sep 25 15:26:30 CST 2014
#modified by Fan Gu in 2015
#usage: python run.py <result_file_to_save> <model_name>
#example: python run.py r_2nd m1

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys
import time
ISOTIMEFORMAT='%Y-%m-%d %X'

class Uppaal_Parse:

	#huangsj: modify the model.xml at the place between "/*modify here*/" and "/*end modify*/" 
	def model_modify(self, repl1, repl2, repl3): 
		model_txt = open("./"+sys.argv[2] + ".xml", 'r')
		model_str = model_txt.read()
		model_txt.close()
		
		config_pattern1 = re.compile('(..power modify here..).+?(..power end modify..)',re.I|re.S)
		config_pattern2 = re.compile('(..lowTemp modify here..).+?(..lowTemp end modify..)',re.I|re.S)
		config_pattern3 = re.compile('(..upTemp modify here..).+?(..upTemp end modify..)',re.I|re.S)
		
		model_str = config_pattern1.sub(repl1, model_str)
		model_str = config_pattern2.sub(repl2, model_str)
		model_str = config_pattern3.sub(repl3, model_str)
		
		model_txt = open("./"+sys.argv[2] + ".xml", 'w')
		model_txt.write(model_str)
		model_txt.close()

	# get useful information from uppaal verify result output 
	def result_parse(self):
		cmdline = './verifyta -t2 -E0.1 '+ sys.argv[2] + '.xml query.q > tmp'+ sys.argv[2] +'.txt'
		os.system(cmdline)
		txt = open("./tmp"+ sys.argv[2] +".txt")
		txt_str = txt.read()
		prob_pattern = re.compile('(Property is satisfied.).+?(with confidence......)',re.I|re.S)
		probability_info = prob_pattern.search(txt_str)
		if probability_info:
			probability_info = probability_info.group()
			print probability_info
			pat = re.compile('\[.+,')
			p_low = pat.search(probability_info).group()
			p_low =  float(p_low[1:-1])
			pat = re.compile(',.+\]')
			p_up = pat.search(probability_info).group()
			p_up = float(p_up[1:-1])
			p_mean = (p_up+p_low)/2
			confidence = ''
			return (p_low, p_up, p_mean, confidence)
		else:
			print "No Result Generated"

	# configuration exploration
	def config_explore(self):
		dataSet1 = "powerSample.txt";
		dataSet2 = "tempLowerSample.txt"
		dataSet3 = "tempUpperSample.txt"
		
		output = "./"+sys.argv[1];
		
		f1 = open(dataSet1, 'r')
		f2 = open(dataSet2, 'r')
		f3 = open(dataSet3, 'r')
		
		config_file1 = open(dataSet1, 'r')
		config_file2 = open(dataSet2, 'r')
		config_file3 = open(dataSet3, 'r')
		
		self.print_time(output)
		
		while True:
			line1 = (f1.readline())[:-1]
			line2 = (f2.readline())[:-1]
			line3 = (f3.readline())[:-1]
		
			config_line1 = config_file1.readline()
			config_line2 = config_file2.readline()
			config_line3 = config_file3.readline()
			
			if line1 and line2 and line3:
				self.model_modify(line1, line2, line3)
				(p_low, p_up, p_mean, confidence) = self.result_parse()
				result_file = open(output, 'a')
				result_file.write(config_line1 + config_line2 + config_line3 + "Prob: " + str(p_mean) + "\n")
				#if (p_mean > 0.95):
				#	result_file.write("****"+"\n")
				result_file.close()

			else:
				break
		f.close()
		self.print_time(output)
		config_file.close()

	def print_time(self, file):
		result_file = open(file, 'a')
 		result_file.write(time.strftime(ISOTIMEFORMAT, time.localtime( time.time())) + "\n")
		result_file.close()


upp = Uppaal_Parse()
upp.config_explore()


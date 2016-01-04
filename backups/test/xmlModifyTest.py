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
		model_txt = open("./heater.xml", 'r')
		model_str = model_txt.read()
		model_txt.close()

		config_pattern1 = re.compile('(..power modify here..).+?(..power end modify..)',re.I|re.S)
		config_pattern2 = re.compile('(..lowTemp modify here..).+?(..lowTemp end modify..)',re.I|re.S)
		config_pattern3 = re.compile('(..upTemp modify here..).+?(..upTemp end modify..)',re.I|re.S)
		
		model_str = config_pattern1.sub(repl1, model_str)
		model_str = config_pattern2.sub(repl2, model_str)
		model_str = config_pattern3.sub(repl3, model_str)
		
		model_txt = open("./heater_new.xml", 'w')
		model_txt.write(model_str)
		model_txt.close()


	# configuration exploration
	def config_explore(self):
		dataSet1 = "powerSample.txt";
		dataSet2 = "tempLowerSample.txt"
		dataSet3 = "tempUpperSample.txt"
		
		f1 = open(dataSet1, 'r')
		f2 = open(dataSet2, 'r')
		f3 = open(dataSet3, 'r')

		
		line1 = (f1.readline())[:-1]
		line2 = (f2.readline())[:-1]
		line3 = (f3.readline())[:-1]

		self.model_modify(line1, line2, line3)
		
		f1.close()
		f2.close()
		f3.close()


upp = Uppaal_Parse()
upp.config_explore()


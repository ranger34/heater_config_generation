#!/usr/bin/env python
# -*- coding = utf - 8 -*-

import re

class file_process:
    def config_filter(self):
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

	def choose(self):
		fin2 = open("step1.txt", 'r')
        fout2 = open("step2.txt", 'a')

        while True:
            line = fin2.readline()
            if line:
                chooseline = line.split(":")[0]
                fout2.write(chooseline)
            else:
                break

        fin2.close()
        fout2.close()


if __name__ == "__main__":
    fp = file_process()
    fp.config_filter()
    #fp.choose()

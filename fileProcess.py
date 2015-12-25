#!/usr/bin/env python
# -*- coding = utf - 8 -*-

import re
import os

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

        content = fin5.read()
        for replaceLine in fin6.readlines():
            print replaceLine
            content.replace(replaceLine, "")

        fout4.write(content)
        fout4.close()
        fin5.close()
        fin6.close()


if __name__ == "__main__":
    fp = file_process()
#    fp.configFilter()
#    fp.lineNumChoose()
    fp.configExtract()
#    fp.remainUpdate()

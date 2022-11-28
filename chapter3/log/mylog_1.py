#!/bin/env python
#-*- coding: utf-8 -*-

# 인자를 5개로 수정
def printlog(logfile, search_word):
    f = open(logfile)       #file open
    logdata = f.read()      #file read
    f.close()               #file close

    # 코드 수정 시작
    index = logdata.find(search_word)
    # 코드 수정 완료

    if index >= 0 :
        print ("-" * 70)
        print ("Log file : ", logfile)
        print ("Find this word : ", search_word)
        print ("-" * 70)

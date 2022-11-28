#!/bin/env python
#-*- coding: utf-8 -*-

# 인자를 5개로 수정
def printlog(logfile, search_word):
    f = open(logfile)
    logdata = f.read()
    f.close()

    # 코드 수정 시작
    index = logdata.find(search_word)
    # 코드 수정 완료

    if index >= 0 :
        print ("-" * 70)
        print ("Log file : ", logfile)
        print ("Find this word : ", search_word)
        print ("-" * 70)

        print (get_log_data(logdata, index,search_word, index))
        print ("-" * 70)
        
def get_log_data(logdata, start_index) :
    enter_index = max(0, logdata,rfind("\n", 0, start_index))

    enter_index2 = logdata.find("\n", start_index,len(logdata))
    print(enter_index)
    print(enter_index2)
    print(logdata[enter_index :enter_index2])
    return logdata[enter_index : enter_index2]
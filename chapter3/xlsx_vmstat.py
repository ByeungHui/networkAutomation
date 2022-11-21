#!/bin/env python
#-*- coding: utf-8 -*-

from subprocess import *
from xlsxwriter import *

cmd = "vmstat 1 5 | awk '{now=strftime(\"%Y-%m-%d %T \"); print now $0}'"
p = Popen(cmd, shell=True, stdout=PIPE)
(ret, err) = p.communicate()

# 첫번째 헤더를 병합한 셀에 직접 작성
merge_format = workbook.add_format({ "bold" : 1, "align" : "center"})   # 포맷 설정
worksheet.merge_range("A1:B1", "datetime", merge_format)    # 하위 열 2개
worksheet.merge_range("C1:D1", "procs", merge_format)       # 하위 열 2개
worksheet.merge_range("E1:H1", "memory", merge_format)      # 하위 열 4개
worksheet.merge_range("I1:J1", "swap", merge_format)        # 하위 열 2개
worksheet.merge_range("K1:L1", "io", merge_format)          # 하위 열 2개
worksheet.merge_range("M1:N1", "system", merge_format)      # 하위 열 2개
worksheet.merge_range("O1:S1", "cpu", merge_format)         # 하위 열 5개

# 데이터를 줄 단위로 만듭니다.
retDec= ret.decode('utf-8')
rows=retDec.split("\n")
print(ret)
print(retDec)

#rows = ret.split("\n")

workbook = Workbook('vmstat.xlsx')
worksheet = workbook.add_worksheet()

for row_idx, row in enumerate(rows) :
    columns = row.split()
    for col_idx, col in enumerate(columns) :
        worksheet.write(row_idx, col_idx, col)


workbook.close()
#!/usr/bin/python3

import xlrd
import csv

def csv_from_excel(book):
    workbook = xlrd.open_workbook(book)
    sheet = workbook.sheet_by_name('Sheet1')
    csv_file = open('e.csv', 'w')
    record = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

    for row in range(sheet.nrows):
        record.writerow(sheet.row_values(row))

    csv_file.close()

csv_from_excel('e.xlsx')

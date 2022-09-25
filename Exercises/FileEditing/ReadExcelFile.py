# need pip modules xlrd and openpyxl
import xlrd
import openpyxl

# define variable to load the dataframe
dataframe = openpyxl.load_workbook('1MonthOfLaunches.xlsx')

# define variable to read sheet
dataframe1 = dataframe.active


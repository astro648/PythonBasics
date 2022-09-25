import xlwings

ws = xlwings.Book("1MonthOfLaunches.xlsx").sheets['Sheet1']
v1 = ws.range("A1:D16")
print(v1.value)
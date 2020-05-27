# Tool name         :GetProgressChart
# Module name       :GetProgressChart.py
# Detail            :This's the script to make Progress Chart.
# Implementer       :R.Ishikawa
# Version           :1.1
# Last update       :2020/05/23

# HISTORY
#1 Create New                  Ver.1.0  R.I  2020/05/23
#2 Change Input format         Ver.1.1  R.I  2020/05/27

import openpyxl.utils
import os

from openpyxl.styles import PatternFill
from openpyxl.styles.borders import Border, Side
from openpyxl.formatting.rule import FormulaRule

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '進捗管理表'


def cellwidth(start, end, wide):
    for length in range(start, end):
        alpha = sheet.cell(row=1, column=length).coordinate[:-1]
        sheet.column_dimensions['{}'.format(alpha)].width = wide


cellwidth(1, 7, 8.38)   # A-F列セルのサイズ設定
cellwidth(7, 8, 40)     # G列セルのサイズ設定
cellwidth(2, 3, 17.38)  # B列セルのサイズ設定
cellwidth(8, 9, 0.38)   # H列セルのサイズ設定
cellwidth(9, 335, 4.88) # I-LV列セルのサイズ設定

for rows in range(1, 100):
    sheet.row_dimensions[rows].height = 19

side1 = Side(style='thin', color='000000')
side2 = Side(style='double', color='000000')
side3 = Side(style='hair', color='000000')

for rows in sheet.iter_rows(min_row=1, min_col=1, max_row=100, max_col=9):
    for cell in rows:
        if cell.row == 5:
            cell.border = Border(right=side1, bottom=side2)
        else:
            cell.border = Border(top=None, right=side1, bottom=None, left=None)

for rows in sheet.iter_rows(min_row=1, min_col=9, max_row=100, max_col=335):
    for cell in rows:
        if cell.row == 5:
            cell.border = Border(right=side3, bottom=side2)
        else:
            cell.border = Border(top=side3, right=side3, bottom=side3, left=side3)


# 同じ階層のディレクトリからproperty.txtをオープン
property_data = open("property.txt", "r")

# property.txtを1行ずつ要素として読み込み、PROPERTYリストを作成
PROPERTY = property_data.readlines()

startYear = int(PROPERTY[0])  # PROPERTYリストの1つ目の値を引用
startMonth = int(PROPERTY[1]) # PROPERTYリストの2つ目の値を引用
startDay = int(PROPERTY[2])   # PROPERTYリストの3つ目の値を引用

sheet["B5"].value = "タスク"
sheet["C4"].value = "着手日"
sheet["C5"].value = "予定"
sheet["D5"].value = "実績"
sheet["E4"].value = "完了日"
sheet["E5"].value = "予定"
sheet["F5"].value = "実績"
sheet["G5"].value = "備考"
sheet["I2"].value = startYear
sheet["J2"].value = "年"
sheet["I3"].value = startMonth
sheet["J3"].value = "月"

sheet["I4"].number_format = "d"
sheet["I4"].value = '=DATE(I2, I3, {})'.format(startDay)
sheet["I5"].number_format = "aaa"
sheet["I5"].value = '=I4'

for rows in sheet.iter_rows(min_row=4, min_col=10, max_row=5, max_col=334):
    for cell in rows:
        if cell.row == 4:
            cell.number_format = 'd'
            cell.value = '={}+1'.format(sheet.cell(row=cell.row, column=cell.column-1).coordinate)
        else:
            cell.number_format = 'aaa'
            cell.value = '={}'.format(sheet.cell(row=cell.row-1, column=cell.column).coordinate)

for rows in sheet.iter_rows(min_row=3, min_col=11, max_row=3, max_col=334):
    for cell in rows:
        cell.number_format = "m"
        cell.value = '=IF(DAY({0})=1, {1},"")'.format(sheet.cell(column=cell.column, row=cell.row + 1).coordinate,
                                                      sheet.cell(column=cell.column, row=cell.row + 1).coordinate)


def colorMake(types, start, end):
    return PatternFill(fill_type=types, start_color=start, end_color=end)


grayfill = colorMake('solid', 'd3d3d3', 'd3d3d3')
planfill = colorMake('solid', PROPERTY[3], PROPERTY[3]) #計画セル色。PROPERTYリストの4つ目の値を引用
actualfill = colorMake('solid', PROPERTY[4], PROPERTY[4]) #実績セル色。PROPERTYリストの5つ目の値を引用

for rows in sheet.iter_rows(min_row=6, min_col=2, max_row=100, max_col=7):
    for cell in rows:
        cell.number_format = "m/d"
sheet.conditional_formatting.add('C6:G100', FormulaRule(formula=['NOT($F6="")'], stopIfTrue=True, fill=grayfill))

sheet.conditional_formatting.add('I4:ME100', FormulaRule(formula=['OR(WEEKDAY(I$5)=1, WEEKDAY(I$5)=7)'], stopIfTrue=True, fill=grayfill))

sheet.conditional_formatting.add('I6:ME100', FormulaRule(formula=['AND($D6<=I$4, $F6>=I$4)'], stopIfTrue=True, fill=actualfill))
sheet.conditional_formatting.add('I6:ME100', FormulaRule(formula=['AND($C6<=I$4, $E6>=I$4)'], stopIfTrue=True, fill=planfill))

sheet.freeze_panes = 'I6'

desktop_path = PROPERTY[5] # PROPERTYリストの6つ目の値を引用
wb.save(desktop_path + '進捗管理表.xlsx')

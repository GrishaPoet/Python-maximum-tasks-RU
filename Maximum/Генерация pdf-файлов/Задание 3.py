#Работа со статьёй (Задание №3, Урок 10)
#Задача: С помощью python можно работать не только с pdf-файлами, но и excel,
#изучите данную статью и повторите код, представленный в ней.
#https://habr.com/ru/post/232291/

#Ответ:
import xlrd, xlwt
rb = xlrd.open_workbook('../ArticleScripts/ExcelPython/xl.xls',formatting_info=True)
sheet = rb.sheet_by_index(0)



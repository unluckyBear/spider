#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib
import xlwt

def cityRun():
	print '58Í¬³Ç start...'
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('58')
	sheet.write(0,0,'xx58')
	sheet.write(0,1,'xx')

	html = urllib.urlopen('http://sh.58.com/zufang/j1/?PGTID=14334892048890.18738903105258942&ClickID=1&final=1&searchtype=3&key=%2525u7533%2525u57CE%2525u4F73%2525u82D1&sourcetype=5').read()
	soup = BeautifulSoup(html)
	priceList = soup.find_all('b',class_='pri')

	count = 0
	for price in priceList:
		if int(price.text) <= 1000:
			count = count + 1
			td = price.parent.findPreviousSibling('td')
			sheet.write(count,0,td.find('a')['href'])
			sheet.write(count,1,price.text)

	wb.save("58.xls")

	
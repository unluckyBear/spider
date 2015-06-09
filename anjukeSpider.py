#-*-coding:utf-8-*-
from bs4 import BeautifulSoup
import urllib
import xlwt

def anjukeRun():
	print 'anjuke start...'
	wb = xlwt.Workbook()
	sheet = wb.add_sheet('anjuke')

	sheet.write(0,0,'xx')
	sheet.write(0,1,'xx')
	sheet.write(0,2,'xx')
	sheet.write(0,3,'xx')

	num = 0
	for i in range(2):
		html = urllib.urlopen('http://sh.zu.anjuke.com/fangyuan/fx1-p'+ str(i+1) +'/?comm_exist=on&kw=%E7%94%B3%E5%9F%8E%E4%BD%B3%E8%8B%91&kw_search_input=%E7%94%B3%E5%9F%8E%E4%BD%B3%E8%8B%91&landmark_kw_segment=%E7%94%B3%E5%9F%8E+%E4%BD%B3%E8%8B%91#filtersort').read()
		soup = BeautifulSoup(html)

		priceList = soup.find_all('dd', class_='dd_price')
		for price in priceList:
			content = price.contents[0].text
			link = price.parent['link']

			if int(content) <= 1000:
				num = num + 1

				sheet.write(num,0,link)
				sheet.write(num,1,content)

				childHtml = urllib.urlopen(link).read()
				childSoup = BeautifulSoup(childHtml)
				trueName = childSoup.find(id='broker_true_name').get_text()
				telephone = childSoup.find_all('i', class_='p_icon icon_tel')[0].next_sibling

				sheet.write(num,2,trueName)
				sheet.write(num,3,telephone)

	wb.save("anjuke.xls")

	
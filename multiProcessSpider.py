#-*-coding:utf-8-*-
from multiprocessing import Pool
from anjukeSpider import anjukeRun
from citySpider import cityRun

if __name__=='__main__':
	print 'hahaha....'
	p = Pool()
	p.apply_async(anjukeRun, ())
	p.apply_async(cityRun, ())

	p.close()
	p.join()
	print 'hehehe...'
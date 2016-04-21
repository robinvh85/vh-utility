import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues() 11")
	
	url = "http://www.invest-tracing.com/{0}".format(url)	
	
	d = pq(url=url)
	print("URL: " + url)
	
	list = d("[border='0'].listbody td")	
	
	#list = d(".listbody td")	
	
	print("LIST: ", len(list))
	
	index = 20
	while index < len(list):				
		obj = {}
		obj['date'] = list[index].text_content()
		obj['user'] = list[index + 1].text_content()
		obj['deposit'] = list[index + 2].text_content().split("/")[0].replace("$", "")
		
		print("{0} - {1} - {2}".format(obj['date'], obj['user'], obj['deposit']))		
		index += 5
	
	#common.insertSiteStat(obj)

def run():	
	print "\n========== RUN invest_tracing.run() ============"
#	try :
	getValues("rcb-Currency-Trader.html")
#	except Exception:
#		pass
	





import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	d = pq(url="https://www.{0}".format(url))
	list = d(".info")
	investArea = d(".info span")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
	
	obj['total_account'] = list[0].text_content().split(" ")[1]
	obj['active_account'] = 0
	obj['total_deposit'] = investArea[0].text_content().replace("$ ", "")
	obj['total_withdraw'] = investArea[1].text_content().replace("$ ", "")
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN nanoproinvest_com.run() ============"
	try :
		getValues("nanoproinvest.com")
	except Exception:
		pass
	





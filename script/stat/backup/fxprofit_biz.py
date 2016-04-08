import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	d = pq(url="https://{0}".format(url))
	list = d(".statistics-item span")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
	
	obj['total_account'] = list[5].text_content()
	obj['active_account'] = list[3].text_content()
	obj['total_deposit'] = list[0].text_content().replace("$ ", "")
	obj['total_withdraw'] = list[1].text_content().replace("$ ", "")
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN stockmarketinv_club.run() ============"
	try :
		getValues("fxprofit.biz")
	except Exception:
		pass
	





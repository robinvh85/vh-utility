import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	url = "https://{0}".format(url)
	print("Call : {0}".format(url))
	d = pq(url=url)
	list = d("#sub-state .numeri")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
		
	obj['total_account'] = list[1].text_content().split(":")[1]
	obj['active_account'] = 0
	obj['total_deposit'] = list[2].text_content().split(":")[1].replace("$ ", "")
	obj['total_withdraw'] = list[3].text_content().split(":")[1].replace("$ ", "")
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN wealthycityltd_com.run() ============"
	try :
		getValues("wealthycityltd.com")
	except Exception:
		pass
	





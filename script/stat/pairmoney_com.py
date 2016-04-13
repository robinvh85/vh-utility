import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	d = pq(url="http://{0}".format(url))
	list = d(".container .row .col-md-6")
	list2 = d(".container .row .col-md-6 a")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
		
	obj['total_account'] = list[0].text_content().split("Total account :")[1].split(" ")[1]
	obj['active_account'] = 0
	obj['total_deposit'] = list2[0].text_content().split("$")[1].split(" ")[1]
	obj['total_withdraw'] = 0
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN pairmoney_com.run() ============"
	try :
		getValues("pairmoney.com")
	except Exception:
		pass
	





import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(url):
	print("getValues()")
	
	d = pq(url="https://{0}".format(url))
	list = d("table table table table td")
	obj = {}
	obj['site_id'] = common.getSiteId(url)
	
	if obj['site_id'] == None:
		obj['site_id'] = -1
		
	obj['total_account'] = list[28].text_content().split(":")[1]
	obj['active_account'] = 0
	obj['total_deposit'] = list[36].text_content().split(":")[1].replace("$ ", "")
	obj['total_withdraw'] = list[40].text_content().split(":")[1].replace("$ ", "")
	obj['time'] = long(time.time()) * 1000
	
	print("{0} - {1} - {2} {3}".format(obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time']))
	common.insertSiteStat(obj)

def run():	
	print "\n========== RUN rioze_com.run() ============"
	try :
		getValues("rioze.com")
	except Exception:
		pass
	





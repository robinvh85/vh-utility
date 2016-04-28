import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(item):
	url = item[3]
	print("getValues(): ", url)
	format = "%b %d %Y %H:%M:%S"
	
	d = pq(url=url)
	list = d("tr[bgcolor='#FFFFFF'] td[width='25%']")	
	list1 = d("tr[bgcolor='#FFFFFF'] td[width='20%']")	
	
	index = 0
	index1 = 0
	while index < len(list):			
		try:
			obj = {}
			obj['date'] = common.removeNumberString(list[index].text_content())
			obj['time'] = common.dateStringToTimestamp(obj['date'])
			obj['time'] = common.formatTimestamp(obj['time'])
			obj['user'] = list1[index1].text_content()
			obj['deposit'] = list1[index1 + 1].text_content().split("/")[0].replace("$", "")
			obj['site_id'] = item[0]
			obj['monitor'] = item[2]
			
			print("{0} - {1} - {2} - {3} - {4} - {5}".format(obj['site_id'], obj['monitor'], obj['date'], obj['time'], obj['user'], obj['deposit']))
			if common.insertUserRcb(obj) == -1:
				return
		except Exception:
			pass
		index += 1
		index1 += 3

def run(item):	
	print "\n========== RUN myinvestblog.run() ============"
#	try :
	getValues(item)
#	except Exception:
#		pass
	





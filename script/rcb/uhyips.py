import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(item):
	url = item[3]
	print("getValues(): ", url)
	format = "%d %b,%Y"
	
	d = pq(url=url)
	list = d(".rcbtable table[width='100%'] td")	
	
	index = 0
	while index < len(list):			
		try:
			obj = {}
			obj['date'] = list[index].text_content()
			obj['time'] = common.dateStringToTimestamp(obj['date'], format=format)
			obj['time'] = common.formatTimestamp(obj['time'])
			obj['user'] = list[index + 1].text_content()
			obj['deposit'] = list[index + 3].text_content().replace("$", "")
			obj['site_id'] = item[0]
			obj['monitor'] = item[2]
			
			print("{0} - {1} - {2} - {3} - {4} - {5}".format(obj['site_id'], obj['monitor'], obj['date'], obj['time'], obj['user'], obj['deposit']))
			if common.insertUserRcb(obj) == -1:
				return
		except Exception:
			pass
		index += 7

def run(item):	
	print "\n========== RUN uhyips.run() ============"
#	try :
	getValues(item)
#	except Exception:
#		pass
	





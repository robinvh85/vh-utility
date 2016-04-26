import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(item):
	url = item[3]
	print("getValues(): ", url)
	
	d = pq(url=url)
	list = d("[border='0'].listbody td")	

	index = 20
	while index < len(list):	
		try :
			obj = {}
			obj['date'] = list[index].text_content()
			obj['time'] = common.dateStringToTimestamp(obj['date'])
			obj['time'] = common.formatTimestamp(obj['time'])
			obj['user'] = list[index + 1].text_content()
			obj['deposit'] = list[index + 2].text_content().split("/")[0].replace("$", "")
			obj['site_id'] = item[0]
			obj['monitor'] = item[2]		
				
			print("{0} - {1} - {2} - {3} - {4} - {5}".format(obj['site_id'], obj['monitor'], obj['date'], obj['time'], obj['user'], obj['deposit']))
			if common.insertUserRcb(obj) == -1:
				return
		except Exception:
			pass
		index += 5

def run(item):	
	print "\n========== RUN invest_tracing.run() ============"
#	try :
	getValues(item)
#	except Exception:
#		pass
	





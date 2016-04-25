import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(item):
	url = item[3]
	print("getValues(): ", url)
	
	d = pq(url=url)
	list = d("#content2 table[cellspacing='0'] td")	

	index = 6
	while index < len(list):	
		try :
			obj = {}
			obj['date'] = list[index].text_content()
			obj['time'] = common.dateStringToTimestamp(obj['date'])
			obj['time'] = common.formatTimestamp(obj['time'])
			obj['user'] = list[index + 1].text_content()
			obj['deposit'] = list[index + 2].text_content().replace("$", "")
			obj['site_id'] = item[0]
			obj['monitor'] = item[2]		
				
			print("{0} - {1} - {2} - {3} - {4} - {5}".format(obj['site_id'], obj['monitor'], obj['date'], obj['time'], obj['user'], obj['deposit']))
			common.insertUserRcb(obj)
		except Exception:
			pass		
		index += 6

def run(item):	
	print "\n========== RUN hyipscope.run() ============"
#	try :
	getValues(item)
#	except Exception:
#		pass
	





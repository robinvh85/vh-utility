import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

def getValues(ref_id):
	print("getValues() 11")
	
	format = "%b %d %Y %H:%M:%S"
	url = "http://hyip-cruiser.com/?a=refback&lid={0}".format(ref_id)	
	
	d = pq(url=url)
	print("URL: " + url)
	
	list = d(".details .list td")	
	
	#list = d(".listbody td")	
	
	print("LIST: ", len(list))
	
	index = 0
	while index < len(list):				
		obj = {}
		obj['date'] = common.removeNumberString(list[index].text_content())
		obj['time'] = common.dateStringToTimestamp(obj['date'], format)
		obj['user'] = list[index + 1].text_content()
		obj['deposit'] = list[index + 2].text_content().split("/")[0].replace("$", "")
		
		print("{0} - {1} - {2} - {3}".format(obj['date'], obj['time'], obj['user'], obj['deposit']))		
		index += 5
	
	#common.insertSiteStat(obj)

def run():	
	print "\n========== RUN hyip_cruiser.run() ============"
#	try :
	getValues("4652")
#	except Exception:
#		pass
	





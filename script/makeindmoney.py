import sys
import os.path
import urllib2
import re
from pyquery import PyQuery as pq

import common

def getId(url):
	arr = url.split("/")
	id = arr[len(arr) - 2]
	
	return id

def getSiteUrl(urlRequest, monitor, rcbUrl):
	result = ""
	#urlRequest = "http://{0}{1}".format(monitor, urlRequest)
	print("REQUEST: {0}".format(urlRequest))
	try:
		req = urllib2.urlopen(urlRequest, timeout=30)
		url = req.geturl()
		print("URL: ", url)
		arr = url.split("/?")
		arr1 = arr[0].split("//")
		
		result = arr1[1].replace("www.", "")
		result = result.split("/")[0]
	except :
		print("========== ERROR ===========")
		#common.insertUnknowSite(rcbUrl, monitor)
	
	return result

def getRcb(monitor):
	print("Monitor: ", monitor)
	
	rcb_url = "http://{0}/new/".format(monitor)
	d = pq(url=rcb_url)
	list = d(".list .program a.name")
	siteList = []
	
	for item in list:
		obj = {}
		obj['id'] = getId(item.get("href"))

		if common.getSiteMonitorByRefSiteId(monitor, obj['id']) == None:
			obj['siteRCBUrl'] = "http://{0}/refback/lid/{1}/".format(monitor, obj['id'])
			obj['url'] = getSiteUrl(item.get("href"), monitor, obj['siteRCBUrl'])
			obj['siteId'] = ""
				
			if obj['url'] != '':
				siteId = common.insertSite(obj)
				obj['siteId'] = siteId
				
				siteList.append(obj)
			print("{0} - {1} - {2}".format(obj['id'], obj['url'], obj['siteId']))
				
	for item in siteList:
		common.insertSiteMonitor(item, monitor)
	
def run():
	MONITOR = "makeindmoney.com"
	getRcb(MONITOR)
	#checkRcb(MONITOR)

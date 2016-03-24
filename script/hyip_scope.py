import sys
import os.path
import urllib2
import re
from pyquery import PyQuery as pq

import common

def getId(url):
	arr = url.split("-")
	arr1 = arr[1].split(".")
	id = arr1[0]
	return id

def getSiteUrl(urlRequest, monitor):
	result = ""
	print("REQUEST: {0}".format(urlRequest))
	try:
		req = urllib2.urlopen(urlRequest, timeout=30)
		url = req.geturl()
	
		arr = url.split("/?")
		arr1 = arr[0].split("//")
		
		result = arr1[1].replace("www.", "")
		result = result.split("/")[0]
	except :
		print("========== ERROR ===========")
		common.insertUnknowSite(urlRequest, monitor)
	
	return result

def getRcb(monitor):
	print("hyip_scope.getRcb()")
	
	rcb_url = "http://{0}/allrcb.html".format(monitor)
	d = pq(url=rcb_url)
	tables = d("table tr td font a")
	siteList = []
	
	for item in tables:
		if item.text:
			obj = {}
			obj['id'] = getId(item.get("href"))
			obj['url'] = getSiteUrl(item.get("href"), monitor)		
			obj['siteId'] = ""
			obj['siteRCBUrl'] = ""
				
			if obj['url'] != '':
				siteId = common.insertSite(obj)
				obj['siteId'] = siteId
				obj['siteRCBUrl'] = "http://{0}/rcb-{1}.html".format(monitor, obj['id'])
				
				print("{0} - {1} - {2}".format(obj['id'], obj['url'], obj['siteId']))
				
			siteList.append(obj)
				
	for item in siteList:
		common.insertSiteMonitor(item, monitor)

def checkPaid(siteUrl):
	d = pq(url=siteUrl)
	tables = d("#content2 table.listbody tr td:nth-child(6) center")
	result = False
	
	#print(tables)
	for item in tables:
		if re.search('paid', item.text_content(), re.IGNORECASE):
			result = True
			
	return result

def checkRcb(monitor):
	siteMonitors = common.getSiteMonitor(monitor)
	for item in siteMonitors:
		print(item)
		if item[2] == 0:
			if checkPaid(item[1]):
				common.setPaid(item[0])
	
def run():
	MONITOR = "hyipscope.org"
	getRcb(MONITOR)
	checkRcb(MONITOR)


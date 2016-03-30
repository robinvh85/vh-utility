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
		common.insertUnknowSite(rcbUrl, monitor)
	
	return result

def getRcb(monitor):
	print("hyip_income.getRcb()")
	
	rcb_url = "http://{0}/new/".format(monitor)
	d = pq(url=rcb_url)
	list = d(".program a.name")
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
	MONITOR = "hyipincome.com"
	getRcb(MONITOR)
	#checkRcb(MONITOR)

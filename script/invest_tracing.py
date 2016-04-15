import sys
import os.path
import urllib2
import re
from pyquery import PyQuery as pq

import common

def getId(url):
	print("=====> ", url)
	arr = url.split("-")
	arr1 = arr[1].split(".")
	id = arr1[0]
	return id

def getSiteUrl(id, monitor, rcbUrl):
	result = ""
	urlRequest = "http://www.{0}/{1}".format(monitor, id)
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
	print("invest_tracing.getRcb()")
	
	rcb_url = "http://{0}/newadd.html".format(monitor)
	d = pq(url=rcb_url)
	tables = d(".listbody tr td[width='28%'] .pro")
	siteList = []
	
	for index, item in enumerate(tables):
		try:
			obj = {}
			obj['id'] = getId(item.get("href"))
			obj['siteRCBUrl'] = "http://{0}/rcb-{1}.html".format(monitor, obj['id'])
			obj['url'] = getSiteUrl(item.get("href"), monitor, obj['siteRCBUrl'])
			obj['siteId'] = ""
				
			if obj['url'] != '':
				siteId = common.insertSite(obj)
				obj['siteId'] = siteId
				
				siteList.append(obj)
				print("{0} - {1} - {2}".format(obj['id'], obj['url'], obj['siteId']))
		except:
			pass
				
	for item in siteList:
		common.insertSiteMonitor(item, monitor)
	
def run():
	MONITOR = "invest-tracing.com"
	getRcb(MONITOR)


import sys
import os.path
from time import sleep
from datetime import datetime
import requests
import urllib2
from pyquery import PyQuery as pq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import config
import util
import mysql

def getId(url):
	arr = url.split("=")
	id = arr[len(arr) - 1]
	return id

def getSiteUrl(id):
	urlRequest = "http://hyiptank.net/hyip-{0}.html".format(id)
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
	
	return result

def insertSite(obj):
	query = """
		INSERT IGNORE INTO sites(url, name) values ('{0}', '{1}')
	""".format(obj['url'], obj['name'])
	
	return mysql.executeInsert(query)

def insertSiteMonitor(obj, monitor):
	query = """
		INSERT IGNORE INTO site_monitor(site_id, monitor, ref_site_id, ref_site_url) values ({0}, '{1}', {2}, '{3}')
	""".format(obj['siteId'], monitor, obj['id'], obj['siteRCBUrl'])
	
	return mysql.executeNoneQuery(query)
	
def main():	
	print "\n========== RUN get_rcb.py ============"
	util.logNow("START AT")
	
	d = pq(url=URL)
	tables = d("table.listbody tr td[align='right'] a")
	siteList = []
	
	print("TABLE: ", len(tables))
	
	for index, item in enumerate(tables):
		if index % 2 == 0 and index < len(tables) - 2:
			obj = {}
			obj['id'] = getId(item.get("href"))
			obj['url'] = getSiteUrl(obj['id'])
			obj['siteId'] = ""
			obj['siteRCBUrl'] = ""
			
			print("URL:", obj['url'])
			if obj['url'] != '':
				siteId = insertSite(obj)
				obj['siteId'] = siteId
				obj['siteRCBUrl'] = "http://{0}/rcb-{1}.html".format(MONITOR, obj['id'])
				
				print("{0} - {1} - {2}".format(obj['id'], obj['url'], obj['siteId']))
				
	#		siteList.append(obj)
					
	#for item in siteList:
	#	insertSiteMonitor(item, MONITOR)
	
	util.logNow("END AT")
		
############## Main #############
datetimeNow = util.getDatetimeNow()
MONITOR = "hyiptank.net"
URL = "http://{0}/allrcb.html".format(MONITOR)

mysql.connect()

main()

mysql.disconnect()




import sys
import os.path
from lxml import etree
from datetime import datetime
import urllib2
from pyquery import PyQuery as pq
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import config
import util
import mysql

def setPaid(siteId):
	query = """
		UPDATE site_monitor SET is_paid = 1 WHERE site_id = {0}
	""".format(siteId)
	
	return mysql.executeNoneQuery(query)	
	
def getSiteMonitor():
	query = """
		SELECT site_id, ref_site_url, is_paid
		FROM site_monitor sm
		JOIN sites s ON s.id = sm.site_id AND s.is_scam = 0
		WHERE sm.is_paid = 0
	"""
	
	return mysql.executeQuery(query)

def checkPaid(siteUrl):
	d = pq(url=siteUrl)
	tables = d("#content2 table.listbody tr td:nth-child(6) center")
	result = False
	
	#print(tables)
	for item in tables:
		if re.search('paid', item.text_content(), re.IGNORECASE):
			result = True
			
	return result
	
def main():	
	print "\n========== RUN check_rcb.py ============"
	util.logNow("START AT")
	
	siteMonitors = getSiteMonitor()
	for item in siteMonitors:
		print(item)
		if item[2] == 0:
			if checkPaid(item[1]):
				setPaid(item[0])	
			
	util.logNow("END AT")
		
############## Main #############
datetimeNow = util.getDatetimeNow()
URL = "http://hyipscope.org/rcb-6474.html"

mysql.connect()

main()

mysql.disconnect()




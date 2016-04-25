import sys
import os.path
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import util
import mysql

def insertSite(obj):
	query = """
		SELECT id FROM sites WHERE url = '{0}'
	""".format(obj['url'])
	
	id = mysql.executeScalar(query)
	
	if id == None:
		query = """
			INSERT INTO sites(url) values ('{0}')
		""".format(obj['url'])
		
		id = mysql.executeInsert(query)
		
	return id 

def insertSiteMonitor(obj, monitor):
	query = """
		INSERT IGNORE INTO site_monitor(site_id, monitor, ref_site_id, ref_site_url) values ({0}, '{1}', '{2}', '{3}')
	""".format(obj['siteId'], monitor, obj['id'], obj['siteRCBUrl'])
	
	return mysql.executeNoneQuery(query)

def insertUnknowSite(url, monitor):
	query = """
		INSERT IGNORE INTO unknow_sites(url, monitor) values ('{0}', '{1}')
	""".format(url, monitor)
	
	return mysql.executeNoneQuery(query)
	
def setPaid(siteId):
	query = """
		UPDATE site_monitor SET is_paid = 1 WHERE site_id = {0}
	""".format(siteId)
	
	return mysql.executeNoneQuery(query)	
	
def getSiteMonitor(monitor):
	query = """
		SELECT site_id, ref_site_url, is_paid
		FROM site_monitor sm
		JOIN sites s ON s.id = sm.site_id AND s.is_scam = 0
		WHERE sm.is_paid = 0 AND sm.monitor = '{0}'
	""".format(monitor)
	
	return mysql.executeQuery(query)
	
def getSiteMonitorByRefSiteId(monitor, refSiteId):
	query = """
		SELECT ref_site_url
		FROM site_monitor
		WHERE monitor='{0}' AND ref_site_id='{1}'
	""".format(monitor, refSiteId)
	
	return mysql.executeScalar(query)

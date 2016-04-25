import sys
import os.path
from datetime import datetime
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import util
import mysql

def dateStringToTimestamp(dateString, timezone=0, format = '%Y-%m-%d %H:%M:%S'):
	#print("Date: ", dateString)
	obj = datetime.strptime(dateString, format)
	return (long(time.mktime(obj.timetuple())) - timezone*86400 ) * 1000
 
def formatTimestamp(timestamp, format=None):
    result = ""    
    length = len(str(timestamp))    
    
    if format == None:
        format = "%Y-%m-%d %H:%M:%S"
    
    if length > 10:    
        div = pow(10, length - 10)
        timestamp = timestamp / div    
    
    result = datetime.fromtimestamp(timestamp).strftime(format)
    
    return result;
	
def removeNumberString(dateString):
	dateString = dateString.replace("st,", "")
	dateString = dateString.replace("nd,", "")
	dateString = dateString.replace("rd,", "")
	dateString = dateString.replace("th,", "")
	return dateString

def getRcbSites():
	query = """
		 select s.id, s.url, sm.monitor, sm.ref_site_url 
		 from sites s 
		 join site_monitor sm ON sm.site_id = s.id 
		 where s.is_stat = 1 AND s.is_scam=0
	"""
	
	return mysql.executeQuery(query)
	
def insertUserRcb(obj):
	query = """
		INSERT INTO user_rcb(site_id, monitor, time, user, deposit) values ({0}, '{1}', '{2}', '{3}', {4})
	""".format(obj['site_id'], obj['monitor'], obj['time'], obj['user'], obj['deposit'])
	
	return mysql.executeNoneQuery(query)
	
def getSiteId(url):
	query = """
		SELECT id FROM sites WHERE url = '{0}'
	""".format(url)
	
	return mysql.executeScalar(query)
	
def statsRcbDaily():
	query = """
		REPLACE INTO user_rcb_daily(date, site_id, monitor, count, deposit)
		SELECT DATE(time), site_id, monitor, COUNT(*) as count, SUM(deposit) as deposit 
		FROM user_rcb
		GROUP BY DATE(time), site_id, monitor
	"""
	
	return mysql.executeNoneQuery(query)
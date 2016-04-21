import sys
import os.path
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import util
import mysql

def insertSiteStat(obj):
	query = """
		INSERT INTO site_stats(site_id, total_account, active_account, total_deposit, total_withdraw, time) values ({0}, {1}, {2}, {3}, {4}, {5})
	""".format(obj['site_id'], obj['total_account'], obj['active_account'], obj['total_deposit'], obj['total_withdraw'], obj['time'])
	
	return mysql.executeNoneQuery(query)
	
def getSiteId(url):
	query = """
		SELECT id FROM sites WHERE url = '{0}'
	""".format(url)
	
	return mysql.executeScalar(query)
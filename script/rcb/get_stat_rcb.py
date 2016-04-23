import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import invest_tracing
import hyip_cruiser

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
	
	rcb_list = common.getRcbSites()
	for item in rcb_list:
		if item[2] == "invest-tracing.com":
			invest_tracing.run(item)
		else if item[2] == "hyip-cruiser.com"
			hyip_cruiser.run(item)
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()
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
import hyipscope
import graspgold
import myhyips
import hyipdollar
import makeindmoney
import myinvestblog
import uhyips

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
	
	rcb_list = common.getRcbSites()
	for item in rcb_list:
		print("=========> PAGE: ", item[1])
		if item[2] == "invest-tracing.com":
			invest_tracing.run(item)
		elif item[2] == "hyip-cruiser.com":
			hyip_cruiser.run(item)
		elif item[2] == "hyipscope.org":
			hyipscope.run(item)
		elif item[2] == "graspgold.com":
			graspgold.run(item)
		elif item[2] == "myhyips.net":
			myhyips.run(item)
		elif item[2] == "hyipdollar.com":
			hyipdollar.run(item)
		elif item[2] == "makeindmoney.com":
			makeindmoney.run(item)
		elif item[2] == "myinvestblog.ru":
			myinvestblog.run(item)
		elif item[2] == "uhyips.com":
			uhyips.run(item)
		
	common.statsRcbDaily()
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()
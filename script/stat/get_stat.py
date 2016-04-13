import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import custommining_com
import unitedswissbanks_com
import depdun_com
import bullair_biz
import oktrade_biz
import lucrativeventure_co
import coiner_biz
import robloxfunds_com
import pairmoney_com
import effective_fund_com

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
		
	custommining_com.run()
	unitedswissbanks_com.run()
	depdun_com.run()
	bullair_biz.run()	
	oktrade_biz.run()
	lucrativeventure_co.run()
	coiner_biz.run()
#	robloxfunds_com.run()
	pairmoney_com.run()
#	effective_fund_com.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




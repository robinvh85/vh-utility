import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import unitedswissbanks_com
import depdun_com
import oktrade_biz
import lucrativeventure_co
import pairmoney_com
import effective_fund_com
import vertexasset_com

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
		
	unitedswissbanks_com.run()
	depdun_com.run()	
	oktrade_biz.run()
	lucrativeventure_co.run()
	pairmoney_com.run()
	vertexasset_com.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




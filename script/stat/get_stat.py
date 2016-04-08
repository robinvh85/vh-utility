import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util

import webflipfunds_com
import custommining_com
import unitedswissbanks_com
import managerhourly_com
import nanoproinvest_com
import bitcoinnetworks_biz
import city_finance_org
import greed_rush_com
import bitcoinpalas_com
import depdun_com
import paragoninvest_biz
import bullair_biz
import oktrade_biz
import lucrativeventure_co
import coiner_biz

def main():	
	print "\n========== RUN get_stat.py ============"
	util.logNow("START AT")
		
	webflipfunds_com.run()
	custommining_com.run()
	unitedswissbanks_com.run()
	managerhourly_com.run()
	nanoproinvest_com.run()
	bitcoinnetworks_biz.run()
	city_finance_org.run()
	greed_rush_com.run()
	bitcoinpalas_com.run()
	depdun_com.run()
	paragoninvest_biz.run()
	bullair_biz.run()	
	oktrade_biz.run()
	lucrativeventure_co.run()
	coiner_biz.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




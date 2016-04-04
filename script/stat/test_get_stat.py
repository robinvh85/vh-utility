import sys
import os.path
from pyquery import PyQuery as pq
import time
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import mysql
import util
import bitcoinpalas_com


def main():	
	print "\n========== RUN test_get_stat.py ============"
	util.logNow("START AT")
	
	bitcoinpalas_com.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import util
import mysql
import makeindmoney
def main():	
	print "\n========== RUN test_get_rcb.py ============"
	util.logNow("START AT")
	
	makeindmoney.run()	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




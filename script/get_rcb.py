import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "lib")))
import util
import mysql
import hyip_scope
import hyip_tank
import hyip_stop
import my_hyip
import gs_monitor
import hyip_income
import invest_tracing
	
def main():	
	print "\n========== RUN get_rcb.py ============"
	util.logNow("START AT")
	
	hyip_scope.run()
	hyip_tank.run()
	hyip_stop.run()
	my_hyip.run()
	gs_monitor.run()
	hyip_income.run()
	invest_tracing.run()
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




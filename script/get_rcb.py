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
import my_invest_blog
import hyip_cruiser_com
import bloghyip_com
import goodhyip_biz
import list4hyip_com
	
def main():	
	print "\n========== RUN get_rcb.py ============"
	util.logNow("START AT")
	
	hyip_scope.run()	
	my_hyip.run()	
	invest_tracing.run()
	my_invest_blog.run()
	list4hyip_com.run()
	hyip_cruiser_com.run()
	gs_monitor.run()	
	hyip_income.run()
	hyip_tank.run()	
	hyip_stop.run()
	bloghyip_com.run()
	goodhyip_biz.run()	
	
	util.logNow("END AT")

############## Main #############
datetimeNow = util.getDatetimeNow()

mysql.connect()

main()

mysql.disconnect()




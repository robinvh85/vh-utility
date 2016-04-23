INSERT IGNORE INTO user_rcb_daily(date, site_id, monitor, count, deposit)
SELECT DATE(time), site_id, monitor, COUNT(*) as count, SUM(deposit) as deposit 
FROM user_rcb
GROUP BY DATE(time), site_id, monitor
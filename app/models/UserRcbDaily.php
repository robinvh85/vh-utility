<?php

class UserRcbDaily extends ModelBase
{
    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'user_rcb_daily';
    }

    /**
     * Allows to query a set of records that match the specified conditions
     *
     * @param mixed $parameters
     * @return Words[]
     */
    public static function find($parameters = null)
    {
        return parent::find($parameters);
    }

    /**
     * Allows to query the first record that match the specified conditions
     *
     * @param mixed $parameters
     * @return Words
     */
    public static function findFirst($parameters = null)
    {
        return parent::findFirst($parameters);
    }
	
	public static function getListBySiteId($site_id){
        $phql = "SELECT u.date, u.count, u.deposit, u.monitor, sm.ref_site_url FROM UserRcbDaily u			
			JOIN SiteMonitors sm ON sm.monitor = u.monitor AND sm.site_id = u.site_id
			WHERE u.site_id=$site_id 
			ORDER BY u.date DESC";
			
        $list = self::getManager()->executeQuery($phql);
        return $list;
    }
	
	public static function getListTotalBySiteId($site_id){
        $phql = "SELECT date, SUM(count) as count, SUM(deposit) as deposit 
		FROM UserRcbDaily 
		WHERE site_id=$site_id
		GROUP BY date
		ORDER BY date DESC";
        
		$list = self::getManager()->executeQuery($phql);
        return $list;
    }
}

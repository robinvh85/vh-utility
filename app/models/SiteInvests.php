<?php

class SiteInvests extends ModelBase
{
    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'site_invest';
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
	
	public static function getList($site_id){
        $phql = "SELECT sm.site_id, s.url, s.is_stat, sm.monitor, sm.ref_site_url, si.id, si.acc_name, si.ip, si.amount, si.time, si.status
			FROM SiteMonitors sm
			JOIN Sites s ON s.id = sm.site_id AND s.id = $site_id
			LEFT JOIN SiteInvests si ON si.site_id = sm.site_id AND si.monitor = sm.monitor
			ORDER BY sm.ref_site_url ASC, si.time DESC";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
	
	public static function getActiveInvests(){
        $phql = "SELECT DISTINCT site_id
			FROM SiteInvests 
			WHERE status='Invest' OR status='Pending'";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
	
	public static function getAllActiveInvests(){
        $phql = "SELECT sm.site_id, s.url, s.is_stat, sm.monitor, sm.ref_site_url, si.id, si.acc_name, si.ip, si.amount, si.time, si.status
			FROM SiteInvests si
			JOIN Sites s ON s.id = si.site_id
			JOIN SiteMonitors sm ON sm.monitor = si.monitor AND sm.site_id = si.site_id
			WHERE si.status = 'Invest' OR si.status = 'Pending'";

        $list = self::getManager()->executeQuery($phql);
        return $list;
    }
	
	
}

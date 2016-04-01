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
        $phql = "SELECT sm.site_id, s.url, sm.monitor, sm.ref_site_url, si.acc_name, si.ip, si.amount, si.time
			FROM SiteMonitors sm
			JOIN Sites s ON s.id = sm.site_id AND s.id = $site_id
			LEFT JOIN SiteInvests si ON si.site_id = sm.site_id AND si.monitor = sm.monitor
			ORDER BY sm.ref_site_url ASC, si.time DESC ";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
	
}

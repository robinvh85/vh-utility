<?php

class SiteMonitors extends ModelBase
{
    public $site_id;
    public $monitor;
    public $ref_site_id;
    public $ref_site_url;	
	public $is_paid;
	public $note;

    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'site_monitor';
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
	
	public static function getList(){
        $phql = "SELECT sm.id, sm.monitor, sm.ref_site_url, sm.site_id, sm.note, s.url, s.is_scam, s.is_stat, s.start_at, s.type
			FROM SiteMonitors sm
			JOIN Sites s ON sm.site_id = s.id AND s.is_scam = 0
			ORDER BY s.start_at desc, s.id ASC";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
	
	public static function getRcbLink($monitor, $refSiteIdid){
		if($monitor == "hyipstop.com"){
			return "http://$monitor/details/aj/rcb/lid/$refSiteIdid/";
		} else {
			return "http://$monitor/rcb-$refSiteIdid.html";
		}
	}
}

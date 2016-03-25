<?php

class UnknowSites extends \Phalcon\Mvc\Model
{
    public $id;
    public $url;
    public $monitor;
    public $is_done;	

    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'unknow_sites';
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
}

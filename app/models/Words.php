<?php

class Words extends \Phalcon\Mvc\Model
{
    public $id;
    public $text;
    public $meaning;
    public $audioPath;	
	public $tags;

    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'words';
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

<?php

class Lessons extends ModelBase
{
    /**
     * Returns table name mapped in the model.
     *
     * @return string
     */
    public function getSource()
    {
        return 'talk_lessons';
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
        $phql = "
			SELECT id, name
			FROM Lessons
		";

        $list = self::getManager()->executeQuery($phql);

        return $list;
    }
}

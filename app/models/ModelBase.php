<?php

namespace Backend\Models;


class ModelBase extends \Phalcon\Mvc\Model
{
    protected static function getManager()
    {
        $di = \Phalcon\DI\FactoryDefault::getDefault();
        return $di['modelsManager'];
    }
}
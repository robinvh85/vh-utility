<?php

class IndexController extends ControllerBase
{

    public function indexAction()
    {
        
    }
	
	public function listAction()
    {
        $this->view->disable();
		
		$arr = array("id" => 1, "name" => "test");		
        echo json_encode(array("data" => $arr));
    }
}


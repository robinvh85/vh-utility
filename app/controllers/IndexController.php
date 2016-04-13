<?php

class IndexController extends ControllerBase
{

    public function indexAction()
    {
        
    }
	
	public function loginAction()
    {
		$this->view->disable();
		
        if($this->request->getQuery('name') == 'invest'){
			$this->session->set("username", "invest");
			echo "OK";
		} else
		{
			$this->response->redirect('/');
		}				
    }
	
	public function listAction()
    {
        $this->view->disable();
		
		$arr = array("id" => 1, "name" => "test");		
        echo json_encode(array("data" => $arr));
    }
}


<?php

class StatsController extends ControllerBase
{
	public function initialize()
	{
		$this->tag->setTitle("Web page");
		if(!$this->session->get("username")){
			$this->response->redirect('/');
		}
	}
	
	public function rcbAction()
    {
		$site_id = $this->request->getQuery('site_id');
		$site = Sites::findFirst($site_id);
		
		$this->view->site_id = $site_id;
		$this->view->site_url = $site->url;
    }
	
	public function listRcbAction(){
		$params = json_decode(file_get_contents('php://input'));
		$list = UserRcbDaily::getListBySiteId($params->site_id);	
		
        $this->view->disable();
        echo json_encode(array("data" => $list->toArray()));
	}
}

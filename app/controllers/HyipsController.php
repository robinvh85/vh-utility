<?php

class HyipsController extends ControllerBase
{
	public function initialize()
	{
		$this->tag->setTitle("HYIP");
	}
	
    public function indexAction()
    {
		
    }

    public function listAction()
    {
		$list = SiteMonitors::getList();	
		
        $this->view->disable();
		
        echo json_encode(array("data" => $list->toArray()));
    }

	public function listUnknowAction()
    {
		$list = UnknowSites::find("is_done = 0");	
        $this->view->disable();
        echo json_encode(array("data" => $list->toArray()));		
    }
	
	public function updateSiteAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = Sites::findFirst($params->id);
        $model->is_scam = intval($params->is_scam);
        $model->type = $params->type;
		$model->start_at = $params->start_at;
		
        if($model->save()){
            echo json_encode(array("status" => "OK"));
        } else {
            echo json_encode(array("status" => "NG"));
        }
    }
	
	public function updateUnknowSiteAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = UnknowSites::findFirst($params->id);
        $model->is_done = 1;
		
        if($model->save()){
            echo json_encode(array("status" => "OK"));
        } else {
            echo json_encode(array("status" => "NG"));
        }
    }
	
	public function updateMonitorSiteAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = SiteMonitors::findFirst($params->id);
        $model->note = $params->note;
		
        if($model->save()){
            echo json_encode(array("status" => "OK"));
        } else {
            echo json_encode(array("status" => "NG"));
        }
    }
	
    public function createAction()
    {
        $this->view->disable();
        $status = "OK";

        $params = json_decode(file_get_contents('php://input'));
		$model = Sites::findFirst("url='$params->url'");
		
		if($model == null){
			$model = new Sites();
			$model->url = $params -> url;
			$model->save();			
		}
		
		$monitorModel = new SiteMonitors();
		$monitorModel->site_id = $model->id;
		$monitorModel->monitor = $params -> monitor;
		$monitorModel->ref_site_id = $params -> ref_site_id;
		$monitorModel->ref_site_url = SiteMonitors::getRcbLink($params->monitor, $params->ref_site_id);
		
		if(!$monitorModel->save()){
			$status = "NG";
		}
		        
        echo json_encode(array("status" => $status));
    }
}

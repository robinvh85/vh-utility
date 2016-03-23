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
	
	public function updateMonitorSiteAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = MonitorSites::findFirst($params->id);
        $model->is_scam = intval($params->is_scam);
        $model->type = $params->type;
		$model->start_at = $params->start_at;
		
        if($model->save()){
            echo json_encode(array("status" => "OK"));
        } else {
            echo json_encode(array("status" => "NG"));
        }
    }
	
    public function createAction()
    {
        $this->view->disable();
        $status = "NG";

        $params = json_decode(file_get_contents('php://input'));

        $model = new Words();

        $model->text = $params -> text;
        $model->meaning = $params -> meaning;
        $model->subtitle = $params -> subtitle;
		$model->audioPath = $params -> audioPath;
		$model->tags = $params -> tags;
		
        if($model->save()) {
            $status = "OK";
        }

        echo json_encode(array("status" => $status));
    }
}

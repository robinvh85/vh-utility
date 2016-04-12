<?php

class HyipsController extends ControllerBase
{
	public function initialize()
	{
		$this->tag->setTitle("Web page");
		if(!$this->session->get("username")){
			$this->response->redirect('/');
		}
	}
	
	public function test1Action()
    {
		$this->view->disable();
		
		if($this->session->get("test"))
			echo $this->session->get("test");
		else
			echo "NG";	
    }
	
	public function test2Action()
    {
		$this->session->set("test", "test2");
		
		$this->view->disable();
		
		if($this->session->get("test"))
			echo $this->session->get("test");
		else
			echo "NG";
    }
	
    public function indexAction()
    {
		 $this->session->get("test");
    }

	public function index2Action()
    {
		$activeInvests = SiteInvests::getActiveInvests();
		$this->view->activeInvests = json_encode($activeInvests->toArray());
    }
	
	public function investAction()
    {
		$site_id = $this->request->getQuery('site_id');			
		$this->view->site_id = $site_id;
    }
	
	public function statAction()
    {
		$site_id = $this->request->getQuery('site_id');	
		
		$site = Sites::findFirst($site_id);
		
		$this->view->site_id = $site_id;
		$this->view->site_url = $site->url;
    }
	
    public function listAction()
    {
		$list = SiteMonitors::getList();	
		
        $this->view->disable();
		
        echo json_encode(array("data" => $list->toArray()));
    }

	public function list2Action()
    {
		$list = Sites::getList();	
		
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
		$model->is_stat = intval($params->is_stat);
		$model->note = $params->note;
		$model->score = $params->score;
		
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
	
	public function updateInvestAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = SiteInvests::findFirst($params->id);
        $model->status = $params->status;
		
        if($model->save()){
			if($model->status == "OK"){
				$account = Accounts::findFirst("name='$params->acc_name'");
				$account->amount += $params->amount;
				$account->save();
			}
            echo json_encode(array("status" => "OK"));
        } else {
            echo json_encode(array("status" => "NG"));
        }
    }
	
	public function deleteInvestAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = SiteInvests::findFirst($params->id);      
		
        if($model->delete()){			
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
		$monitorModel->ref_site_url = $params -> ref_site_url; //SiteMonitors::getRcbLink($params->monitor, $params->ref_site_id);
		
		if(!$monitorModel->save()){
			$status = "NG";
		}
		        
        echo json_encode(array("status" => $status));
    }
	
	public function createInvestAction()
    {
        $this->view->disable();
        $status = "NG";

        $params = json_decode(file_get_contents('php://input'));
		
		$model = new SiteInvests();
		$model->site_id = $params->site_id;
		$model->monitor = $params -> monitor;
		$model->acc_name = $params -> acc_name;
		$model->amount = $params -> amount;
		$model->ip = $params -> ip;
		$model->time = $params -> time;
		$model->status = "Invest";
		
		if($model->save()){
			$account = Accounts::findFirst("name='$params->acc_name'");
			$account->amount -= $params->amount;
			$account->save();
			
			$status = "OK";
		}
		        
        echo json_encode(array("status" => $status));
    }
	
	public function listSiteStatsAction()
    {
		$params = json_decode(file_get_contents('php://input'));
		//$list = SiteStats::find("site_id = $params->site_id");	
		
		$list = SiteStats::query()
			->where("site_id = $params->site_id");
		
		if($params->from_time > 0){
			$list->andWhere("time >= $params->from_time");
		}
		
		if($params->to_time > 0){
			$list->andWhere("time <= $params->to_time");
		}
		
		$list = $list->execute();
		
        $this->view->disable();
        echo json_encode(array("data" => $list->toArray()));		
    }
	
	public function listSiteInvestAction()
    {
		$params = json_decode(file_get_contents('php://input'));
		
		if($params->site_id){
			$list = SiteInvests::getList($params->site_id);	
		} else {
			$list = SiteInvests::getAllActiveInvests();	
		}
		
        $this->view->disable();
        echo json_encode(array("data" => $list->toArray()));		
    }
}

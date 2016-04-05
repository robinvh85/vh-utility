<?php

class AccountsController extends ControllerBase
{
	public function initialize()
	{
		$this->tag->setTitle("Info");
	}
	
    public function indexAction()
    {
		
    }
	
    public function listAction()
    {
		$list = Accounts::find();	
		
        $this->view->disable();
		
        echo json_encode(array("data" => $list->toArray()));
    }

	public function updateAction()
    {
        $this->view->disable();
		$params = json_decode(file_get_contents('php://input'));
        $model = Accounts::findFirst($params->id);    
		$model->group = $params->group;
		$model->name = $params->name;
		$model->pm = $params->pm;
		$model->email = $params->email;
		$model->amount = $params->amount;
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
		$model = Accounts::findFirst("name='$params->name'");
		
		if($model == null){
			$model = new Accounts();
			$model->group = $params -> group;
			$model->name = $params -> name;
			$model->email = $params -> email;
			$model->pm = $params -> pm;
			$model->save();			
		}
		        
        echo json_encode(array("status" => $status));
    }
}

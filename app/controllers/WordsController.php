<?php

class WordsController extends ControllerBase
{
    /**
     * Index action
     */
    public function indexAction()
    {

    }

	public function adminAction()
    {

    }
	
    public function listAction()
    {
        $list = Words::find();
        $this->view->disable();
		
        echo json_encode(array("data" => $list->toArray()));
    }

    /**
     * Creates a new categorie
     */
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

    /**
     * Saves a categorie edited
     */
	public function saveAction(){
		$this->view->disable();
		$status = "NG";
		
        $params = json_decode(file_get_contents('php://input'));
        $model = Words::findFirstByid($params -> id);
		
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

    /**
     * Deletes
     *
     * @param string $id
     */
    public function deleteAction($id)
    {
		$this->view->disable();
		$status = "NG";
        $categorie = Words::findFirstByid($id);
        
        if ($categorie->delete()) {
			$status = "OK";
        }
		
		echo json_encode(array("status" => $status));
    }
}

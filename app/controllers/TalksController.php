<?php

class TalksController extends ControllerBase
{
	public function initialize()
	{
		$this->tag->setTitle("Talks");
	}

    public function indexAction()
    {		
    }

    public function listAction()
    {
		$params = json_decode(file_get_contents('php://input'));		
		
		$lesson_id = $params -> lesson_id;
		$list = Talks::find("lesson_id='$lesson_id'");
		
        $this->view->disable();	
        echo json_encode(array("data" => $list->toArray()));
    }
	
	public function listLessonAction()
    {
		$this->view->disable();	
		$lessons = Lessons::getList();
		echo json_encode(array("data" => $lessons->toArray()));		
    }
}

import sys
import os.path
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import util
import mysql

def insertWord(obj):
	query = """
		INSERT INTO talk_words(lesson_id, file_path, text) values ({0}, "{1}", "{2}")
	""".format(obj['lesson_id'], obj['file_path'], obj['text'])
	
	id = mysql.executeInsert(query)
		
	return id
	
def getLesson():
	query = """
		SELECT *
		FROM talk_lessons		
		WHERE is_done = 0
	"""
	
	return mysql.executeQuery(query)
import sys
import os.path
from datetime import datetime
import urllib
from pyquery import PyQuery as pq
import re
import common

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lib")))
import config
import util
import mysql

def get_words(lesson_id, _url):
	print("get_words() at " + _url)
	
	d = pq(url=_url)
	list = d("a")
	obj = {}
	
	for item in list:
		href = item.get("href")
		if href.find(".mp3") > 0:				
			obj['lesson_id'] = lesson_id
			obj['text'] = item.text_content()
			obj['file_path'] = get_file(href)
			print("{0} - {1}".format(obj['text'], obj['file_path']))	
			common.insertWord(obj)

def get_file(file_url):
	file_path_local = file_url.split(".com")[1]
	file_path_local = file_path_local[1:]
	file_path = config.TALK_ENGLISH_PATH + "/" + file_path_local
	arr = file_path.split("/")
	file_name = arr[len(arr) - 1]
	directory = file_path.replace("/" + file_name, "")

	if not os.path.exists(directory):
		os.makedirs(directory)
	
	if not os.path.exists(file_path):
		urllib.urlretrieve (file_url, file_path)
		
	return file_path_local
		
def run():

	lessons = common.getLesson()
	
	for lesson in lessons:
		print(lesson[2])
		get_words(lesson[0], lesson[2])
	
#############
mysql.connect()

run()

mysql.disconnect()
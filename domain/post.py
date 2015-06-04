import json
import datetime

class Post:
	
	def __init__(self,title,content,tags,author):
		self.title = title
		self.content = content
		self.tags = tags
		self.author = author
		self.create_date = int(datetime.datetime.now().strftime("%s")) * 1000 
		self.last_modified_date = int(datetime.datetime.now().strftime("%s")) * 1000 

	def get_json_string(self):
		return json.dumps(self.__dict__)


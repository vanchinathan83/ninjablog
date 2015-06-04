import json
import datetime

class Post:
	
	def __init__(self,title,content,tags,author):
		self.title = title
		self.content = content
		self.tags = tags
		self.author = author
		self.create_date = datetime.date.today().strftime("%B %d, %Y")
		self.last_modified_date = datetime.date.today().strftime("%B %d, %Y")

	def get_json_string(self):
		return json.dumps(self.__dict__)


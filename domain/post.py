import json

class Post:
	
	def __init__(self,title,content,tags,author):
		self.title = title
		self.content = content
		self.tags = tags
		self.author = author

	def get_json_string(self):
		return json.dumps(self.__dict__)


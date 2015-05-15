import json

class Post:
	
	def __init__(self,title,content,tags,author):
		self.title = title
		self.content = content
		self.tags = tags
		self.author = author

	def get_json_string(self):
		print json.dumps(self.__dict__)
		return json.dumps(self.__dict__)


class http_status():
	
	def __init__(status_code=200,message="Success"):
		self.status_code = status_code
		self.message = message

	def __str__():
		return self.status_code + '-' + self.message
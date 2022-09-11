import happybase

class HBaseDao:
	"""
	Dao class for operation on HBase
	"""
	__instance = None

	@staticmethod
	def get_instance():
		""" Static access method. """
		if HBaseDao.__instance == None:
			HBaseDao()
		return HBaseDao.__instance

	def __init__(self):
		if HBaseDao.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			HBaseDao.__instance = self
			self.host = '184.72.87.189'
			#self.host = 'localhost'
			for i in range(2):
				try:
					self.pool = happybase.ConnectionPool(size=3, host=self.host, port=9090)
					break
				except:
					print("Exception in connecting HBase")


	def get_data(self, key, table):
		for i in range(2):
			try:
				with self.pool.connection() as connection:
					t = connection.table(table)
					row = t.row(key)
					return row
			except:
				self.reconnect()



	def write_data(self, key, row, table):
		for i in range(2):
			try:
				with self.pool.connection() as connection:
					t = connection.table(table)
					t.put(key, row)
			except:
				self.reconnect()

	def reconnect(self):
		self.pool = happybase.ConnectionPool(size=3, host=self.host)
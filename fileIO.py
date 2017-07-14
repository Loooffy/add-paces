def get_data(filename):

	with open(filename,'r',-1,'utf_8') as f:
		read_data=f.read()

	f.close()

	return read_data

def post_data(filename, data):
	
	with open(filename,'w',-1,'utf_8') as f:
		f.write(data)
		
	f.close()
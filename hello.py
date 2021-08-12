def app(env, start_response):
	status = '200 OK'
	response_headers = [
		('Content-Type', 'text/plain'), 
		('Content-Lenght', str(len(data)))
	]
	data = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	start_response(status, response_headers)
	return iter(data)
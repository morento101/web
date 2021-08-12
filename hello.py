def app(env, start_response):
	status = '200 OK'
	data = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	response_headers = [
		('Content-Type', 'text/plain'), 
		('Content-Lenght', str(len(data)))
	]
	start_response(status, response_headers)
	return iter(data)
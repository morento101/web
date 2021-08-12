def app(env, start_response):
	status = '200 OK'
	data = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
	headers = [
		('Content-Type', 'text/plain')
	]
	start_response(status, headers)
	return iter([data])
def app(environ, start_response):
  data = ""
  status = '200 OK'
  print(environ["PATH_INFO"], environ["PATH_INFO"]=="/")
  if (environ["PATH_INFO"] == "/") or (environ["PATH_INFO"] == "/index.html"):
    data = str.encode(open('./web/index.html', 'r').read())
  elif (environ["PATH_INFO"] == "/flag_m4k3r"):
    data = str.encode(open('./web/flag_m4k3r.html', 'r').read())
  elif (environ["PATH_INFO"] == "/about"):
    data = str.encode(open('./web/about.html', 'r').read())
  elif (environ["PATH_INFO"] == "/robots.txt"):
    data = str.encode(open('./web/robots.txt', 'r').read())
  else:
    status = '404 Not Found'
    data = b'page not Found!\n'
  #print(data)
  response_headers = [
    ('Content-type', 'text/html'),
    ('Content-Length', str(len(data)))
  ]
  start_response(status, response_headers)
  return iter([data])

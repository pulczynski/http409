from wsgiref.simple_server import make_server
import  random

def enterprisey_409(environ, start_response):
    status = '409 Conflict' # HTTP Status
    headers = [('Content-type', 'text/plain')] # HTTP Headers
    start_response(status, headers)

    # The returned object is going to be printed
    excuses = ["I think taht the request submited conflicts with rome rule alreadu established", 'I thnk you conflict with some rules!', 'I dont think so']
    return [random.choice(excuses).encode('utf-8')]
    
httpd = make_server('', 8000, enterprisey_409)


# Serve until process is killed
httpd.serve_forever()

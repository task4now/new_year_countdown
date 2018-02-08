#! Simple local server to show New Year countdown
import bottle
from wsgiref.simple_server import make_server
from seconds_to_new_year import seconds_to_new_year

app = application = bottle.Bottle()


@app.route('/')
def show_index():
    """Countdouw index"""
    name = seconds_to_new_year()
    return bottle.template('new_year.tpl', name=name)


@app.get('/<new_year:re:.*\.css>')
def stylesheets(new_year):
    """Get css file for template"""
    return bottle.static_file(new_year, root='static/')


@app.get('/<salut:re:.*\.jpg>')
def stylesheets(salut):
    """Get jpg file for css"""
    return bottle.static_file(salut, root='static/')


class StripPathMiddleware(object):
    """
    Get that slash out of the request
    """

    def __init__(self, a):
        self.a = a

    def __call__(self, e, h):
        e['PATH_INFO'] = e['PATH_INFO'].rstrip('/')
        return self.a(e, h)


if __name__ == '__main__':
    with make_server('', 5005, application) as httpd:
        print("Serving on port 5005...")
        httpd.serve_forever()

from livereload import Server
from fhir_amp_tutorial import app

server = Server(app.wsgi_app)
server.watch('templates/', delay=2)
server.watch('test/unit/','python -m unittest discover test/unit/')
server.serve()
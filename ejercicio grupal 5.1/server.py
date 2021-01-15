from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

TEMPLATES_DIR = "templates"

port = 8080

def render_template(file_name, data):
    with open(TEMPLATES_DIR + "/" + file_name, "r") as template_file:
        template = template_file.read()
        rendered_template = template.format_map(data)
        return rendered_template.encode("utf-8")

class ManejadorDeRequest(BaseHTTPRequestHandler):

    # manejador para los requerimientos GET
    def do_GET (self):
        if self.path == "/":
        # generamos encabezado header HTTP
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # envia mensaje HTML
            nombre_de_usuario = "Usuario"
            data = {'titulo': 'Página de inicio de: '+ nombre_de_usuario, 'texto':'hola: ' + nombre_de_usuario}
            self.wfile.write(render_template("index.html", data))

        if self.path == "/portafolio":
        # generamos encabezado header HTTP
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # envia mensaje HTML
            nombre_de_usuario = "Usuario"
            data = {'titulo': 'Página de portafolio de: '+ nombre_de_usuario, 'texto':'portafolio: ' + nombre_de_usuario}
            self.wfile.write(render_template("portafolio.html", data))

        if self.path == "/nosotros":
        # generamos encabezado header HTTP
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # envia mensaje HTML
            nombre_de_usuario = "Usuario"
            data = {'titulo': 'Página de nosotros: '+ nombre_de_usuario, 'texto':'nosotros: ' + nombre_de_usuario}
            self.wfile.write(render_template("nosotros.html", data))

server = HTTPServer(('', port), ManejadorDeRequest)
print('Comenzando servido HTTP en puerto: ', port)

# esperar request http para siempre
server.serve_forever()
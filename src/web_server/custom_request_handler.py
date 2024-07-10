import logging
from http.server import BaseHTTPRequestHandler
from urllib.parse import parse_qs


def get_file(filename):
    with open("../resources/"+filename, 'r', encoding='utf-8') as f:
        file = f.read()
    return file


class CustomRequestHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200, content_type='text/html', response_data=None):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        if response_data is not None:
            self.wfile.write(response_data.encode('utf-8'))

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        query_string = self.path.split('?')[1] if len(self.path.split('?')) > 1 else ''  # Získat řetězec dotazu
        params = parse_qs(query_string)  # Analyzovat řetězec dotazu a získat parametry GET
        for param_name, values in params.items():
            print(f"Param: {param_name}, Values: {values}")

        if self.headers.get('Accept') is None or ',' not in self.headers.get('Accept'):
            self.process_generic_request()
            return

        match self.headers.get('Accept').split(','):
            case header if 'text/html' in header:
                self.process_html_request()
            case header if 'application/json' in header:
                self._set_response(404, 'application/json', '{"error": "404 Not found"}')
            case _:
                self.process_generic_request()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    def process_html_request(self):
        filename = self.path.split('/')[1] if len(self.path.split('/')) > 1 else 'index.html'
        filename = 'index.html' if filename == '' else filename
        self._set_response(response_data=get_file(filename))

    def process_generic_request(self):
        #check if self.path contains /res/
        location = None
        if "/res/" in self.path:
            location = self.path.split("/res/")[1]

        content_type = None
        if location is not None:
            match location.split('.')[-1]:
                case 'css': content_type='text/css'
                case 'js': content_type='text/javascript'
                case 'png': content_type='image/png'
                case 'jpg': content_type='image/jpeg'
                case 'gif': content_type='image/gif'
            if content_type is not None:
                self._set_response(content_type=content_type, response_data=get_file(location))
                return

        self._set_response(404, 'application/json', '{"error": "404 Not found"}')

        #if file ends with .js set content-type to text/javascript same with css


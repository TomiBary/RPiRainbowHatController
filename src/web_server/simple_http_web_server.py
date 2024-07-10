import logging
from http.server import HTTPServer
from custom_request_handler import CustomRequestHandler


def run(server_class=HTTPServer, handler_class=CustomRequestHandler, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        print('all args ' + str(argv))
        run(port=int(argv[1]))
    else:
        run()

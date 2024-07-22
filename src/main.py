from web_server import simple_http_web_server as web_server

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        print('all args ' + str(argv))
        web_server.run(port=int(argv[1]))
    else:
        web_server.run()

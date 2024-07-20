class SimplePostHandler():
    def handle_POST(self, ):
        match self.path:
            case header if '/hydrat' in header:
                pass
            case _:
                self.process_generic_request()
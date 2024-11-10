from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 5000

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello from Docker!</h1></body></html>")

if __name__ == "__main__":
    server = HTTPServer(("", PORT), CustomHandler)
    print(f"Serving on port {PORT}")
    server.serve_forever()

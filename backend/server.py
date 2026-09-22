from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json


class Handler(BaseHTTPRequestHandler):

    def send_json(self, status, data):
        response = json.dumps(data).encode("utf-8")

        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.send_header(
            "Content-Length",
            str(len(response))
        )

        self.end_headers()

        self.wfile.write(response)


    def do_GET(self):

        if self.path == "/api/health":

            self.send_json(
                200,
                {
                    "ok": True,
                    "mode": "virtual-coins-demo"
                }
            )

        else:

            self.send_json(
                404,
                {
                    "error": "Not found"
                }
            )


server = HTTPServer(
    ("127.0.0.1", 8000),
    Handler
)


print(
    "Server running at "
    "http://127.0.0.1:8000"
)


server.serve_forever()

from http.server import BaseHTTPRequestHandler, HTTPServer
import base64

HOST = "127.0.0.1"
PORT = 8080

USERNAME = "john"
PASSWORD = "123456"


class BasicAuthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Get Authorization header
        auth_header = self.headers.get("Authorization")

        # Expected credentials
        credentials = f"{USERNAME}:{PASSWORD}"
        expected = base64.b64encode(credentials.encode()).decode()

        # Check authentication
        if auth_header != f"Basic {expected}":
            self.send_response(401)
            self.send_header(
                "WWW-Authenticate",
                'Basic realm="Admin"'
            )
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(
                b"401 Unauthorized - Authentication required"
            )
            return

        # Authentication successful
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.wfile.write(
            b"""
            <html>
                <head>
                    <title>Admin Panel</title>
                </head>
                <body>
                    <h1>Welcome to the Admin Panel!</h1>
                    <p>HTTP Basic Authentication successful.</p>
                </body>
            </html>
            """
        )


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), BasicAuthHandler)

    print(f"[+] HTTP Basic Auth Lab running at http://{HOST}:{PORT}")
    print(f"[+] Protected endpoint: http://{HOST}:{PORT}/admin")
    print(f"[+] Username: {USERNAME}")
    print(f"[+] Password: {PASSWORD}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] Server stopped.")
        server.server_close()

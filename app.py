from http.server import SimpleHTTPRequestHandler, HTTPServer
import json
import urllib.request

class Handler(SimpleHTTPRequestHandler):

    def do_POST(self):

        if self.path != "/generate":
            self.send_error(404)
            return

        length = int(self.headers["Content-Length"])
        data = json.loads(self.rfile.read(length))

        prompt = f"""
You are TouchGrass AI.

Create one safe outdoor micro-adventure.

Time: {data['time']} minutes
Energy: {data['energy']}
Place: {data['place']}

Return simple plain text only.

TITLE: short title
OBJECTIVE: one sentence
STEP 1: first action
STEP 2: second action
STEP 3: third action
LOOK FOR: something interesting to notice

No JSON. No markdown. No extra text.
"""

        payload = json.dumps({
            "model": "gemma3:1b",
            "prompt": prompt,
            "stream": False
        }).encode("utf-8")

        try:

            request = urllib.request.Request(
                "http://localhost:11434/api/generate",
                data=payload,
                headers={"Content-Type": "application/json"}
            )

            response = urllib.request.urlopen(request)
            result = json.loads(response.read())

            answer = result["response"]

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.end_headers()

            output = json.dumps(
                {"answer": answer},
                ensure_ascii=False
            )

            self.wfile.write(output.encode("utf-8"))

        except Exception as e:

            self.send_response(500)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps({"error": str(e)}).encode()
            )


server = HTTPServer(("localhost", 8000), Handler)

print("TouchGrass running at http://localhost:8000")
print("Gemma + Ollama connected.")

server.serve_forever()
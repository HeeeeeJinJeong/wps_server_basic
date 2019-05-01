"""
HTTP Server
1. 브라우저를 통해 사용자가 HTTP Request Message를 보내면
2. 서버는 그 Message를 해석하고 Response Message로 응답한다.
2-1. 어느 페이지로 접속했느냐?
2-2. Query String은 어떤 데이터를 가지고 있느냐?
2-3. 특정 스크립트 요청이 있느냐?
2-4. 최종 응답을 HTML, 다운로드는 파일로 할것이냐?
"""

# 1. HTTP Response만 하는 서버
import http.server
import socketserver

PORT = 8000 # 서버에 접속하면 포트

# 요청이 들어오면 어느 객체가 요청을 해석하고 처리할 것이냐?
Handler = http.server.SimpleHTTPRequestHandler


with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print("serving at PORT", PORT)
    httpd.serve_forever()
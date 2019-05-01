"""
CGI (common Gatewqy Interface)
- 단점 : 요청이 있을 때마다 프로세스(응용프로그램)을 새로 실행
- 장점 : 특별한 추가 프로그램 없이도 여러 언어의 스크립트 실행 가능
"""

import http.server

PORT = 8000

class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/cgi']

with http.server.HTTPServer(("",PORT), Handler) as httpd:
    print('serving at port', PORT)
    httpd.serve_forever()

# http://127.0.0.1:8000/cgi/test.py -> test.py의 결과가 출력됨
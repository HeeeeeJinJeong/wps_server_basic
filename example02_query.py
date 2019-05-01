from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse # 어떤 브라우저로 접속했는지 해석해줌

PORT = 8000

class Handler(BaseHTTPRequestHandler):
    # 검색창 만들기
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        # query_text = urlparse(self.path).query
        # print(query_text) # name=test&name2=jake
        #
        # query_vars = parse_qs(query_text)
        # print(query_vars) # {'name': ['test'], 'name2': ['jake']}

        # 1. 딕셔너리를 다룰 수 있는가?
        # 2. 변수형에 대해 인지하고 있는가?
        # 3. 연산에 대해 알고 있는가?

        # query string으로 키와 몸무게를 전달받아서
        # bmi를 계산해서 message로 출력
        query_text = urlparse(self.path).query
        print(query_text)

        query_vars = parse_qs(query_text)
        print(query_vars)

        message = ''
        form_html = """
            <form action='' method='post'>
                <label>Weight:<input type='text' name='weight'></label><br>
                <label>Height:<input type='text' name='height'></label><br>
                <input type='submit' value='Calc'>
            </form>
        """
        if 'weight' in query_vars and 'height' in query_vars:
            weight = float(query_vars['weight'][0])
            height = float(query_vars['height'][0])
            bmi = weight / ((height/100)**2)
            message += "bmi :"+str(round(bmi,2))
        message += form_html

        self.wfile.write(bytes(message, "utf-8"))
        return


    def do_POST(self):
        # 검색 결과 보여주기 - 네이버에서 크롤링
        content_length = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_length)
        queries = parse_qs(post_body.decode('utf-8'))
        print(queries)

        if 'weight' in queries and 'height' in queries:
            wei = float(queries['weight'][0])
            hei = float(queries['height'][0])
            bmi = wei / ((hei / 100) ** 2)
            message = "BMI : "+str(round(bmi,2))

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        self.wfile.write(bytes(message,"utf-8"))
        return


# 한 페이지에서 접속 Method에 따라 기능을 분기
# 회원가입 페이지 domain.com/signup/
# Get : 회원가입 양식 보여주기
# Post : 전달 받은 데이터를 처리해서 회원가입 진행하기(데이터베이스에 저장하기)

def run():
    server_address = ('127.0.0.1', PORT)
    httpd = HTTPServer(server_address, Handler)
    print("serving at PORT", PORT)
    httpd.serve_forever()

run()
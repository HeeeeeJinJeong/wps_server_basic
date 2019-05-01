import http.server
import socketserver
from io import BytesIO

import xlsxwriter
from openpyxl import Workbook
from tempfile import NamedTemporaryFile

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # flush 방식
        # output = io.BytesIO()

        # xlsxwriter로 만든 데이터를 BytesIO라는 데이터스트림으로 변환해서 출력
        """
        workbook = xlsxwriter.Workbook(output, {'in_memory':True})
        worksheet = workbook.add_worksheet()
        worksheet.write(0,0, "EXCEL TEST")
        workbook.close()
        
        output.seek(0)
        """

        # openpyxl ->
        wb = Workbook()
        with NamedTemporaryFile() as tmp:
            wb.save(tmp.name)
            output = BytesIO(tmp.read())

        self.send_response(200)
        self.send_header('Context-Disposition','attachment; filename=test.xlsx')
        self.send_header('Content-type','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        self.end_headers()
        self.wfile.write(output.read())
        return

print('serving at port', PORT)
httpd = socketserver.TCPServer(('',PORT),Handler)
httpd.serve_forever()
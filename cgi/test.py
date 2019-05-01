#!/Users/heejin/PycharmProjects/server_basic/venv/bin/python

# 권한설정 먼저! chmod ugo+x cgi/test.py
# which python -> /Users/heejin/PycharmProjects/server_basic/venv/bin/python 앞에 느낌표를 붙여서 맨 위에 작성하면
# 단독파일로 실행됨

print('Context-type: text/html\n')
print('<html><head><title>CGI TEST</title></head><body>CGI Server Testing</body></html>')
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

# namedtupleはメソッド作れないのでクラスにした
class HttpResponse:
    def __init__(self, status_code, content_type, body):
        self.status_code = status_code
        self.content_type = content_type
        self.body = body

    def header(self):
        header = {
            "Date": format_date_time(mktime(datetime.now().timetuple())),
            "Server": "SimpleHTTPServer",
            "Content-Type": self.content_type,
            "Content-Length": '33333',
            "Connection": 'Close'
        }

    def to_bytes(self):
        str_list  = [
            "HTTP/1.1 status_code",
            "",
            self.body
        ]
        str = '\n'.join(str_list).encode('utf-8')
        print(str)
        return str

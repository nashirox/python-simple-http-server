import http_response
from pathlib import Path

class RequestHandler:
    def handle(self, request):
        print("this is handler class")
        path = self.__server_path(request.path)
        with path.open() as f:
            content = f.read

        print(content)

        response = http_response.HttpResponse(
            status_code=200,
            content_type='text/html',
            body=content
        )

        print(response.to_bytes)

        return response

    def __server_path(self, request_path):
        req_path = Path('public/index.html')
        path = req_path
        # print(path)
        return path

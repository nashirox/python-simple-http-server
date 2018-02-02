from collections import namedtuple
Request = namedtuple('Request', ('method', 'path', 'http_version'))

class RequestParser:
    def parse(self, io):
        # print(io.decode('UTF-8').split('\n')[0].split(' '))
        method, path, http_version = io.decode('UTF-8').split('\n')[0].split(' ')
        request = Request(method=method, path=path, http_version=http_version)

        return request

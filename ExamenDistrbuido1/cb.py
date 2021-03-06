import tornado.ioloop
from tornado.httpclient import AsyncHTTPClient
#urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def callb():
    urls=[]
    datos = input("ingrese la cantidad de threads: ")

    for i in range(datos) :
        urls.append(raw_input("Ingrese el url: "))

    def handle_response(response):
        if response.error:
            print("Error:", response.error)
        else:
            url = response.request.url
            data = response.body
            print('{}: {} bytes: {}'.format(url, len(data), data))

    http_client = AsyncHTTPClient()
    for url in urls:
        http_client.fetch(url, handle_response)

    tornado.ioloop.IOLoop.instance().start()

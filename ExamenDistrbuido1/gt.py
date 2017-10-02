import gevent.monkey
from urllib2 import urlopen
gevent.monkey.patch_all()
#urls = ['http://www.google.com', 'http://www.yandex.ru', 'http://www.python.org']

def greent():
    urls=[]
    datos = input("ingrese la cantidad de threads: ")

    for i in range(datos) :
        urls.append(raw_input("Ingrese el url: "))


    def print_head(url):
        print('Starting {}'.format(url))
        data = urlopen(url).read()
        print('{}: {} bytes: {}'.format(url, len(data), data))

    jobs = [gevent.spawn(print_head, _url) for _url in urls]

    gevent.wait(jobs)

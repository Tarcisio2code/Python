import base64
base64.encodestring = base64.encodebytes
base64.decodestring = base64.decodebytes

from flexx import flx

class Exemplo(flx.Widget):

    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title='Flexx demonstração')
    m = a.launch()
    flx.run()
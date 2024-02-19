import wx
from pathlib import Path
from os.path import join
from cv2 import imread

root = Path.cwd()

images = join(root, "images")
imagem_desligada = "0.jpg"
imagem_ligada = "1.jpg"


class MyFrame(wx.Frame):
    def __init__(self, parent, title, width, height):
        super(MyFrame, self).__init__(parent, title=title, size=(width, height))

        # Painel para conter os elementos da interface
        panel = wx.Panel(self)

        # Adicionando uma imagem de fundo
        img = wx.Image(join(images, imagem_desligada), wx.BITMAP_TYPE_ANY)
        bmp = wx.StaticBitmap(panel, -1, wx.Bitmap(img))

        # Dimensões da imagem de fundo
        image_width = img.GetWidth()
        image_height = img.GetHeight()

        # Posicionar botões centralizados na parte inferior
        button_width = 100
        button_height = 30
        button_x = (width - button_width) // 2 
        button_y = (height - image_height - button_height) // 2 + image_height

        self.button_on = wx.Button(panel, label="Ligar", pos=(button_x, button_y), size=(button_width, button_height))
        self.button_off = wx.Button(panel, label="Desligar", pos=(button_x, button_y + button_height + 10), size=(button_width, button_height))


        # Associando eventos aos botões
        self.button_on.Bind(wx.EVT_BUTTON, self.on_button_on)
        self.button_off.Bind(wx.EVT_BUTTON, self.on_button_off)

        # Mostrando a janela
        self.Show()

    def on_button_on(self, event):
        print("Botão Ligar pressionado")
        # Adicione aqui o código para a ação de ligar

    def on_button_off(self, event):
        print("Botão Desligar pressionado")
        # Adicione aqui o código para a ação de desligar


if __name__ == "__main__":
    app = wx.App()
    #LARGURA = 1240.53
    #ALTURA = 701.96
    
    ALTURA,LARGURA = imread(join(images, imagem_desligada)).shape[0:2]
    #LARGURA,ALTURA = imread(join(images, imagem_desligada)).shape[0:2]
    print(ALTURA,LARGURA)
    
    frame = MyFrame(None, title="Minha Interface Gráfica", width=LARGURA+16, height=ALTURA+38)
    app.MainLoop()

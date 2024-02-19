import wx
from pathlib import Path
from os.path import join


root = Path.cwd()

images = join(root,"images")
imagem_desligada = "desligada.jpg"
imagem_ligada = "ligada.jpg"


class MyFrame(wx.Frame):
    def __init__(self, parent, title,wight,height):
        super(MyFrame, self).__init__(parent, title=title, size=(wight, height))
        
        # Painel para conter os elementos da interface
        panel = wx.Panel(self)
        
        # Adicionando uma imagem de fundo
        
        img = wx.Image(join(images,imagem_desligada), wx.BITMAP_TYPE_ANY)
        bmp = wx.StaticBitmap(panel, -1, wx.Bitmap(img))
        
        # Criando botões
        self.button_on = wx.Button(panel, label="Ligar", pos=(50, 200))
        self.button_off = wx.Button(panel, label="Desligar", pos=(200, 200))
        
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
    LARGURA = 1162
    #ALTURA = 705
    ALTURA = 800
    
    frame = MyFrame(None, title="Minha Interface Gráfica",wight=LARGURA,height=ALTURA)
    app.MainLoop()

import wx
from pathlib import Path
from os.path import join

root = Path.cwd()
images = join(root, "images")

#estado da coruja e do bot, Inicia desligado, quando ligado recebe True
state = False

IMAGE_OFF = join(images,"0.jpg")
IMAGE_ON = join(images,"1.jpg")
# TAMANHOS ORIGINAIS
WINDOW_WIDTH = 750 
WINDOW_HEIGHT = 376
#WINDOW_WIDTH = 1280
#WINDOW_HEIGHT = 720

MAIN_BUTTON_WIDTH = 200
MAIN_BUTTON_HEIGHT = 40

PRECISION_BUTTON_WIDTH = MAIN_BUTTON_WIDTH//3
PRECISION_BUTTON_HEIGHT =  MAIN_BUTTON_HEIGHT//2

print(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT)


class myPanel(wx.Panel):
    def __init__(self, parent):
        super(myPanel, self).__init__(parent)
        self.image_off = self.resize_image(IMAGE_OFF, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.image_on = self.resize_image(IMAGE_ON, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.buttons = []

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        image = self.image_on if state else self.image_off
        dc.DrawBitmap(image.ConvertToBitmap(), 0, 0)

        if not self.buttons:
            # Adiciona os botões se ainda não foram adicionados (ao somar um valor a largura da posição, puxamos para a direita, se subtraimos, puxamos pra esquerda, se somamos na altura, descemnos o valor e vice versa)
            button_data = [
                ("Ativar Owlyes",(WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.30), WINDOW_HEIGHT//2 - int(WINDOW_HEIGHT * 0.10)),(MAIN_BUTTON_WIDTH,MAIN_BUTTON_HEIGHT)), 
                ("Desativar Owlyes",(WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.30), WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.10)),(MAIN_BUTTON_WIDTH,MAIN_BUTTON_HEIGHT)), 
                ("Cansado",(int(WINDOW_WIDTH/2.2) - PRECISION_BUTTON_WIDTH , WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT)), 
                ("Normal",(int(WINDOW_WIDTH/1.8) - PRECISION_BUTTON_WIDTH , WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT)), 
                ("Atento",(int(WINDOW_WIDTH/1.5) - PRECISION_BUTTON_WIDTH -8, WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT))]
            print(button_data)
            
            for data in button_data:
                button = wx.Button(self, label=f"{data[0]}", pos=data[1],size=data[2])
                button.Bind(wx.EVT_BUTTON, self.switch_mode)
                button.SetBackgroundColour(wx.Colour(255, 255, 0))  # Amarelo
                self.buttons.append(button)

    def switch_mode(self, event):
        global state
        state = not state
        self.Refresh()

    def resize_image(self, image_path, new_width, new_height):
        image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
        image = image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        return image

class myFrame(wx.Frame):
    def __init__(self,parent,title):
        super(myFrame,self).__init__(parent,title=title,size=(WINDOW_WIDTH,WINDOW_HEIGHT))
        self.Panel = myPanel(self)
        
        self.SetMinClientSize((WINDOW_WIDTH,WINDOW_HEIGHT))
        self.SetMaxClientSize((WINDOW_WIDTH,WINDOW_HEIGHT))
        #self.SetMaxSize((800,600))

class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(parent=None,title="Owleyes")
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = myApp()
    app.MainLoop()

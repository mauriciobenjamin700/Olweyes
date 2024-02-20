import wx
from pathlib import Path
from os.path import join

root = Path.cwd()
images = join(root, "images")

#estado da coruja e do bot, Inicia desligado, quando ligado recebe True
state = False

#image = "images\\background\\0.jpg"
#image = "images\\background\\1.jpg"

IMAGE_OFF = join(images,"background","0.jpg")
IMAGE_ON = join(images,"background","1.jpg")


# TAMANHOS ORIGINAIS E FINAL
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
#WINDOW_WIDTH = 1280
#WINDOW_HEIGHT = 720

MAIN_BUTTON_WIDTH = 200
MAIN_BUTTON_HEIGHT = 40

PRECISION_BUTTON_WIDTH = MAIN_BUTTON_WIDTH//3
PRECISION_BUTTON_HEIGHT =  MAIN_BUTTON_HEIGHT//2



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
            # Cor do botão (amarelo)
            button_color = "#FAFF00"
        
            # Fonte do botão wx.FONTSTYLE_NORMAL, wx.FONTSTYLE_ITALIC, FONTSTYLE_SLANT
            main_button_font = wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD)
            precision_button_font = wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
            
            # Adiciona os botões se ainda não foram adicionados (ao somar um valor a largura da posição, puxamos para a direita, se subtraimos, puxamos pra esquerda, se somamos na altura, descemnos o valor e vice versa)
            button_data = [
                ("Ativar Owlyes",(WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.30), WINDOW_HEIGHT//2 - int(WINDOW_HEIGHT * 0.10)),(MAIN_BUTTON_WIDTH,MAIN_BUTTON_HEIGHT)), 
                ("Desativar Owlyes",(WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.30), WINDOW_HEIGHT//2 + int(WINDOW_HEIGHT * 0.10)),(MAIN_BUTTON_WIDTH,MAIN_BUTTON_HEIGHT)), 
                ("Cansado",(int(WINDOW_WIDTH/2.3) - PRECISION_BUTTON_WIDTH , WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT)), 
                ("Normal",(int(WINDOW_WIDTH/1.7) - PRECISION_BUTTON_WIDTH , WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT)), 
                ("Atento",(int(WINDOW_WIDTH/1.3) - PRECISION_BUTTON_WIDTH -20, WINDOW_HEIGHT - 2 * PRECISION_BUTTON_HEIGHT),(PRECISION_BUTTON_WIDTH,PRECISION_BUTTON_HEIGHT))]
            print(button_data)
            
            for id,data in enumerate(button_data):
                button = wx.Button(self, label=f"{data[0]}", pos=data[1],size=data[2])
                button.SetBackgroundColour(wx.Colour(button_color))
                
                match id:
                    case 0 | 1:
                
                        button.Bind(wx.EVT_BUTTON, self.switch_mode)
                        button.SetBackgroundColour(wx.Colour(255, 255, 0))  # Amarelo
                        button.SetFont(main_button_font)
                    
                    case 2 | 3 | 4:
                        button.Bind(wx.EVT_BUTTON, self.switch_mode)
                        button.SetBackgroundColour(wx.Colour(255, 255, 0))  # Amarelo
                        button.SetFont(precision_button_font)
                    case _:
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

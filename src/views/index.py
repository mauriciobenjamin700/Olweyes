import wx
import os.path as path
from time import sleep
from threading import Thread

#importando as funções que o "JHON" fez
from  os.path import dirname,abspath
import sys
# Obtém o diretório atual do pai do script em execução
current_dir = dirname(dirname(abspath(__file__)))
print("linha9",current_dir)
sys.path.append(current_dir)
from models import observar,aceitar_fila,hereges


class myPanel(wx.Panel):
    def __init__(self, parent,window_size,images, MAIN_BUTTON_SIZE, PRECISION_BUTTON_SIZE, colors,mode_options):
        super(myPanel, self).__init__(parent)
        self.image_off = self.resize_image(images[0], window_size[0], window_size[1])
        self.image_on = self.resize_image(images[1], window_size[0], window_size[1])
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.buttons = []
        
        self.state = False
        self.mode_options = mode_options
        self.active_mode = 5
        self.thread = None
        
        self.main_button_width = MAIN_BUTTON_SIZE[0]
        self.main_button_height = MAIN_BUTTON_SIZE[1]
        
        self.precision_button_width = PRECISION_BUTTON_SIZE[0]
        self.precision_button_height = PRECISION_BUTTON_SIZE[1]
        
        self.on_button_color = colors[0]
        self.off_button_color = colors[1]
        self.hover = colors[2]
        

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        image = self.image_on if self.state else self.image_off
        dc.DrawBitmap(image.ConvertToBitmap(), 0, 0)

        if not self.buttons:

        
            # Fonte do botão wx.FONTSTYLE_NORMAL, wx.FONTSTYLE_ITALIC, FONTSTYLE_SLANT
            font = wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
            #font_face = font.Fon
            
            # Adiciona os botões se ainda não foram adicionados (ao somar um valor a largura da posição, puxamos para a direita, se subtraimos, puxamos pra esquerda, se somamos na altura, descemnos o valor e vice versa)
            """
            button_data = [
                ("Ativar Owlyes",(window_height//2 + int(window_height * 0.30), window_height//2 - int(window_height * 0.10)),(self.main_button_width,main_button_height)), 
                ("Desativar Owlyes",(window_height//2 + int(window_height * 0.30), window_height//2 + int(window_height * 0.10)),(self.main_button_width,main_button_height)), 
                ("Cansado",(int(window_width/2.3) - precision_button_width , window_height - 2 * precision_button_height),(precision_button_width,precision_button_height)), 
                ("Normal",(int(window_width/1.7) - precision_button_width , window_height - 2 * precision_button_height),(precision_button_width,precision_button_height)), 
                ("Atento",(int(window_width/1.3) - precision_button_width -20, window_height - 2 * precision_button_height),(precision_button_width,precision_button_height))]
            print(button_data)
            """
            button_data = [
                ("Ativar Owlyes",(210, 120),(self.main_button_width,self.main_button_height)), 
                ("Desativar Owlyes",(210, 180),(self.main_button_width,self.main_button_height)), 
                ("Cansado",(202, 260),(self.precision_button_width,self.precision_button_height)), 
                ("Normal",(278 , 260),(self.precision_button_width,self.precision_button_height)), 
                ("Atento",(353, 260),(self.precision_button_width,self.precision_button_height))]
            #print(button_data)
            
            for id,data in enumerate(button_data):
    
                match id:
                    case 0:
                        button = wx.Button(self, label=f"{data[0]}", pos=data[1],size=data[2])
                        button.Bind(wx.EVT_BUTTON, self.turn_on)
                        button.Bind(wx.EVT_ENTER_WINDOW, self.on_hover)  # Evento de passagem do mouse sobre o botão
                        button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)  # Evento de saída do mouse do botão
                        button.SetBackgroundColour(wx.Colour(self.on_button_color))
                        button.SetFont(font)
                        button.SetWindowStyleFlag(wx.NO_BORDER)
                        self.buttons.append(button)
                        
                    case 1:
                        button = wx.Button(self, label=f"{data[0]}", pos=data[1],size=data[2])
                        button.Bind(wx.EVT_BUTTON, self.turn_off)
                        button.Bind(wx.EVT_ENTER_WINDOW, self.on_hover)  # Evento de passagem do mouse sobre o botão
                        button.Bind(wx.EVT_LEAVE_WINDOW, self.on_leave)  # Evento de saída do mouse do botão
                        button.SetBackgroundColour(wx.Colour(self.on_button_color))
                        button.SetFont(font)
                        button.SetWindowStyleFlag(wx.NO_BORDER)
                        self.buttons.append(button)
                        
                    case 2:
                        toggleButton = wx.ToggleButton(self,label = data[0], pos=data[1],size=data[2])
                        toggleButton.Bind(wx.EVT_TOGGLEBUTTON,self.mode)
                        toggleButton.SetBackgroundColour(wx.Colour(self.off_button_color))
                        toggleButton.SetFont(font)
                        toggleButton.SetWindowStyleFlag(wx.NO_BORDER)
                        self.buttons.append(toggleButton)
                    
                    case 3:
                        toggleButton = wx.ToggleButton(self,label = data[0], pos=data[1],size=data[2])
                        toggleButton.Bind(wx.EVT_TOGGLEBUTTON,self.mode)
                        toggleButton.SetBackgroundColour(wx.Colour(self.on_button_color))
                        toggleButton.SetFont(font)
                        toggleButton.SetWindowStyleFlag(wx.NO_BORDER)
                        self.buttons.append(toggleButton)
                        
                    case 4:
                        toggleButton = wx.ToggleButton(self,label = data[0], pos=data[1],size=data[2])
                        toggleButton.Bind(wx.EVT_TOGGLEBUTTON,self.mode)
                        toggleButton.SetBackgroundColour(wx.Colour(self.off_button_color))
                        toggleButton.SetFont(font)
                        toggleButton.SetWindowStyleFlag(wx.NO_BORDER)
                        self.buttons.append(toggleButton)
                        
                    case _:
                        #button.SetBackgroundColour(wx.Colour(255, 255, 0))  # Amarelo
                        pass
                    
                
                
    def turn_on(self,event):
        if self.state == False:
            #global thread
            self.switch_mode()
            self.buttons[0].SetBackgroundColour(wx.Colour(self.hover))
            self.buttons[1].SetBackgroundColour(wx.Colour(self.on_button_color))
            self.bot()
            #thread = Thread(target=bot)
            #thread.start()
            
            
    def turn_off(self,event):
        if self.state == True:
            #global thread
            self.switch_mode()
            self.buttons[0].SetBackgroundColour(wx.Colour(self.on_button_color))
            self.buttons[1].SetBackgroundColour(wx.Colour(self.hover))
            #thread.join()

            
    
    def mode(self,event):
        button = event.GetEventObject()
        #mode = button.GetValue()
        label = button.GetLabel()
        
        slow,normal, fast = self.buttons[2:5]
        
        
            #event.GetEventObject().SetLabel("Click to Off")
        match label:
            case "Cansado":
                slow.SetBackgroundColour(wx.Colour(self.on_button_color))
                normal.SetBackgroundColour(wx.Colour(self.off_button_color))
                fast.SetBackgroundColour(wx.Colour(self.off_button_color))
                
                self.active_mode = self.mode_options[0]
                
                slow.SetValue(True)
                normal.SetValue(True)
                fast.SetValue(True)
                
    
                
            case "Normal":
                slow.SetBackgroundColour(wx.Colour(self.off_button_color))
                normal.SetBackgroundColour(wx.Colour(self.on_button_color))
                fast.SetBackgroundColour(wx.Colour(self.off_button_color))
                
                self.active_mode = self.mode_options[1]
                
                slow.SetValue(True)
                normal.SetValue(True)
                fast.SetValue(True)
                
            case "Atento":
                slow.SetBackgroundColour(wx.Colour(self.off_button_color))
                normal.SetBackgroundColour(wx.Colour(self.off_button_color))
                fast.SetBackgroundColour(wx.Colour(self.on_button_color))
                
                self.active_mode = self.mode_options[2]
                
                slow.SetValue(True)
                normal.SetValue(True)
                fast.SetValue(True)
                
        print("Modo Atual = ",self.active_mode)
                    


    def switch_mode(self,event=None):
        self.state = not self.state
        self.Refresh()
        
    def bot(self):
        self.thread = Thread(target=self.bot_config).start()
        if self.thread:
            self.thread.join()
        
    def bot_config(self):
        while self.state == True:
            print("estou ligado")
            if(observar()):
                if(aceitar_fila()):
                    if(hereges()):
                        self.state = False
                        self.switch_mode()
            sleep(self.active_mode)
            
        print("não estou mais de olho")
        

    def resize_image(self, image_path, new_width, new_height):
        image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
        image = image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        return image
    
    def on_hover(self, event):
        button = event.GetEventObject()
        button.SetBackgroundColour(wx.Colour(self.hover))

    def on_leave(self, event):
        button = event.GetEventObject()
        button.SetBackgroundColour(wx.Colour(self.on_button_color))

class myFrame(wx.Frame):
    def __init__(self,parent,title,window_size):
        super(myFrame,self).__init__(parent,title=title,size=window_size)
        
        root = path.abspath(path.curdir)
        images = path.join(root, "images")
        #image = "images\\background\\0.jpg"
        #image = "images\\background\\1.jpg"

        image_off = path.join(images,"background","0.jpg")
        image_on = path.join(images,"background","1.jpg")
            
        IMAGES = (image_off,image_on)
        
        MAIN_BUTTON_SIZE = (200,40)
        
        PRECISION_BUTTON_SIZE = (MAIN_BUTTON_SIZE[0]//3,MAIN_BUTTON_SIZE[1]//2)
        COLORS = ("#FAFF00","#ABAE0C","#00FF00") # on button, off button, hover
        
        MODE = (10,5,3)
        
        self.Panel = myPanel(self, window_size,IMAGES, MAIN_BUTTON_SIZE, PRECISION_BUTTON_SIZE, COLORS,MODE)
        self.SetMinClientSize((window_size[0],window_size[1]))
        self.SetMaxClientSize((window_size[0],window_size[1]))
        #self.SetMaxSize((800,600))

class myApp(wx.App):
    def OnInit(self):
        self.frame = myFrame(parent=None,title="Owleyes",window_size=(600,300))
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = myApp()
    app.MainLoop()

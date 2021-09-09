import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.scrollview import ScrollView
from tkinter import messagebox

Window.clearcolor=(1,1,1,1)
fn='BAUHS93'

purple=(450/255.0,30/255.0,450/255.0,1)

with open('stocks1.memory','wb') as mem_file:
    mem_file.write(bytes())

with open('price_list.memory','w') as mem_file1:
    mem_file1.write('')

class Start(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text='CHOOSE THEME',color=purple,font_name=fn,pos=(340,300)
            ,font_size=30))

        self.light_click=Button(text='LIGHT THEME',background_color=purple,font_name=fn,
            pos=(340,200),size=(100,50))
        self.light_click.bind(on_press=self.use_light)
        self.add_widget(self.light_click)

        self.dark_click=Button(text='DARK THEME',background_color=purple,font_name=fn,pos=(340,100)
            ,size=(100,50))
        self.dark_click.bind(on_press=self.use_dark)
        self.add_widget(self.dark_click)

    def use_light(self, instance):
        Window.clearcolor=(1,1,1,1)
       #with open('stocks.memory','r') as file:
        #    nstock=file.read()'''

        try:
            with open('stocks.memory','r') as file:
                nstock=file.read()
        except:
            messagebox.showerror('ERROR','IT SEEMS YOU DONT HAVE THE MEMORY FILE FOR STOCKNAME')

        if nstock=='':

            asc.screen_manager.current='main'

        else:
            asc.main0.update(nstock)
            asc.screen_manager.current='main0'

    def use_dark(self, instance):
        Window.clearcolor=(20/255.0,20/255.0,20/255.0,1)
        #with open('stocks.memory','r') as file:
        #    nstock=file.read()'''

        try:
            with open('stocks.memory','r') as file:
                nstock=file.read()
        except:
            messagebox.showerror('ERROR','IT SEEMS YOU DONT HAVE THE MEMORY FILE FOR STOCKNAME')
        if nstock=='':

            asc.screen_manager.current='main'
        else:
            asc.main0.update(nstock)
            asc.screen_manager.current='main0'

class Main0(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.message=Label(color=purple,font_size=30,pos=(350,350),font_name=fn)
        self.add_widget(self.message)

        self.next=Button(text='OK CONTINUE',background_color=purple,font_name=fn,pos=(350,200),size=(105,50))
        self.next.bind(on_press=self.donext)
        self.add_widget(self.next)

    def donext(self, instance):
        asc.screen_manager.current='main1'

    def update(self, message):
        self.message.text=message

class Main(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='Welcome to Automated Stock Care App',color=purple,font_name=fn,pos=(350,400)
            ,font_size=25))
        self.add_widget(Label(text='Please register your stock name  below',color=purple,font_name=fn,pos=(350,350)
            ,font_size=25))

        self.add_widget(Label(text='Stock name: ',color=purple,font_name=fn,pos=(230,300),font_size=25))

        self.stock_name=TextInput(multiline=False,size=(300,50),pos=(350,300),font_name=fn)
        self.add_widget(self.stock_name)

        self.submit_click=Button(text='SUBMIT',font_name=fn,size=(100,50),pos=(350,200),background_color=purple)
        self.submit_click.bind(on_press=self.submitting)
        self.add_widget(self.submit_click)


        self.back_button=Button(text='<<-',background_color=purple,pos=(0,0),size=(50,25))
        self.back_button.bind(on_press=self.goingback)
        self.add_widget(self.back_button)

    def submitting(self,instance):
        stockname=self.stock_name.text 
        stockname=str(stockname)

        with open('stocks.memory','w') as file:
            file.write(stockname)

        asc.screen_manager.current='main1'


        #self.add_widget(Label(text='submitted',pos=(100,10)))

    def goingback(self,instance):
        asc.screen_manager.current='start'

class Main1(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='STOCK OPERATIONS',color=purple,font_name=fn,pos=(350,450)
            ,font_size=35))

        self.b1=Button(text='PRICE LIST',background_color=purple,font_name=fn,pos=(350,350),size=(200,50))
        self.b1.bind(on_press=self.gos1)
        self.add_widget(self.b1)

        self.b2=Button(text='STOCK ADMINISTRATION',background_color=purple,font_name=fn,pos=(350,250),size=(200,50))
        self.b2.bind(on_press=self.gos2)
        self.add_widget(self.b2)

        self.b3=Button(text='PERSONAL ACCOUNTS',background_color=purple,font_name=fn,pos=(350,150),size=(200,50))
        self.b3.bind(on_press=self.gos3)
        self.add_widget(self.b3)

        self.back_button=Button(text='<<-',background_color=purple,font_name=fn,size=(50,25))
        self.back_button.bind(on_press=self.goback)
        self.add_widget(self.back_button)

    def gos1(self,instance):
        asc.screen_manager.current='s1'

    def gos2(self,instance):
        asc.screen_manager.current='s2'

    def gos3(self,instance):
        asc.screen_manager.current='s3'

    def goback(self, instance):
        asc.screen_manager.current='start'

class S1(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=5

        #self.add_widget(Label(text='LIST OF GOODS THEIR QUANTITIES AND PRICES',font_size=25,font_name=fn,
         #   pos=(350,470),color=purple))
        #database and list of prices go here

        #self.back_button=Button(text='<<-',background_color=purple,font_name=fn,size=(50,25))
        #self.back_button.bind(on_press=self.goback)
        #self.add_widget(self.back_button)
        #self.add_widget(self.s)

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label(text='PRICE LIST',font_name=fn,color=purple,font_size=19))
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='PRODUCT ID',font_name=fn,color=purple,font_size=19))
        self.add_widget(Label(text='PRODUCT NAME',font_name=fn,color=purple,font_size=19))
        self.add_widget(Label(text='QTY',font_name=fn,color=purple,font_size=19))
        self.add_widget(Label(text='PRICE @ QTY',font_name=fn,color=purple,font_size=19))
        self.add_widget(Label(text='TOTAL PRICE',font_name=fn,color=purple,font_size=19))

        self.add_widget(Label(text='1',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 6M',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='2',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 8M TANZANIA',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='3',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 8M KENYA',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='4',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 10M UPANDE',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='5',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 10M PLAIN',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='6',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 12M UPANDE',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='7',font_name=fn,color=purple))
        self.add_widget(Label(text='NONDO 12M PLAIN',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='8',font_name=fn,color=purple))
        self.add_widget(Label(text='GYPSUM BOARD',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='9',font_name=fn,color=purple))
        self.add_widget(Label(text='GYPSUM POWDER',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='10',font_name=fn,color=purple))
        self.add_widget(Label(text='STICKS G10',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='11',font_name=fn,color=purple))
        self.add_widget(Label(text='STICKS G12',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='12',font_name=fn,color=purple))
        self.add_widget(Label(text='PLATER',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='13',font_name=fn,color=purple))
        self.add_widget(Label(text='MARINE BOARD',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='14',font_name=fn,color=purple))
        self.add_widget(Label(text='RED SURURU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='15',font_name=fn,color=purple))
        self.add_widget(Label(text='BLACK SURURU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='16',font_name=fn,color=purple))
        self.add_widget(Label(text='SMALL BLUE WAVU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='17',font_name=fn,color=purple))
        self.add_widget(Label(text='BIG BLUE WAVU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='18',font_name=fn,color=purple))
        self.add_widget(Label(text='SMAILL GREEN WAVU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='19',font_name=fn,color=purple))
        self.add_widget(Label(text='BIG GREEN WAVU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.add_widget(Label(text='20',font_name=fn,color=purple))
        self.add_widget(Label(text='SMALL GOLDEN WAVU',font_name=fn,color=purple))
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())






    def goback(self, instance):
        asc.screen_manager.current='main1'

class S2(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='STOCK ADMINISTRATION',color=purple,pos=(350,450),font_name=fn,font_size=20))

        self.b01=Button(text='STOCK TAKING AND EVALUATION',background_color=purple,pos=(350,350),size=(230,50),font_name=fn)
        self.b01.bind(on_press=self.gos201)
        self.add_widget(self.b01)

        self.b02=Button(text='STOCK INLET',background_color=purple,pos=(350,250),size=(230,50),font_name=fn)
        self.b02.bind(on_press=self.gos202)
        self.add_widget(self.b02)

        self.b03=Button(text='STOCK OUTLET',background_color=purple,pos=(350,150),size=(230,50),font_name=fn)
        self.b03.bind(on_press=self.gos203)
        self.add_widget(self.b03)

        self.back_button=Button(text='<<-',background_color=purple,font_name=fn,size=(50,25))
        self.back_button.bind(on_press=self.goback)
        self.add_widget(self.back_button)

    def gos201(self,instance):
        asc.screen_manager.current='s201'

    def gos202(self,instance):
        asc.screen_manager.current='s202'

    def gos203(self,instance):
        asc.screen_manager.current='s203'

    def goback(self, instance):
        asc.screen_manager.current='main1'

class S201(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='VALUE OF STOCK IS (TOTAL GOES HERE AFTER PRICE) & ITS STATUS IS STABLE',color=(0,1,0,1),font_name=fn
            ,halign='center',font_size=19,pos=(350,400)))

        self.bb=Button(text='<<-',background_color=purple,size=(50,25))
        self.bb.bind(on_press=self.gb)
        self.add_widget(self.bb)

    def gb(self,instance):
        asc.screen_manager.current='s2'


class S202(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='ADD VALUE INTO STOCK',font_name=fn,color=purple,font_size=27))
        self.add_widget(Label())

        #PRODUCT ID
        self.add_widget(Label(text='PRODUCT ID',font_name=fn,color=purple,font_size=19))
        self.pidi=TextInput(multiline=False)
        self.add_widget(self.pidi)

        #VALUE TO INCREASE
        self.add_widget(Label(text='AMOUNT TO INCREASE',font_name=fn,color=purple,font_size=19))
        self.vi=TextInput(multiline=False)
        self.add_widget(self.vi)

        self.add_widget(Label())

        self.sb=Button(text='SUBMIT',font_name=fn,background_color=purple)
        self.add_widget(self.sb)

class S203(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=2

        self.add_widget(Label(text='REDUCE VALUE FROM STOCK',font_name=fn,color=purple,font_size=27))
        self.add_widget(Label())

        #PRODUCT ID
        self.add_widget(Label(text='PRODUCT ID',font_name=fn,color=purple,font_size=19))
        self.pidi=TextInput(multiline=False)
        self.add_widget(self.pidi)

        #VALUE TO INCREASE
        self.add_widget(Label(text='AMOUNT TO DECREASE',font_name=fn,color=purple,font_size=19))
        self.vi=TextInput(multiline=False)
        self.add_widget(self.vi)

        self.add_widget(Label())

        self.sb=Button(text='SUBMIT',font_name=fn,background_color=purple)
        self.add_widget(self.sb)



class S3(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='LIST OF DEBTORS AND CREDITORS ACCOUNTS',color=purple,pos=(350,450),font_name=fn
            ,font_size=20))

        self.dc=Button(text='DEBTORS',font_name=fn,background_color=purple,pos=(350,250),size=(100,50))
        self.dc.bind(on_press=self.dca)
        self.add_widget(self.dc)

        self.cc=Button(text='CREDITORS',font_name=fn,background_color=purple,pos=(350,150),size=(100,50))
        self.cc.bind(on_press=self.cca)
        self.add_widget(self.cc)

        self.bb=Button(text='<<-',font_name=fn,background_color=purple,size=(50,25))
        self.bb.bind(on_press=self.gb)
        self.add_widget(self.bb)

    def dca(self,instance):
        asc.screen_manager.current='dr'

    def cca(self,instance):
        asc.screen_manager.current='cr'

    def gb(self,instance):
        asc.screen_manager.current='main1'

class Dr(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text='PEOPLE WHO YOU DEBT ARE:',color=purple,font_name=fn))

class Cr(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text='PEOPLE WHO OWE YOU ARE:',color=purple,font_name=fn))

class About(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        with open('about.txt','r') as file:
            about_info=file.read()

        self.add_widget(Label(text=about_info,pos=(300,300),color=purple,font_size=17))

        self.back_button=Button(text='<<-',background_color=purple,pos=(0,0),size=(100,50))
        self.back_button.bind(on_press=self.goingback)
        self.add_widget(self.back_button)

    def goingback(self,instance):
        asc.screen_manager.current='start'


class ASCApp(App):
    def build(self):
        self.screen_manager=ScreenManager()

        self.start=Start()
        screen=Screen(name='start')
        screen.add_widget(self.start)
        self.screen_manager.add_widget(screen)

        self.main=Main()
        screen=Screen(name='main')
        screen.add_widget(self.main)
        self.screen_manager.add_widget(screen)

        self.main0=Main0()
        screen=Screen(name='main0')
        screen.add_widget(self.main0)
        self.screen_manager.add_widget(screen)

        self.main1=Main1()
        screen=Screen(name='main1')
        screen.add_widget(self.main1)
        self.screen_manager.add_widget(screen)

        self.s1=S1()
        screen=Screen(name='s1')
        screen.add_widget(self.s1)
        self.screen_manager.add_widget(screen)

        self.s2=S2()
        screen=Screen(name='s2')
        screen.add_widget(self.s2)
        self.screen_manager.add_widget(screen)

        self.s201=S201()
        screen=Screen(name='s201')
        screen.add_widget(self.s201)
        self.screen_manager.add_widget(screen)

        self.s202=S202()
        screen=Screen(name='s202')
        screen.add_widget(self.s202)
        self.screen_manager.add_widget(screen)

        self.s203=S203()
        screen=Screen(name='s203')
        screen.add_widget(self.s203)
        self.screen_manager.add_widget(screen)


        self.s3=S3()
        screen=Screen(name='s3')
        screen.add_widget(self.s3)
        self.screen_manager.add_widget(screen)

        self.dr=Dr()
        screen=Screen(name='dr')
        screen.add_widget(self.dr)
        self.screen_manager.add_widget(screen)

        self.cr=Cr()
        screen=Screen(name='cr')
        screen.add_widget(self.cr)
        self.screen_manager.add_widget(screen)

        self.about=About()
        screen=Screen(name='about')
        screen.add_widget(self.about)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

        
asc=ASCApp()
asc.run()

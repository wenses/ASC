import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.textinput import TextInput

Window.clearcolor=(1,1,1,1)

purple=(450/255.0,30/255.0,450/255.0,1)

class Start(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1

        self.add_widget(Label(text='AUTOMATED STOCK CARE',font_size=35,color=purple))

        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())
        self.add_widget(Label())

        self.start_button=Button(text='ENTER',background_color=purple)
        self.start_button.bind(on_press=self.goto_enter)
        self.add_widget(self.start_button)

        self.about_button=Button(text='ABOUT & HOW TO USE',background_color=purple)
        self.about_button.bind(on_press=self.goto_about)
        self.add_widget(self.about_button)

    def goto_about(self,instance):
        asc.screen_manager.current='about'

    def goto_enter(self,instance):
        asc.screen_manager.current='main'

class Main(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #self.cols=1

        self.add_widget(Label(text='STOCK OPERATIONS',pos=(400,450),color=purple,font_size=35))

        self.b1=Button(text='PRICE LIST',background_color=purple,pos=(350,300)
                       ,size=(200,100))
        self.add_widget(self.b1)

        self.b2=Button(text='STOCK ADMINISTRATION',background_color=purple,pos=(350,200)
                       ,size=(200,100))
        self.add_widget(self.b2)

        self.b3=Button(text='PERSONAL ACCOUNTS',background_color=purple,pos=(350,100)
                       ,size=(200,100))
        self.add_widget(self.b3)

        self.back_button=Button(text='<<-',background_color=purple,pos=(0,0),size=(100,50))
        self.back_button.bind(on_press=self.goingback)
        self.add_widget(self.back_button)

    def goingback(self,instance):
        asc.screen_manager.current='start'

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

        self.about=About()
        screen=Screen(name='about')
        screen.add_widget(self.about)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

        
asc=ASCApp()
asc.run()

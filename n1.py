import kivy
from kivy.app import App 
from kivy.uix.textinput import TextInput 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen 

class Start(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1

		self.add_widget(Label(text='name:'))

		self.namein=TextInput()
		self.add_widget(self.namein)

		self.submit=Button(text='submit')
		self.submit.bind(on_press=self.submitting)
		self.add_widget(self.submit)

	def submitting(self, instance):
		name=self.namein.text 
		o.main.update(name)
		o.sm.current='main'

class Main(GridLayout):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.cols=1

		self.message=Label(halign='center')
		self.add_widget(self.message)

	def update(self, message):
		self.message.text=message

class OApp(App):
	def build(self):
		self.sm=ScreenManager()

		self.start=Start()
		screen=Screen(name='start')
		screen.add_widget(self.start)
		self.sm.add_widget(screen)

		self.main=Main()
		screen=Screen(name='main')
		screen.add_widget(self.main)
		self.sm.add_widget(screen)

		return self.sm 

o=OApp()
o.run()

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from kivy.graphics import *

class TestFloat(FloatLayout):
	def draw_canvas(self):
		with self.canvas:
			Line(points=[100,100,200,200,300,400], dash_length=50)

class LineAndDotApp(App):
	pass


if __name__ == '__main__':
	LineAndDotApp().run()


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color
from kivy.graphics import *

class TestFloat(FloatLayout):
	def draw_canvas(self):
		with self.test_button.canvas:
			Color(1,0,0)


class LineAndDotApp(App):
	pass


if __name__ == '__main__':
	LineAndDotApp().run()


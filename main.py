from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.graphics import Color
from kivy.graphics import *

import math

def dist(x1,y1, x2,y2, x3,y3):
    px = x2-x1
    py = y2-y1

    something = px*px + py*py

    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    dist = math.sqrt(dx*dx + dy*dy)

    return dist

class TestDraw(ScatterLayout):
	def __init__(self, **kwargs):
		super(TestDraw, self).__init__(**kwargs)

		self.lines = [Line(points=[100,100,200,200], dash_length=10, dash_offset=10), Line(points=[200,200,300,400], dash_length=10, dash_offset=10)] 

		self.canvas.add(Color(1,1,1))
		self.canvas.add(self.lines[0])
		self.canvas.add(self.lines[1])

	def update_line(self, touch):
		self.canvas.clear()
		for line in self.lines:
			if(dist(line.points[0], line.points[1], line.points[2], line.points[3], touch.x, touch.y) < 5.0):
				self.canvas.add(Color(0,0,1))
			else:
				self.canvas.add(Color(1,1,1))
			self.canvas.add(line)

			
	def on_touch_move(self, touch):
		self.update_line(touch)
		return super(TestDraw, self).on_touch_move(touch)

	def on_touch_up(self, touch):
		self.canvas.clear()
		self.canvas.add(Color(1,1,1))
		self.canvas.add(self.lines[0])
		self.canvas.add(self.lines[1])
		return super(TestDraw, self).on_touch_up(touch)
			

class TestFloat(FloatLayout):
	def __init__(self, **kwargs):
		super(TestFloat, self).__init__(**kwargs)

		self.test_draw = TestDraw()
		self.add_widget(self.test_draw)
		


class LineAndDotApp(App):
	pass


if __name__ == '__main__':
	LineAndDotApp().run()
	

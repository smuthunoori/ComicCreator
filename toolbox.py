__author__ = 'smuthunoori'

import kivy
kivy.require('1.7.0')

import math
from kivy.uix.togglebutton import ToggleButton
from kivy.graphics import Line
from comicwidgets import StickMan, DraggableWidget

class ToolButton(ToggleButton):
    def on_touch_down(self, touch):
        ds = self.parent.drawing_space

        #print 'ToolButton: touch_down'

        if self.state == 'down' and ds.collide_point(touch.x, touch.y):
            #print 'ToolButton: touch_down collided'

            (x,y) = ds.to_widget(touch.x, touch.y)

            self.draw(ds, x, y)

            return True
        return super(ToolButton, self).on_touch_down(touch)

    def draw(self, ds, x, y):
        pass

class ToolStickMan(ToolButton):
    def draw(self, ds, x, y):
        sm = StickMan(width=48, height=48)
        sm.center = (x,y)
        ds.add_widget(sm)

class ToolCircle(ToolButton):
    def draw(self, ds, x, y):
        pass

class ToolLine(ToolButton):
    def draw(self, ds, x, y):
        pass

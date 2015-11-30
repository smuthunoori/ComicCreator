__author__ = 'smuthunoori'

import kivy
kivy.require('1.7.0')

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty


class GeneralOptions(BoxLayout):
    group_mode = False
    translation = ListProperty(None)

    def clear(self, instance):
        self.drawing_space.clear_widgets()

    def remove(self, instance):
        if self.drawing_space.children:
            self.drawing_space.remove_widget(self.drawing_space.children[0])

    def group(self, instance, value):
        if value == 'down':
            self.group_mode = True
        else:
            self.group_mode = False
            self.unselectall()

    def color(self, instance):
        pass

    def gestures(self, instance, value):
        pass

    def unselectall(self):
        for child in self.drawing_space.children:
            child.unselect()

    def on_translation(self, instance, value):
        for child in self.drawing_space.children:
            if child.selected:
                child.translate(*self.translation)

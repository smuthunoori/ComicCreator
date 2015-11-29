__author__ = 'smuthunoori'

import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.interactive import InteractiveLauncher

Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('comicwidgets.kv')
Builder.load_file('generaloptions.kv')
Builder.load_file('statusbar.kv')

class ComicCreator(AnchorLayout):
    pass

class ComicCreatorApp(App):
    def build(self):
        self.title = 'My Comic Creator'
        return ComicCreator()

if __name__ == '__main__':
    ComicCreatorApp().run()



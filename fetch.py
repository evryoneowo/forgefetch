# fetch class

import renderer
import textutils

class Fetch:
    def __init__(self, accent, secondary, reset):
        self.data = {}

        self.accent = accent
        self.secondary = secondary
        self.reset = reset

        self.tart = ''

    def add(self, name, value):
        self.data[name] = value
    
    def art(self, text):
        self.tart = text
    
    def print(self, indentmain=2, indentart=2):
        rdata = renderer.renderer(self.data, indentmain, accent=self.accent, secondary=self.secondary, reset=self.reset)

        if self.tart:
            rdata = textutils.connecttext(self.tart, rdata, indentart)
        
        print(rdata)
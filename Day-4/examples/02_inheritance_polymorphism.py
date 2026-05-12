# Inheritance and polymorphism: base component and specialized components
class BaseComponent:
    def __init__(self, name):
        self._name = name  # encapsulated attribute

    def click(self):
        print(self._name + ' clicked (base)')

class Button(BaseComponent):
    def click(self):
        print(self._name + ' button clicked (Button override)')

class Link(BaseComponent):
    def click(self):
        print(self._name + ' link followed (Link override)')

components = [Button('Save'), Link('Home')]
for c in components:
    c.click()

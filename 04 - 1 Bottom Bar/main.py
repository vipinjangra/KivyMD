from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (300, 400)

VC = """
MDBoxLayout:
    MDBottomAppBar:
            
        MDToolbar:
            title: "vipin coding"
            icon: "android"
            type: "bottom"
            left_action_items: [["menu", lambda x: x]]
            mode: "free-end"
"""

class Test (MDApp):
    def build(self):
        return Builder.load_string(VC)

Test().run()

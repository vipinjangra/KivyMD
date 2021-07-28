from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
ScrollView:
    
    MDList:
        
        OneLineAvatarIconListItem:
            text: "This is our first list item"
            on_release: print("You have clicked 1st item")
            
            IconLeftWidget:
                icon:"android"
        OneLineAvatarIconListItem:
            text: "This is our second list item"
            on_release: print("You have clicked 2nd item")
            
            IconLeftWidget:
                icon:"android"
    
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
ScrollView:
    
    MDList:
        
        TwoLineAvatarIconListItem:
            text: "This is our first list item"
            secondary_text: "Subtitle 1"
            on_release: print("You have clicked 1st item")
            
            IconLeftWidget:
                icon:"android"
        TwoLineAvatarIconListItem:
            text: "This is our second list item"
            secondary_text: "Subtitle 2"
            on_release: print("You have clicked 2nd item")
            
            IconLeftWidget:
                icon:"facebook"
    
"""


class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MainApp().run()

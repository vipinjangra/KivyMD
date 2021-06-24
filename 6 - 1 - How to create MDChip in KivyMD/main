from kivy.lang import Builder
from kivymd.app import MDApp

# your layouts
KV = '''
MDBoxLayout:
    pos_hint: {'center_y': 1, 'center_x':1}  
    
    MDChip:
        text: 'vipin coding'
        icon: 'coffee'
       
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

Test().run()

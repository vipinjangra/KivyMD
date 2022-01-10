from kivy.lang import Builder
from kivymd.app import MDApp

VC = '''
MDBoxLayout:
    orientation: "vertical"
    
    MDToolbar:
        title: "vipin channel"
        elevation: 10
        left_action_items: [["menu", lambda x: app.callback()]]
        right_action_items: [["dots-vertical", lambda x: app.callback_1()], ["android", lambda x: app.callback_2()]]
        md_bg_color: app.theme_cls.accent_color
    
    MDLabel:
        text: "vipin coding videos"
        halign: "center"
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(VC)

Test().run()

from kivymd.app import MDApp
from kivy.lang import Builder
import kivymd_extensions.akivymd
from helper import KV

class vipin(MDApp):

    def build(self):
        return Builder.load_string(KV)

vipin().run()

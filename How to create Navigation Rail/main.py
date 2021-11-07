from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
#:import get_color_from_hex kivy.utils.get_color_from_hex

<MyTile@SmartTileWithStar>
    size_hint_y: None
    height: "240dp"

MDBoxLayout:
    orientation: "vertical"

    MDToolbar:
        title: "vipin coding"
        md_bg_color: rail.md_bg_color


    MDBoxLayout:

        MDNavigationRail:
            id: rail
            md_bg_color: get_color_from_hex("#3b5998")
            color_normal: get_color_from_hex("#8b9dc3")
            color_active: get_color_from_hex("#dfe3ee")
            
            
            MDNavigationRailItem:
                icon: "language-cpp"
                text: "C++"
    
            MDNavigationRailItem:
                icon: "language-python"
                text: "Python"
    
            MDNavigationRailItem:
                icon: "language-java"
                text: "Java"

        MDBoxLayout:
            padding: "24dp"
            
            ScrollView:
                
                MDList:
                    id: box
                    cols: 3
                    spacing: "12dp"

'''

class vipincoding(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        for i in range(9):
            tile = Factory.MyTile(source="https://1.bp.blogspot.com/-o1D3jrH0o5M/YUcziu4T_RI/AAAAAAAAO1Q/Ep4Zw8n-HVgCjmNpA8NbV40bGBejxzP_ACLcBGAsYHQ/w320-h320/vipincodinglogo.jpg")
            tile.stars = 5
            self.root.ids.box.add_widget(tile)

vipincoding().run()

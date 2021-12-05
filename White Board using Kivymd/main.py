from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color
from kivy.uix.button import Button


class DrawInput(Widget):

    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            Color(1, 0, 0)
            touch.ud["Line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        print(touch)
        touch.ud["Line"].points += (touch.x, touch.y)

    def on_touch_up(self, touch):
        print("Left", touch)


class vipincanvas(MDApp):

    def build(self):
        parent = Widget()
        self.painter = DrawInput()
        eraser = Button(text='Erase', background_color =(5, 1, 1, 1))
        eraser.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(eraser)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == "__main__":
    vipincanvas().run()

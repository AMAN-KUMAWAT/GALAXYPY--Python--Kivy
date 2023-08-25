from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout

class MenuWidget(RelativeLayout):
    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(RelativeLayout, self).on_touch_down(touch)

    pass

```.py
# recipe_GUI

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class IntroScreen(MDScreen):
    pass


class PrepareDough(MDScreen):
    pass


class PrebakeDough(MDScreen):
    pass


class recipe(MDApp):
    def build(self):
        return


my_app = recipe()
my_app.run()
```
```.kv
# recipe.kv

ScreenManager:
    id: screen_manager

    IntroScreen:
        name: "IntroScreen"

    Ingredients:
        name: "Ingredients"

    Wash:
        name: "Wash"

    Cut:
        name: "Cut"

<IntroScreen>:

    MDCard:
        size_hint: .7, .7
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: 0.4, 0.4, 0, 0.5
        orientation: "vertical"

        MDLabel:
            text: "Pizza Tutorial"
            font_style: "H5"
            halign: "center"
            size_hint: 1, .1

        FitImage:
            size_hint: 1, .3
            source: "pizza.jpg"
            radius: 36, 36, 0, 0

        MDRectangleFlatButton:
            text: "Next step"
            on_press: root.parent.current = "PrepareDough"
            pos_hint: {'center_x': .5}

<PrepareDough>:

    MDCard:
        size_hint: .7, .7
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: 0.4, 0.4, 0, 0.5
        orientation: "vertical"

        MDLabel:
            text: "Pizza Tutorial"
            font_style: "H5"
            halign: "center"
            size_hint: 1, .1

        FitImage:
            size_hint: 1, .3
            source: "pizza.jpg"
            radius: 36, 36, 0, 0

        MDBoxLayout:
            size_hint: 1, .1
            MDRectangleFlatButton:
                size_hint: .5, 1
                text: "Previous step"
                on_press:
                    root.parent.transition.direction = 'left'
                    root.parent.current = "IntroScreen"

                pos_hint: {'center_x': .5}

            MDRectangleFlatButton:
                size_hint: .5, 1
                text: "Next step"
                on_press: root.parent.current = "PrebakeDough"
                pos_hint: {'center_x': .5}

<PrebakeDough>:

    MDCard:
        size_hint: .7, .7
        pos_hint: {'center_x': .5, 'center_y': .5}
        md_bg_color: 0.4, 0.4, 0, 0.5
        orientation: "vertical"

        MDLabel:
            text: "Prebake Dough"
            font_style: "H5"
            halign: "center"
            size_hint: 1, .1

        FitImage:
            size_hint: 1, .3
            source: "pizza.jpg"
            radius: 36, 36, 0, 0

        MDRectangleFlatButton:
            text: "Previous step"
            on_press:
                root.parent.transition.direction = 'left'
                root.parent.current = "PrepareDough"
            pos_hint: {'center_x': .5}
```

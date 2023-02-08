![image](https://user-images.githubusercontent.com/111758436/217506306-6fdec8ba-bb9d-48b1-a55c-f6ef8e960dda.png)

## Code
```.py
# demo_counter.py

from kivymd.app import MDApp

class layout_demo(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def set_counter(self):
        # validate that it is a digit
        user_start = int(self.root.ids.user_start_x.text)
        self.count = user_start
        self.root.ids.counter_label.text = f"x={self.count}"


    def change(self, name: str):
        if 'up' in name:
            self.count += 1
        else:
            self.count -= 1
        self.root.ids.counter_label.text = f"x={self.count}"

demo_class = layout_demo()
demo_class.run()
```
```.kv
# layout_demo.kv

Screen:
    size: 500, 500

    MDBoxLayout:
        id: main_box
        orientation: "vertical"
        size_hint: 1, .5
        md_bg_color: "#2993f0"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: user_start_x
            hint_text: "Enter a number"
            hint_text_size: "36dp"
            mode: "round"
            size_hint: .25, 1
            pos_hint: {"center_x": .5}
            on_text: app.set_counter()
            font_size: "36dp"

        MDBoxLayout:
            id: second_box
            orientation: "horizontal"
            md_bg_color: "#e63946"

            MDLabel:
                id: counter_label
                font_style: "H3"
                halign: "center"

            MDBoxLayout:
                id: third_box
                orientation: "vertical"

                MDRaisedButton:
                    id: up_btn
                    text: "+1"
                    on_press: app.change("up")
                    size_hint: 1, 1

                MDRaisedButton:
                    id: dow_btn
                    text: "-1"
                    on_press: app.change("down")
                    size_hint: 1, 1
```

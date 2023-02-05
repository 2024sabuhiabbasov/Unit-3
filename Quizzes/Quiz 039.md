# Quiz 039

![image](https://user-images.githubusercontent.com/111758436/216805994-19112e2a-49c0-4865-8532-351c28360a85.png)

## My codes

### Python
```.py
# Program for Quiz 039

from kivymd.app import MDApp


class counter(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0

    def build(self):
        return

    def change(self):
        self.count += 1
        print(self.count)
        self.root.ids.counter_label.text = f"{self.count}"


demo_class = counter()
demo_class.run()
```
### KivyMD
```.kv
# counter.kv

Screen:
    size: 500, 500

    MDBoxLayout:
        id: main_box
        orientation: "horizontal"
        size_hint: .7, .3
        md_bg_color: "#FFFFFF"
        pos_hint: {"center_x": .5, "center_y": .5}


        MDLabel:
            id: counter_label
            size_hint: .5, 1
            font_size: 34
            halign: "center"
            md_bg_color: "#658864"
            text_color: 0, 0, 1, 1

        MDRaisedButton:
            id: add_btn
            size_hint: .5, 1
            text: "Add +1"
            font_size: 34
            md_bg_color: "#B7B78A"
            text_color: "#DDDDDD"
            on_press: app.change()
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/216806893-d2bec13f-151f-4364-b3e9-dba0aee487fc.png)

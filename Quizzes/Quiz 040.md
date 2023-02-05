# Quiz 040

![image](https://user-images.githubusercontent.com/111758436/216806960-62075295-7202-4579-841f-d35a624c9e40.png)

## My codes

### Python
```.py
# Program for Quiz 039

from kivymd.app import MDApp


class theming(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        return

    def change_mode(self):
        print(self.root.ids.main.md_bg_color)
        if self.root.ids.main.md_bg_color == [1.0, 1.0, 1.0, 1.0]:
            self.root.ids.main.md_bg_color = "#000000"
            self.root.ids.theme_mode.text_color = 1, 1, 1, 1
            self.root.ids.my_name.text_color = 1, 1, 1, 1
            self.root.ids.theme_mode.text = "LIGHT"
            self.root.ids.theme_mode.md_bg_color = "#B7B78A"
        else:
            self.root.ids.main.md_bg_color = "#FFFFFF"
            self.root.ids.theme_mode.text_color = 0, 0, 0, 1
            self.root.ids.my_name.text_color = 0, 0, 0, 1
            self.root.ids.theme_mode.text = "DARK"
            self.root.ids.theme_mode.md_bg_color = "#658864"


quiz40 = theming()
quiz40.run()
```
### KivyMD
```.kv
# theming.kv
Screen:
    size:500,500
    MDBoxLayout:
        id: main
        orientation:"vertical"
        md_bg_color: "#FFFFFF"
        MDLabel:
            id:my_name
            text: "Sabuhi Abbasov"
            halign: "center"
            font_style: "H2"
            theme_text_color: "Custom"
            text_color: 0, 0, 0, 1
            pos_hint: {"center_x": .5, "center_y": .5}
        MDRaisedButton:
            id: theme_mode
            text: "Dark Mode"
            md_bg_color: "B7B78A"
            pos_hint: {"center_x": 0.05, "center_y": 0.1}
            on_release: app.change_mode()
```
### Proof
![image](https://user-images.githubusercontent.com/111758436/216807664-8aa3978e-b6a9-4eae-9b59-3bf98f1967de.png)
![image](https://user-images.githubusercontent.com/111758436/216807669-66aaf755-dc94-4438-b574-ac8881015ed1.png)

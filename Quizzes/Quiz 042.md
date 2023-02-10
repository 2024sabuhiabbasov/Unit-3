# Quiz 042

![image](https://user-images.githubusercontent.com/111758436/217976443-8e60d6d5-1098-4c6d-953b-57d344ff57df.png)

## My codes

### Python
```.py
# Program for quiz 042

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

class MysteryPageA(MDScreen):
    pass

class MysteryPageB(MDScreen):
    pass

class quiz042(MDApp):
    def build(self):
        return
test = quiz042()
test.run()
```
### KivyMD
```.kv
# kv for Quiz 042
ScreenManager:
    id: mystery
    MysteryPageA:
        name: "MysteryPageA"

    MysteryPageB:
        name: "MysteryPageB"

<MysteryPageA>
    size: 500,500
    md_bg_color: "#3c362a"

    MDLabel:
        text: "This is a mystery page A you pressed the button"
        font_style: "H3"
        halign: "center"
        color: "#e8f7ee"

        MDRaisedButton:
            text: "Next page"
            on_press: root.parent.current = "MysteryPageB"
            size_hint: .3, .5
            md_bg_color: "#352208"

<MysteryPageB>
    size: 500,500
    md_bg_color: "#e8f7ee"

    MDLabel:
        text: "This is a mystery page B you pressed the button"
        font_style: "H3"
        halign: "center"
        color: "#3c362a"

        MDRaisedButton:
            text: "Previous page"
            on_press: root.parent.current = "MysteryPageA"
            size_hint: .3, .5
            md_bg_color: "#352208"
```
### Proof
![image](https://github.com/2024sabuhiabbasov/Unit-3/blob/main/Other/quiz_042.gif)

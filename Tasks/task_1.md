# Task 1

![image](https://user-images.githubusercontent.com/111758436/215520789-f6dc1db1-af8d-4004-bff4-24d8c184a794.png)

## My solutions
### My code
**Python code**
```.py
# Program for Task 1 - currency converter: AZN to USD, JPY

from kivymd.app import MDApp


class converter(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input = 0

    def build(self):
        return

    def set_amount(self):
        if not self.root.ids.input_amount.text.isdigit():
            self.root.ids.show_converted_amount.text = "Please enter a valid number"
        number = int(self.root.ids.input_amount.text)
        self.input = number

    def convert_to_usd(self):
        self.exchanged_result = round(self.input * 0.59, 2)
        self.root.ids.show_converted_amount.text = f" {self.exchanged_result} USD"

    def convert_to_jpy(self):
        self.exchanged_result = round(self.input * 76.66, 2)
        self.root.ids.show_converted_amount.text = f" {self.exchanged_result} JPY"


result = converter()
result.run()
```

**KV**
```.kv
# .kv file for task_1 - currency converter

Screen:
    size: 500,500
    MDBoxLayout:
        id: main
        orientation: 'vertical'
        size_hint: 1,.8
        pos_hint: {'center_x': .5, 'center_y': .5}

        MDLabel:
            text:"Currency Converter"
            halign: 'center'
            font_style: 'H3'
            size_hint: 1, .2
            pos_hint: {'center_x': .5}

        MDTextField:
            id: input_amount
            hint_text: "Enter Amount to convert from AZN"
            pos_hint: {'center_x':0.5}
            size_hint: .7, .2
            on_text: app.set_amount()

        MDBoxLayout:
            id: exchange_and_results
            orientation: 'horizontal'
            size_hint: 1, .4
            pos_hint: {'center_x':0.5}

            MDLabel:
                id : hint
                text: "CLICK TO CONVERT"
                halign: 'center'
                size_hint: .3, 1
                pos_hint: {'center_x':0.2, 'center_y':0.5}
            MDBoxLayout:
                id: buttons_and_result
                orientation:"vertical"
                size_hint: .3, 1
                MDBoxLayout:
                    id: buttons_box
                    orientation: "horizontal"
                    size_hint: .7, 1
                    pos_hint: {'center_x':0.7, 'center_y':0.9}
                    MDRaisedButton:
                        id: usd
                        text: "USD"
                        pos_hint: {"center_x": 0.25, "center_y": .25}
                        on_release: app.convert_to_usd()
                        md_bg_color:"#002B41"
                    MDRaisedButton:
                        id: jpn
                        text: "JPY"
                        pos_hint: {"center_x": 0.75, "center_y": .25}
                        on_release: app.convert_to_jpy()
                        md_bg_color:"#F20021"
                MDLabel:
                    id: show_converted_amount
                    text: "0"
                    halign: 'center'
                    font_style: 'H5'
                    text_color: "#000000"
                    size_hint: .3, 1
                    pos_hint: {'center_x':0.6}
                    font_size: 20
```

## Proofs
![image](https://user-images.githubusercontent.com/111758436/215521616-4d4fe961-b3b5-489a-ab91-f74ff5b14007.png)
![image](https://user-images.githubusercontent.com/111758436/215521678-e19b7b71-b4c2-4e8a-8496-0e47a9232ebe.png)

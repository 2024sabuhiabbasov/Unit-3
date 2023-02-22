# Quiz 041

![image](https://user-images.githubusercontent.com/111758436/220294831-3082502f-4ba1-4d8b-982f-2f2217d2cebe.png)

## My codes

### Python
```.py
# Program for Quiz 041

from kivymd.app import MDApp
class tictactoe(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.values = [0,0,0,0,0,0,0,0,0]
        self.player = "X"

        # "0" means empty
        # "1" means X
        # "2" means O

    def build(self):
        return

    def button_press(self,button_id):
        print(button_id)
        current_player = self.player
        temp = "self.root.ids.button" + button_id
        current_button = eval(temp)
        #current_button.disabled = True
        if self.values[int(button_id)-1] == 0:
            current_button.text = current_player
            if current_player == "X":
                self.player = "O"
                current_button.md_bg_color = "#94163a"
                self.values[int(button_id)-1] = 1
            else:
                self.player = "X"
                current_button.md_bg_color = "black"
                self.values[int(button_id)-1] = 2


        print(self.values)

        win_combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6)]

        for indices in win_combs:
            if all(self.values[i] == self.values[indices[0]] and self.values[i] != 0 for i in indices):
                print(f"Winner is {current_player}")
                self.root.ids.label2.text = f"Winner is {current_player}"
                break
        else:
            print("No Winner Yet")
            self.root.ids.label2.text = f"Current Player: {self.player}"

    def reset(self):
        self.values = [0,0,0,0,0,0,0,0,0]
        self.player = "X"
        for i in range(1,10):
            temp = "self.root.ids.button" + str(i)
            current_button = eval(temp)
            current_button.text = ""
            current_button.md_bg_color = "#0e576e"
            #current_button.disabled = False
        self.root.ids.label2.text = f"Current Player: {self.player}"


result = tictactoe()
result.run()
```
### KV
```.kv
MDScreen:
    id : screen
    size:500,500
    md_bg_color: "black"
    MDBoxLayout:
        id: main_box
        size_hint: .8, .8
        orientation: 'vertical'
        pos_hint: {'center_x': .5, 'center_y': .5}
        MDBoxLayout:
            id: box1
            size_hint: 1, .2
            orientation: 'vertical'
            MDLabel:
                id: label1
                text: 'Tic Tac Toe by Sabu'
                halign: 'center'
                font_style: 'H4'
                color: "white"
            MDLabel:
                id: label2
                text: "Current Player:" + app.player
                halign: 'center'
                font_size: 24
                color: "white"

        MDBoxLayout:
            id: box2
            size_hint: 1, .8
            orientation: 'vertical'
            pos_hint: {'center_x': .5, 'center_y': .5}
            MDBoxLayout:
                id: layerone
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button1
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("1")
                MDRaisedButton:
                    id: button2
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("2")
                MDRaisedButton:
                    id: button3
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("3")
            MDBoxLayout:
                id: layertwo
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button4
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("4")
                MDRaisedButton:
                    id: button5
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("5")
                MDRaisedButton:
                    id: button6
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("6")

            MDBoxLayout:
                id: layerthree
                size_hint:1,.33
                orientation:"horizontal"
                MDRaisedButton:
                    id: button7
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("7")
                MDRaisedButton:
                    id: button8
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("8")
                MDRaisedButton:
                    id: button9
                    text: ""
                    size_hint: .33, 1
                    md_bg_color: "#0e576e"
                    on_release: app.button_press("9")

        MDLabel:
            text: ""
            size_hint: 1, .07

        MDBoxLayout:
            id: resetbox
            size_hint: 1, .09
            orientation: 'vertical'
            MDRectangleFlatButton:
                id: resetbutton
                text: "Reset"
                size_hint: .1, .1
                line_color: "#0e576e"
                text_color: "#0e576e"
                pos_hint: {'center_x': .5, 'center_y': .5}
                on_release: app.reset()
```
### Proof
![quiz041](https://user-images.githubusercontent.com/111758436/220589026-26e2fc06-29c2-476a-a924-d6739e9e1068.gif)

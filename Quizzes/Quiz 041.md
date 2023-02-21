# Quiz 040

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
### Proof

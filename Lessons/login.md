```.py
# login.py

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):

    def try_login(self):
        print("User is trying to login")

    def try_register(self):
        print("User trying registration")
        self.parent.current = "SignupScreen"


class SignupScreen(MDScreen):
    def try_cancel(self):
        self.parent.current = "LoginScreen"

    def try_register(self):
        passwd1 = self.ids.e_passwd
        passwd2 = self.ids.c_passwd
        if passwd1 != passwd2:
            self.ids.e_passwd.error = True
            self.ids.c_passwd.error = True



class login(MDApp):
    def build(self):
        return
test = login()
test.run()
```
```.kv
# login.kv

ScreenManager:
    LoginScreen:
        name: "LoginScreen"

    SignupScreen:
        name: "SignupScreen"


<LoginScreen>:
    size: 500, 500
    FitImage:
        source: "pizza.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#EEE9DA"

        MDLabel:
            text: "Login"
            font_size: 24
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: uname
            hint_text: "Enter your username or email"
            icon_left: "email"

        MDTextField:
            id: passwd
            hint_text: "Enter your password"
            icon_left: "key"
            password: True

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: login
                text: "Login"
                on_press: root.try_login()
                size_hint: .3, .4
                md_bg_color: "#BDCDD6"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: signup
                text: "Signup"
                on_press: root.try_register()
                size_hint: .3, .4
                md_bg_color: "#93BFCF"

<SignupScreen>:
    size: 500, 500
    FitImage:
        source: "pizza.jpg"

    MDCard:
        size_hint: .5, .9
        elevation: 2
        orientation: "vertical"
        pos_hint: {"center_x": .5, "center_y": .5}
        padding: dp(50)
        md_bg_color: "#EEE9DA"

        MDLabel:
            text: "Signup"
            font_size: 24
            size_hint: 1, .2
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}

        MDTextField:
            id: uname
            hint_text: "Enter username"
            icon_left: "account"

        MDTextField:
            id: email
            hint_text: "Enter your email"
            icon_left: "email"

        MDTextField:
            id: e_passwd
            hint_text: "Enter password"
            icon_left: "key"
            password: True

        MDTextField:
            id: c_passwd
            hint_text: "Confirm password"
            icon_left: "key"
            password: True

            helper_text_mode: "on_error"
            helper_text: "Passwords don't match"

        MDBoxLayout:
            orientation: "horizontal"
            size_hint: 1, .1

            MDRaisedButton:
                id: signup_signup
                text: "Cancel"
                on_press: root.try_cancel()
                size_hint: .3, .65
                md_bg_color: "#93BFCF"

            MDLabel:
                size_hint: .3, 1

            MDRaisedButton:
                id: signup
                text: "Submit"
                on_press: root.try_register()
                size_hint: .3, .65
                md_bg_color: "#BDCDD6"
```

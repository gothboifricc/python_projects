from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob, random
from datetime import datetime
from pathlib import Path
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
#from kivy.core.audio import SoundLoader
#from kivy.uix.label import Label

Builder.load_file('mydesign.kv')

class LoginScreen(Screen):
    def register(self):
        self.manager.transition.direction = 'left'
        self.manager.current = "register_screen"
    def secondaryscreenpopup(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "secondary_screen"
        else:
            self.ids.invalid.text = "Wrong username or password, please try again or click on register now."
class RegisterScreen(Screen):
    def reg(self,uname,pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {'username': uname, 'password': pword,
        'created on': datetime.now().strftime("%Y-%m-%d %H-%M-%S")}
        
        with open("users.json", 'w') as file:
            json.dump(users, file)
        self.manager.transition.direction = 'left'
        self.manager.current = "sign_up_success_screen"
class SecondaryScreen(Screen):
    def returntologin2(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"       

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")
        available_feelings = [Path(filename).stem 
                                for filename in available_feelings]
        if feel in available_feelings:

            #CORRECTION HERE ARDIT WRONG

            with open(f"quotes/{feel}.txt", encoding="utf-8") as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Please try a similar feeling"

class ImageButton( ButtonBehavior, HoverBehavior, Image ):
    pass

class SignUpSuccess(Screen):
    def returntologin(self):

        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"
class RootWidget(ScreenManager):
    pass
class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    MainApp().run()

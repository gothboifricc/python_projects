from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout 
from kivy.core.audio import SoundLoader 
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition 
  
class Tester(BoxLayout): 
    def __init__(self, **kwargs): 
        super().__init__(**kwargs) 
  
    def play_sound(self): 
        sound = SoundLoader.load('lofii.wav') 
        if sound: 
            sound.play() 
  
class SampleApp(App): 
  
    def build(self): 
        return Tester() 
  
myApp = SampleApp() 
myApp.run() 
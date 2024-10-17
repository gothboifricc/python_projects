from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
 
 
 
#our main window class 
class MusicWindow(App):
 
    def build(self):
        
        #load the mp3 music 
        music = SoundLoader.load('testt.mp3')
 
        #check the exisitence of the music 
        if music:
            music.play()
            loop=True
 
        return Label(text = "Music is playing")
 
 
 
 
 
if __name__ == "__main__":
    window = MusicWindow()
    window.run()
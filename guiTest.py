from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import random

class Country_Guessing_Game(App):

    def build(self):

        

        def Change_flag(list, current_country):
            x = random.randint(0, len(list)-1)
            current_country = list[x]
            return current_country

        countries = ["japan.jpg", "usa.jpg", "canada.jpg"]
        self.countries = countries
        current_country = ""
        
        self.window = GridLayout()
        self.window.cols = 1


        self.window.add_widget(Label(text="Country Guessing Game"))

        current_country = Change_flag(countries, current_country)


        self.image = Image(source=current_country)
        self.window.add_widget(self.image)

        self.guess = TextInput(text="What is that country? \"Remove this entire phrase before submitting!\"")
        self.window.add_widget(self.guess)

        self.button = Button(text="Submit")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        self.answer = Label(text="Enter your Guess!")
        self.window.add_widget(self.answer)



        return self.window
    
    def callback(self, instance):
        x = self.image.source.removesuffix(".jpg")
        if(self.guess.text.lower() == x.lower()):
            self.answer.text = "Correct!"
            self.image.source = self.Change_flag(self.countries, self.image.source)
        else: 
            self.answer.text = "Wrong, Try Again!"

    def Change_flag(self, list, current_country):
 
        x = random.randint(0, len(list)-1)
        return list[x]

if __name__ == "__main__":
    Country_Guessing_Game().run()

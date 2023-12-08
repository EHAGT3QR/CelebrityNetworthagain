from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader

celebrity_data = {
    "Taylor Swift": {
        "net_worth": "$400 million",
        "fact": "Taylor Swift is a Grammy-winning singer-songwriter known for hits like 'Love Story' and 'Shake It Off.'",
    },
    "Dwayne Johnson": {
        "net_worth": "$320 million",
        "fact": "Dwayne Johnson, also known as 'The Rock,' is a former professional wrestler turned actor and producer.",
    },
    "Oprah Winfrey": {
        "net_worth": "$2.7 billion",
        "fact": "Oprah Winfrey is a media mogul, talk show host, and philanthropist.",
    },
    "Kylie Jenner": {
        "net_worth": "$700 million",
        "fact": "Kylie Jenner is a reality TV personality, businesswoman, and founder of Kylie Cosmetics.",
    },
    "LeBron James": {
        "net_worth": "$500 million",
        "fact": "LeBron James is a professional basketball player and considered one of the greatest in NBA history.",
    },
    "Elon Musk": {
        "net_worth": "$297 billion",
        "fact": "Elon Musk is a billionaire entrepreneur known for founding Tesla, SpaceX, and other ventures.",
    },
    "Beyoncé": {
        "net_worth": "$440 million",
        "fact": "Beyoncé is a global icon and Grammy-winning artist known for her contributions to music and entertainment.",
    },
    "Cristiano Ronaldo": {
        "net_worth": "$500 million",
        "fact": "Cristiano Ronaldo is a professional footballer widely considered one of the greatest of all time.",
    },
    "Kim Kardashian": {
        "net_worth": "$1.4 billion",
        "fact": "Kim Kardashian is a reality TV star, businesswoman, and social media influencer.",
    },
    "George Clooney": {
        "net_worth": "$500 million",
        "fact": "George Clooney is an Academy Award-winning actor, producer, and director.",
    },
    "Kanye West": {
        "net_worth": "$1.8 billion",
        "fact": "Kanye West is a rapper, fashion designer, and entrepreneur known for his influential music career.",
    },
    "Ellen DeGeneres": {
        "net_worth": "$370 million",
        "fact": "Ellen DeGeneres is a comedian, actress, and TV host known for 'The Ellen DeGeneres Show.'",
    },
    "Brad Pitt": {
        "net_worth": "$300 million",
        "fact": "Brad Pitt is an Academy Award-winning actor and film producer.",
    },
    "Jennifer Aniston": {
        "net_worth": "$300 million",
        "fact": "Jennifer Aniston is an actress best known for her role as Rachel Green on 'Friends.'",
    },
    "Leonardo DiCaprio": {
        "net_worth": "$260 million",
        "fact": "Leonardo DiCaprio is an Academy Award-winning actor and environmental activist.",
    },
    "Tom Hanks": {
        "net_worth": "$350 million",
        "fact": "Tom Hanks is an acclaimed actor known for roles in films like 'Forrest Gump' and 'Toy Story.'",
    },
    "Will Smith": {
        "net_worth": "$350 million",
        "fact": "Will Smith is a versatile actor and rapper known for his roles in 'Men in Black' and 'The Pursuit of Happyness.'",
    },
    "Meryl Streep": {
        "net_worth": "$160 million",
        "fact": "Meryl Streep is an Academy Award-winning actress widely regarded as one of the greatest actors of her generation.",
    },
    "Johnny Depp": {
        "net_worth": "$200 million",
        "fact": "Johnny Depp is an actor known for his diverse roles in films like 'Pirates of the Caribbean' and 'Edward Scissorhands.'",
    },
    "Lady Gaga": {
        "net_worth": "$320 million",
        "fact": "Lady Gaga is a Grammy and Academy Award-winning artist known for her music and acting career.",
    },
    "Lionel Messi": {
        "net_worth": "$600 million",
        "fact": "Lionel Messi is an Argentine professional footballer widely regarded as one of the greatest football players in history.",
    },
    "Sans": {
        "net_worth": "$100 trillion",
        "fact": "Sans is a famous actor in the video game 'Undertale,' known for his laid-back attitude and love of puns. He won the Tumblr's Sexy Man Award in 2021.",
    },
    "Adele": {
        "net_worth": "$190 million",
        "fact": "Adele is a Grammy-winning singer known for her powerful vocals and hit songs like 'Hello' and 'Rolling in the Deep.'",
    },
    "Chris Hemsworth": {
        "net_worth": "$130 million",
        "fact": "Chris Hemsworth is an Australian actor best known for his role as Thor in the Marvel Cinematic Universe.",
    },
    "Emma Watson": {
        "net_worth": "$80 million",
        "fact": "Emma Watson is a British actress, activist, and UN Women Goodwill Ambassador, known for her role as Hermione Granger in the 'Harry Potter' series.",
    },
    "Tom Cruise": {
        "net_worth": "$570 million",
        "fact": "Tom Cruise is an American actor and producer, known for his roles in blockbuster films like 'Top Gun' and the 'Mission: Impossible' series.",
    },
    "Scarlett Johansson": {
        "net_worth": "$165 million",
        "fact": "Scarlett Johansson is an actress and singer, widely regarded as one of Hollywood's highest-paid actresses.",
    },
    "Chris Pratt": {
        "net_worth": "$60 million",
        "fact": "Chris Pratt is an American actor known for his roles in 'Guardians of the Galaxy' and 'Jurassic World.'",
    },
    "Keanu Reeves": {
        "net_worth": "$380 million",
        "fact": "Keanu Reeves is a Canadian actor, producer, and musician, known for his roles in 'The Matrix' trilogy and 'John Wick' series.",
    },
    "Jennifer Lawrence": {
        "net_worth": "$130 million",
        "fact": "Jennifer Lawrence is an Oscar-winning actress, known for her performances in 'The Hunger Games' and 'Silver Linings Playbook.'",
    },
}


class TitleScreen(BoxLayout):
    def __init__(self, start_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 20

        sound = SoundLoader.load('C:/Users/Mohammed.s1_wsa/PycharmProjects/CelebrityNetworth/New folder (9)/onlymp3.to - Undertale OST sans. Extended-N1-RyLUQUrA-192k-1700809270.mp3')

        title_label = Label(text="Celebrity Net Worth App", font_size=40, color=(1, 0.5, 0.5, 1))
        image = Image(source='C:/Users/Mohammed.s1_wsa/PycharmProjects/CelebrityNetworth/New folder (9)/download.png')
        start_button = Button(
            text="Start",
            on_press=lambda x: self.play_sound(sound, start_callback),
            background_color=(1, 0.5, 0.5, 1),
            size_hint=(None, None),
            size=(200, 50)
        )

        self.add_widget(title_label)
        self.add_widget(image)
        self.add_widget(start_button)

    def play_sound(self, sound, callback):
        if sound:
            sound.play()
        callback()

class CelebrityNetWorthApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_text = None
        self.result_label = None
        self.title_screen = TitleScreen(start_callback=self.switch_to_main)
        self.main_layout = None

    def build(self):
        return self.title_screen

    def switch_to_main(self):
        self.main_layout = BoxLayout(orientation='vertical')
        label = Label(text="Enter the name of the celebrity:")
        input_text = TextInput(multiline=False)
        result_label = Label(text="")

        input_text.bind(on_text_validate=self.on_enter)

        self.main_layout.add_widget(label)
        self.main_layout.add_widget(input_text)
        self.main_layout.add_widget(result_label)

        self.root.clear_widgets()
        self.root.add_widget(self.main_layout)

    def on_enter(self, instance):
        celebrity_name = instance.text.strip()
        celebrity_info = celebrity_data.get(celebrity_name, {"net_worth": "Net worth information not found.",
                                                             "fact": "No additional information available."})

        if celebrity_name.lower() == "gaster":
            App.get_running_app().stop()  # Shut down the app for Gaster

        net_worth = celebrity_info["net_worth"]
        fact = celebrity_info["fact"]

        result_text = f"{celebrity_name}'s net worth is {net_worth}.\n\nFact: {fact}"
        self.main_layout.children[-1].text = result_text
        instance.text = ""
        instance.focus = True

if __name__ == "__main__":
    CelebrityNetWorthApp().run()
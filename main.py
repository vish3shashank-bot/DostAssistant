from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Mobile jaisa look dene ke liye (Optional)
Window.clearcolor = (0.1, 0.1, 0.1, 1) 

class AssistantUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 10

        # 1. Header
        self.add_widget(Label(
            text="Dost Assistant", 
            size_hint_y=0.1, 
            font_size='24sp',
            bold=True,
            color=(0, 0.7, 1, 1)
        ))

        # 2. Chat History (Scroll Hone Wala Area)
        self.scroll = ScrollView(size_hint_y=0.7)
        self.chat_history = Label(
            text="Assistant: Hello! Main aapki kya madad kar sakta hoon?\n",
            size_hint_y=None,
            valign='top',
            halign='left',
            padding=(10, 10),
            color=(1, 1, 1, 1)
        )
        self.chat_history.bind(size=self.update_text_width)
        self.scroll.add_widget(self.chat_history)
        self.add_widget(self.scroll)

        # 3. Input Area (Text box aur Button)
        input_area = BoxLayout(size_hint_y=0.2, spacing=10)
        self.user_input = TextInput(
            hint_text="Yahan likhein...",
            multiline=False,
            background_color=(0.2, 0.2, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0.7, 1, 1)
        )
        send_btn = Button(
            text="Bhejein",
            size_hint_x=0.3,
            background_normal='',
            background_color=(0, 0.5, 0.8, 1)
        )
        send_btn.bind(on_press=self.process_message)
        
        input_area.add_widget(self.user_input)
        input_area.add_widget(send_btn)
        self.add_widget(input_area)

    def update_text_width(self, *args):
        self.chat_history.text_size = (self.chat_history.width, None)
        self.chat_history.height = self.chat_history.texture_size[1]

    def process_message(self, instance):
        msg = self.user_input.text.strip()
        if msg:
            # User ka message add karein
            self.chat_history.text += f"\nAap: {msg}"
            
            # Assistant ka simple logic (Aap ise baad mein AI se connect kar sakte hain)
            response = "Assistant: Maaf kijiye, abhi main seekh raha hoon!"
            if "hello" in msg.lower():
                response = "Assistant: Namaste! Kaise hain aap?"
            elif "kaise ho" in msg.lower():
                response = "Assistant: Main ekdum mast hoon, shukriya!"
            
            self.chat_history.text += f"\n{response}\n"
            self.user_input.text = "" # Input saaf karein
            
class MyApp(App):
    def build(self):
        return AssistantUI()

if __name__ == "__main__":
    MyApp().run()

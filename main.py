import random
import json

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle


food_list = [
    "tavuk çorbası, baget tavuk kızartma, pilav",
    "tarhana çorbası, mantı",
    "balık çorbası, hamsi, makarna",
    "balık çorbası, döner",
    "tarhana çorbası, Urfa köfte, pilav",
    "mercimek çorbası, Urfa ızgara lavaş, soğan, sumak",
    "mercimek çorbası, kıymalı makarna, brokoli haşlama",
    "mercimek çorbası, Brüksel lahana haşlama",
    "köfte, makarna, zeytinyağlı kereviz",
    "kemik suyuna çorba, suluköfte, makarna, zeytinyağlı kereviz",
    "kıymalı pırasa, erişte",
    "Tarhana çorbası, kuzu sote, pilav",
    "Balık, kuzu sote, pilav",
    "Kısır",
    "Et suyu çorba, lahana dolması",
    "Brokoli çorbası",
    "Brokoli çorbası sütlü, karışık et ızgara, pilav",
    "Tarhana çorbası, suluköfte, makarna",
    "Tavuk suyuna çorba, fırında patatesli tavuk, pilav",
    "Mercimek çorbası, ızgara köfte, makarna",
    "Mercimek çorbası, tavuk sote, pilav",
    "Mantı",
    "İşkembe çorbası, bamya, pilav",
    "Köfte, makarna",
    "Köz patlıcan, kıyma, makarna",
    "Yeşil mercimek, makarna",
    "ızgara köfte, kızarmış patates, salata",
    "Tarhana çorbası, karnabahar, makarna",
    "Urfa, kuzu şiş, bulgur pilavı",
    "Tarhana çorbası, bezelye, beyaz pilav",
    "Domates çorbası, İzmir köfte, makarna",
    "Tavuk suyu çorba, piliç haşlama, pilav",
    "Tavuk suyu çorba, mantarlı tavuk sote, pilav",
    "Et suyuna çorba, kuzu etli nohut, pilav",
    "Yeşil mercimek, erişte",
    "Izgara köfte, makarna",
    "Brokoli çorbası, fırında köfte patates, pilav",
    "Brokoli çorbası, kızarmış piliç, fırında köfte patates, pilav",
    "Kabak çorbası, bamya, pilav",
    "Kabak çorbası, pirzola, antrikot",
    "Mercimek çorbası, pirzola, antrikot",
    "Pazı çorbası, pazı dolması, biber dolması",
    "Domates çorbası, taze fasulye, pilav",
    "Kırmızı mercimek çorba, fırında köfte, makarna",
    "İşkembe çorbası, Urfa şiş, bulgur pilavı",
    "Tarhana çorbası, bulgur pilavı",
    "Sac tava",
    "Et suyuna çorba, parça etli nohut, pilav",
    "Köfte, patates kızartması, kabak patlıcan kızartma",
    "Tavuk kanat, incik ızgara, makarna",
    "Kıymalı pırasa, makarna",
    "Ton Balıklı salata, zeytin, makarna"
]


def save_foods():
    with open("food_data.json", "w", encoding="utf-8") as file:
        json.dump(food_list, file, ensure_ascii=False, indent=4)


def load_foods():
    global food_list

    try:
        with open("food_data.json", "r", encoding="utf-8") as file:
            food_list = json.load(file)
    except FileNotFoundError:
        save_foods()


def add_background(layout, color):
    with layout.canvas.before:
        Color(*color)

        rectangle = Rectangle(
            pos=layout.pos,
            size=layout.size
        )

        layout.bind(
            pos=lambda instance, value:
            setattr(rectangle, "pos", value)
        )

        layout.bind(
            size=lambda instance, value:
            setattr(rectangle, "size", value)
        )


# ================= ANA EKRAN =================

class MainScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=35,
            spacing=18
        )

        add_background(layout, (0.055, 0.065, 0.09, 1))

        title = Label(
            text="YEMEK MENÜSÜ",
            font_size=32,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.18
        )

        layout.add_widget(title)

        menu_button = Button(
            text="MENÜ",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.05, 0.45, 0.22, 1)
        )
        menu_button.bind(on_press=self.open_menu)

        add_button = Button(
            text="EKLE",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.05, 0.30, 0.65, 1)
        )
        add_button.bind(on_press=self.open_add)

        show_button = Button(
            text="GÖSTER",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.75, 0.38, 0.05, 1)
        )
        show_button.bind(on_press=self.open_show)

        delete_button = Button(
            text="SİL",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.65, 0.08, 0.08, 1)
        )
        delete_button.bind(on_press=self.open_delete)

        layout.add_widget(menu_button)
        layout.add_widget(add_button)
        layout.add_widget(show_button)
        layout.add_widget(delete_button)

        self.add_widget(layout)

    def open_menu(self, instance):
        self.manager.current = "menu"

    def open_add(self, instance):
        self.manager.current = "add"

    def open_show(self, instance):
        self.manager.current = "show"

    def open_delete(self, instance):
        self.manager.current = "delete"


# ================= MENÜ EKRANI =================

class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=35,
            spacing=25
        )

        add_background(layout, (0.07, 0.08, 0.12, 1))

        title = Label(
            text="BUGÜN NE YİYELİM?",
            font_size=28,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.15
        )

        self.food_label = Label(
            text="",
            font_size=24,
            bold=True,
            color=(1, 1, 1, 1),
            halign="center",
            valign="middle"
        )

        self.food_label.bind(
            size=lambda instance, value:
            setattr(instance, "text_size", value)
        )

        new_menu_button = Button(
            text="YENİ MENÜ",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.40, 0.15, 0.65, 1),
            size_hint_y=0.22
        )
        new_menu_button.bind(on_press=self.choose_food)

        back_button = Button(
            text="GERİ",
            font_size=20,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.20, 0.21, 0.25, 1),
            size_hint_y=0.18
        )
        back_button.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(self.food_label)
        layout.add_widget(new_menu_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_enter(self):
        self.choose_food()

    def choose_food(self, instance=None):
        if food_list:
            self.food_label.text = random.choice(food_list)
        else:
            self.food_label.text = "Henüz yemek eklenmemiş."

    def go_back(self, instance):
        self.manager.current = "main"


# ================= EKLE EKRANI =================

class AddScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=35,
            spacing=20
        )

        add_background(layout, (0.055, 0.075, 0.12, 1))

        title = Label(
            text="YENİ YEMEK EKLE",
            font_size=28,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.18
        )

        self.input_box = TextInput(
            hint_text="Yemek menüsünü yaz...",
            font_size=20,
            multiline=False,
            size_hint_y=0.25
        )

        add_button = Button(
            text="EKLE",
            font_size=23,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.05, 0.30, 0.65, 1),
            size_hint_y=0.22
        )
        add_button.bind(on_press=self.add_food)

        back_button = Button(
            text="GERİ",
            font_size=20,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.20, 0.21, 0.25, 1),
            size_hint_y=0.18
        )
        back_button.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(self.input_box)
        layout.add_widget(add_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def add_food(self, instance):
        food = self.input_box.text.strip()

        if food:
            food_list.append(food)
            save_foods()

            self.input_box.text = ""
            self.input_box.hint_text = "Yemek eklendi!"

    def go_back(self, instance):
        self.manager.current = "main"


# ================= GÖSTER EKRANI =================

class ShowScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        add_background(layout, (0.06, 0.08, 0.07, 1))

        title = Label(
            text="YEMEK LİSTESİ",
            font_size=28,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.12
        )

        self.list_label = Label(
            text="",
            font_size=18,
            color=(1, 1, 1, 1),
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.list_label.bind(
            texture_size=self.update_label_height
        )

        scroll = ScrollView()
        scroll.add_widget(self.list_label)

        back_button = Button(
            text="GERİ",
            font_size=20,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.20, 0.21, 0.25, 1),
            size_hint_y=0.15
        )
        back_button.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(scroll)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_label_height(self, instance, value):
        self.list_label.height = value[1]

    def on_enter(self):
        text = ""

        for i, food in enumerate(food_list, start=1):
            text += f"{i}. {food}\n\n"

        if not text:
            text = "Henüz yemek yok."

        self.list_label.text = text

    def go_back(self, instance):
        self.manager.current = "main"


# ================= SİL EKRANI =================

class DeleteScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        add_background(layout, (0.10, 0.06, 0.07, 1))

        title = Label(
            text="YEMEK SİL",
            font_size=28,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint_y=0.12
        )

        self.list_label = Label(
            text="",
            font_size=18,
            color=(1, 1, 1, 1),
            halign="left",
            valign="top",
            size_hint_y=None
        )

        self.list_label.bind(
            texture_size=self.update_label_height
        )

        scroll = ScrollView()
        scroll.add_widget(self.list_label)

        self.input_box = TextInput(
            hint_text="Silmek istediğin yemek numarası",
            input_filter="int",
            font_size=19,
            multiline=False,
            size_hint_y=0.15
        )

        delete_button = Button(
            text="SİL",
            font_size=22,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.65, 0.08, 0.08, 1),
            size_hint_y=0.2
        )
        delete_button.bind(on_press=self.delete_food)

        back_button = Button(
            text="GERİ",
            font_size=20,
            bold=True,
            color=(1, 1, 1, 1),
            background_color=(0.20, 0.21, 0.25, 1),
            size_hint_y=0.15
        )
        back_button.bind(on_press=self.go_back)

        layout.add_widget(title)
        layout.add_widget(scroll)
        layout.add_widget(self.input_box)
        layout.add_widget(delete_button)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_label_height(self, instance, value):
        self.list_label.height = value[1]

    def on_enter(self):
        self.update_list()

    def update_list(self):
        text = ""

        for i, food in enumerate(food_list, start=1):
            text += f"{i}. {food}\n\n"

        if not text:
            text = "Henüz yemek yok."

        self.list_label.text = text

    def delete_food(self, instance):
        try:
            number = int(self.input_box.text)

            if 1 <= number <= len(food_list):
                food_list.pop(number - 1)
                save_foods()

                self.input_box.text = ""
                self.update_list()

        except ValueError:
            pass

    def go_back(self, instance):
        self.manager.current = "main"


# ================= UYGULAMA =================

class FoodApp(App):

    def build(self):
        load_foods()

        screen_manager = ScreenManager()

        screen_manager.add_widget(
            MainScreen(name="main")
        )

        screen_manager.add_widget(
            MenuScreen(name="menu")
        )

        screen_manager.add_widget(
            AddScreen(name="add")
        )

        screen_manager.add_widget(
            ShowScreen(name="show")
        )

        screen_manager.add_widget(
            DeleteScreen(name="delete")
        )

        return screen_manager


FoodApp().run()
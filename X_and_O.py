from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from X_and_O_back import *
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

Window.clearcolor = (1, 0, 0, 1)


turn = ["X", "O"]
key_logger = []
with open('ids.txt', 'r') as f:
    button_ids = [num.strip() for num in f.readlines()]


class Controller(BoxLayout):
    def exit_code(self):
        App.get_running_app().stop()

    def touched_down(self, number, id):

        def restart():
            clear_board()
            key_logger.clear()
            turn.clear()
            turn.append("X")
            turn.append("O")
            for button_id in button_ids:
                button_changes = self.ids[button_id]
                button_changes.text = ""

        if number not in key_logger:
            key_logger.append(number)

            button_change = self.ids[button_ids[id]]
            button_change.text = turn[0]
            button_change.font_size = 70

            game = main(number, turn[0])

            if game == 1:
                layout = BoxLayout(center_x=True, center_y=True, height="10dp", orientation="vertical")
                buttons = GridLayout()

                popupLabel = Label(text=f"{turn[0]} is the winner", font_size=70)

                win_size = Window.size

                closeButton = Button(text='Quit', size=(300, 100), pos=(win_size[0]*0.5625, win_size[1]*0.3333), on_release=self.exit_code)
                restartButton = Button(text="Play Again", pos=(win_size[0]*0.0625, win_size[1]*0.33333), size=(300, 100), on_release= lambda *args: restart(), on_press=lambda *args: popup.dismiss())

                layout.add_widget(popupLabel)

                buttons.add_widget(closeButton)
                buttons.add_widget(restartButton)

                layout.add_widget(buttons)

                popup = Popup(title="Gameover", content=layout, height="10dp")
                popup.open()


            elif game == 0:
                print("Game was a draw")
                layout = BoxLayout(center_x=True, center_y=True, height="10dp", orientation="vertical")
                buttons = GridLayout()

                popupLabel = Label(text="Game was a draw", font_size=70)

                win_size = Window.size

                closeButton = Button(text='Quit', size=(300, 100), pos=(win_size[0] * 0.5625, win_size[1] * 0.3333),
                                     on_release=self.exit_code)
                restartButton = Button(text="Play Again", pos=(win_size[0] * 0.0625, win_size[1] * 0.33333),
                                       size=(300, 100), on_release=lambda *args: restart(),
                                       on_press=lambda *args: popup.dismiss())

                layout.add_widget(popupLabel)

                buttons.add_widget(closeButton)
                buttons.add_widget(restartButton)

                layout.add_widget(buttons)

                popup = Popup(title="Gameover", content=layout, height="10dp")
                popup.open()

            turn[0], turn[1] = turn[1], turn[0]
        else:

            print("Already selected")


class BehindApp(App):

    def build(self):
        return Controller()


BehindApp().run()

import tkinter as tk
from .bingo import BingoCage
from .translations import translations


class BingoGUI:
    def __init__(self, geometry='1650x1050', lang='en'):
        self._lang = lang
        self._bingo_cage = BingoCage()
        self.root = tk.Tk()
        self.root.title(translations[self._lang]['title'])
        self.root.geometry(geometry)
        self.shown_numbers = tk.Label(self.root, font=('Monospace', 50), wraplength=1000, justify="center")
        self.shown_numbers.pack(padx=20, pady=20)
        self.next_button = tk.Button(
            self.root,
            text=translations[self._lang]['next_button'],
            font=('Monospace', 40),
            command=self.show_next_number,
            width=10,
        )
        self.next_button.pack(side='left', expand=True)
        self.restart_button = tk.Button(
            self.root,
            text=translations[self._lang]['restart_button'],
            font=('Monospace', 40),
            command=self.restart,
            width=10,
        )
        self.change_lang_button = tk.Button(
            self.root,
            text=translations[self._lang]['lang_name'],
            font=('Monospace', 40),
            command=self.change_lang,
            width=10,
        )
        self.change_lang_button.pack(side='left', expand=True)
        self.restart_button.pack(side='right', expand=True)
        self.root.mainloop()

    def show_next_number(self):
        self._bingo_cage.pick()
        self.shown_numbers.config(text='  '.join(self._bingo_cage._match_numbers))

    def restart(self):
        self.shown_numbers.config(text='')
        self._bingo_cage = BingoCage()

    def change_lang(self):
        self._lang = 'ua' if self._lang == 'en' else 'en'
        self.root.title(translations[self._lang]['title'])
        self.change_lang_button.config(text=translations[self._lang]['lang_name'])
        self.next_button.config(text=translations[self._lang]['next_button'])
        self.restart_button.config(text=translations[self._lang]['restart_button'])

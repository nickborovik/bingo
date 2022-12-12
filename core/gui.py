import tkinter as tk
from core.bingo import BingoCage


class BingoGUI:
    def __init__(self, geometry='1650x1050'):
        self._bingo_cage = BingoCage()
        self.root = tk.Tk()
        self.root.title('Bingo Game')
        self.root.geometry(geometry)
        self.numbers = tk.Label(self.root, font=('Monospace', 50), wraplength=1000, justify="center")
        self.numbers.pack(padx=20, pady=20)
        self.next_button = tk.Button(
            self.root,
            text='Next',
            font=('Monospace', 40),
            command=self.show_next_number,
            width=10,
        )
        self.next_button.pack(side='left', expand=True)
        self.restart_button = tk.Button(
            self.root,
            text='Reset',
            font=('Monospace', 40),
            command=self.restart,
            width=10,
        )
        self.restart_button.pack(side='right', expand=True)
        self.root.mainloop()

    def show_next_number(self):
        self._bingo_cage.pick()
        self.numbers.config(text='  '.join(self._bingo_cage._match_numbers))

    def restart(self):
        self.numbers.config(text='')
        self._bingo_cage = BingoCage()

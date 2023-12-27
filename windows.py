from tkinter import *


class Window:
    def __init__(
        self, width, height, title="MyWindow", resizable=(True, True), icon=None
    ):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        self.root.config(background="#747474")
        if icon:
            self.root.iconbitmap(icon)

    def DrawWidgets(self):
        Button(
            self.root,
            text="Сотрудники",
            font="Georgia 14",
            width=30,
            relief=RAISED,
            bg="#b4b4b4",
            bd=5,
        ).pack(anchor="w", padx=10, pady=10)
        Button(
            self.root,
            text="График работы",
            font="Georgia 14",
            width=30,
            relief=RAISED,
            bg="#b4b4b4",
            bd=5,
        ).pack(anchor="w", padx=10, pady=10)
        Button(
            self.root,
            text="Бронирования",
            font="Georgia 14",
            width=30,
            relief=RAISED,
            bg="#b4b4b4",
            bd=5,
        ).pack(anchor="w", padx=10, pady=10)
        Button(
            self.root,
            text="Финансы",
            font="Georgia 14",
            width=30,
            relief=RAISED,
            bg="#b4b4b4",
            bd=5,
        ).pack(anchor="w", padx=10, pady=10)
        Button(
            self.root,
            text="Сформировать отчет",
            font="Georgia 14",
            width=30,
            relief=RAISED,
            bg="#b4b4b4",
            bd=5,
        ).pack(anchor="w", padx=10, pady=10)
        Button(
            self.root,
            text="Настройки",
            font="Georgia 14",
            relief=GROOVE,
            bg="#b4b4b4",
            bd=3,
        ).place(relx=0.85, y=10)

    def run(self):
        self.DrawWidgets()
        self.root.mainloop()


if __name__ == "__main__":
    window = Window(950, 600, "Tkinter")
    window.run()

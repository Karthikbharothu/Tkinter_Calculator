import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PremiumCalculator(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Premium Calculator")
        self.geometry("360x520")
        self.resizable(False, False)

        self.expression = ""

        # Display
        self.display = ctk.CTkEntry(
            self,
            font=("Segoe UI", 28),
            justify="right",
            height=60
        )
        self.display.pack(padx=20, pady=20, fill="x")

        # Button frame
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Buttons layout
        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", "√"]
        ]

        # Create buttons
        for row in range(5):
            self.frame.rowconfigure(row, weight=1)
            for col in range(4):
                self.frame.columnconfigure(col, weight=1)

                btn = ctk.CTkButton(
                    self.frame,
                    text=buttons[row][col],
                    font=("Segoe UI", 18),
                    command=lambda x=buttons[row][col]: self.on_click(x)
                )

                btn.grid(
                    row=row,
                    column=col,
                    padx=6,
                    pady=6,
                    sticky="nsew"
                )

        # Keyboard support
        self.bind("<Key>", self.key_input)

    def on_click(self, char):

        if char == "C":
            self.expression = ""
            self.update_display()

        elif char == "=":
            self.calculate()

        elif char == "√":
            self.square_root()

        else:
            self.expression += str(char)
            self.update_display()

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.expression = result
            self.update_display()

        except:
            self.expression = "Error"
            self.update_display()

    def square_root(self):
        try:
            value = float(eval(self.expression))
            result = value ** 0.5
            self.expression = str(result)
            self.update_display()

        except:
            self.expression = "Error"
            self.update_display()

    def update_display(self):
        self.display.delete(0, "end")
        self.display.insert("end", self.expression)

    def key_input(self, event):

        if event.char in "0123456789+-*/().":
            self.expression += event.char
            self.update_display()

        elif event.keysym == "Return":
            self.calculate()

        elif event.keysym == "BackSpace":
            self.expression = self.expression[:-1]
            self.update_display()

        elif event.keysym == "Escape":
            self.expression = ""
            self.update_display()


# Run app
if __name__ == "__main__":
    app = PremiumCalculator()
    app.mainloop()

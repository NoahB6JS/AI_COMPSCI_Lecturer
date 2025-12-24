import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        self.entry = customtkinter.CTkEntry(self, placeholder_text="enter here:", width = 360, height=120)
        self.entry.pack(padx=20, pady=20)

        self.button = customtkinter.CTkButton(
            self,
            text="Ask",
            command=self.button_callback
        )
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        prompt = self.entry.get()
        print(prompt)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")

        self.label = customtkinter.CTkLabel(
            self,
            text="Computer Science helper",
            font=('arial', 30)
        )
        self.label.pack(padx=20, pady=20)

        self.label1 = customtkinter.CTkLabel(
            self,
            text="Speak to your tutor:",
            font=('arial', 15)
        )
        self.label1.pack(padx=20, pady=10)

        self.frame = MyFrame(self)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        


app = App()
app.mainloop()
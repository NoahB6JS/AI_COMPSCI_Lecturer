import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.label = customtkinter.CTkLabel(self, text="Speak to your tutor:", fg_color="transparent")
        

        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.pack(padx=20, pady=20)

        self.button = customtkinter.CTkButton(
            self,
            text="my button",
            command=self.button_callback
        )
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        text = self.entry.get()
        print(text)

app = App()
app.mainloop()
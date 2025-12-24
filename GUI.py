import customtkinter
from chatgpt_bot import Get_ai_output


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        
        self.label = customtkinter.CTkLabel(self, text="Computer Science helper", fg_color="transparent", font=('ariel',30))
        self.label.pack(padx=20, pady=20)
        self.label1 = customtkinter.CTkLabel(self, text="Speak to your tutor:", fg_color="transparent", font=('ariel',15))
        self.label1.pack(padx=20, pady=20)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="enter here:", width = 360, height=120)
        self.entry.pack(padx=20, pady=20)

        self.button = customtkinter.CTkButton(
            self,
            text="Ask",
            command=self.button_callback
        )
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        get_prompt_from_entry = self.entry.get()
        run_api = Get_ai_output()
        outputs = run_api.api_contact(get_prompt_from_entry)
        self.label1 = customtkinter.CTkLabel(self, text=(f"output:{outputs}"), fg_color="transparent", font=('ariel',15))
        self.label1.pack(padx=20, pady=20)
        
        
        
        


app = App()
app.mainloop()
from config import Session
from command import add_task
from database import Tasks
from datetime import datetime
import customtkinter


db = Session()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Window(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x600")
        self.minsize(600, 600)
        self.maxsize(600, 600)

        self.name_field = None
        self.description_field = None
        self.deadline_field = None
        self.db_window = None
        self.init_window()

        self.names = []
        self.descriptions = []
        self.deadlines = []

    def save_name(self):
        if self.name_field:
            return self.name_field.get()
        return ""

    def save_description(self):
        if self.description_field:
            return self.description_field.get()
        return ""

    def save_deadline(self):
        if self.deadline_field:
            return datetime.strptime(self.deadline_field.get(), '%Y-%m-%d').date()
        return ""

    def save_position_to_db(self):
        for _ in range(0, len(self.names)):
            add_task(db, self.names[_], self.descriptions[_], self.deadlines[_])
            self.names.pop(_)
            self.descriptions.pop(_)
            self.deadlines.pop(_)

    def show_the_database(self):
        self.db_window = customtkinter.CTkToplevel(self)
        self.db_window.geometry("1000x500")

        self.minsize(1000, 500)
        self.maxsize(1000, 500)

        self.scroll_db = customtkinter.CTkFrame(self.db_window)
        self.scroll_db.pack(fill='both', expand=True)

        self.canvas = customtkinter.CTkCanvas(self.scroll_db)
        self.scrollable_frame = customtkinter.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        self.db_window_scrollbar = customtkinter.CTkScrollbar(self.scroll_db, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.db_window_scrollbar.set)

        self.db_window_scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        result = db.query(Tasks).all()

        for item in result:
            formatted_deadline = datetime.strftime(item.deadline, '%Y-%m-%d')
            #formatted_deadline = deadline_date.strftime('%Y-%m-%d')
            this_info = customtkinter.CTkLabel(self.scrollable_frame,
                                               text=("\n\nИмя: " + item.name + "\n Описание: " + item.description + "\nДедлайн: " + formatted_deadline),
                                               font=("Arial", 20))
            this_info.pack()

    def init_window(self):
        label_name = customtkinter.CTkLabel(self, text="Input task name", font=("Arial", 20))
        label_name.pack()

        self.name_field = customtkinter.CTkEntry(self, width=300, placeholder_text="input task name", font=("Arial", 18))
        self.name_field.pack()

        label_desc = customtkinter.CTkLabel(self, text="Input task description", font=("Arial", 20))
        label_desc.pack()

        self.description_field = customtkinter.CTkEntry(self, width=300, placeholder_text="input task description",
                                                        font=("Arial", 18))
        self.description_field.pack()

        self.deadline_field = customtkinter.CTkEntry(self, width=300, placeholder_text="input task deadline",
                                                        font=("Arial", 18))
        self.deadline_field.pack()

        button_save_name = customtkinter.CTkButton(self, text="Save task name",
                                                   command=lambda: self.names.append(self.save_name()))
        button_save_name.pack()

        button_save_description = customtkinter.CTkButton(self, text="Save tea description",
                                                          command=lambda: self.descriptions.append(
                                                              self.save_description()))
        button_save_description.pack()

        button_save_deadline = customtkinter.CTkButton(self, text="Save tea deadline",
                                                          command=lambda: self.deadlines.append(
                                                              self.save_deadline()))
        button_save_deadline.pack()

        button_print_name = customtkinter.CTkButton(self, text="Print Names", command=lambda: print(self.names))
        button_print_name.pack()

        button_print_description = customtkinter.CTkButton(self,
                                                           text="Print Description",
                                                           command=lambda: print(self.descriptions))
        button_print_description.pack()

        button_print_deadline = customtkinter.CTkButton(self,
                                                           text="Print Deadline",
                                                           command=lambda: print(self.deadlines))
        button_print_deadline.pack()

        button_save_to_db = customtkinter.CTkButton(self, text="Save to database", command=self.save_position_to_db)
        button_save_to_db.pack()

        button_show_db = customtkinter.CTkButton(self, text="Show database", command=self.show_the_database)
        button_show_db.pack()




window_prototype = Window()
window_prototype.mainloop()
from tkinter import *
from tkinter import messagebox
from modules.generators import PasswordGen
from modules.tools import ToolManager
import json
import os


class Program:
    def __init__(self):
        self.config_folder = os.path.join(os.path.dirname(__file__), 'resources')
        self.pwd_file_path = os.path.join(self.config_folder, 'pwd.json')
        self.tool_manager = ToolManager()
        self.password_gen = PasswordGen()
        self.website_input = None
        self.username_input = None
        self.password_input = None
        self.website = None
        self.username = None
        self.pwd = None

    green = '#9bdeac'

    def clear_all_fields(self) -> None:
        """
        Remove any text in the website and password textboxes
        :return:            None
        """
        self.tool_manager.clear(self.website_input)
        self.tool_manager.clear(self.password_input)

    def insert_password(self) -> None:
        """
        Generating password, filling password textbox and copying generated password to the clipboard
        :return:            None
        """
        self.tool_manager.clear(self.password_input)
        generated_password = self.password_gen.generate_password()
        self.tool_manager.copy_generated_password(generated_password)
        self.password_input.insert(END, generated_password)

    def empty_field_check(self) -> None:
        """
        Checking that all fields are filled with information and passing to the data saving
        :return:            None
        """
        self.set_vars()
        if len(self.website) == 0 or len(self.pwd) == 0 or len(self.username) == 0:
            messagebox.showinfo(title='Empty fields', message='Please, do not leave any fields empty')
        else:
            self.add_data_to_file()

    def set_vars(self) -> None:
        """
        Setting instances for commonly used variables
        :return:            None
        """
        self.website = self.tool_manager.get_value(self.website_input)
        self.username = self.tool_manager.get_value(self.username_input)
        self.pwd = self.tool_manager.get_value(self.password_input)

    def add_data_to_file(self) -> None:
        """
        Check if data file exist, not empty and writing data to file
        :return:            None
        """
        self.set_vars()
        new_data = self.tool_manager.make_data(self.website, self.username, self.pwd)
        try:
            with open(self.pwd_file_path, 'r', encoding='utf8') as outfile:
                data = json.load(outfile)
        except FileNotFoundError:
            with open(self.pwd_file_path, 'w', encoding='utf8') as outfile:
                json.dump(new_data, outfile, indent=4)
        except json.JSONDecodeError:
            with open(self.pwd_file_path, 'w', encoding='utf8') as outfile:
                json.dump(new_data, outfile, indent=4)
        else:
            data.update(new_data)
            with open(self.pwd_file_path, 'w', encoding='utf8') as outfile:
                json.dump(data, outfile, indent=4)
        finally:
            self.clear_all_fields()

    def search_password(self) -> None:
        """
        Check if data file exist and parsing through the data and showing search results to the user
        :return:            None
        """
        self.set_vars()
        try:
            with open(self.pwd_file_path, 'r', encoding='utf8') as outfile:
                data = json.load(outfile)
        except FileNotFoundError:
            messagebox.showinfo(title='No file found', message='Looks like you are running this program first time. \n'
                                                               'Data with password records not found')
        else:
            if self.website in data:
                username = data[self.website]['username']
                password = data[self.website]['password']
                messagebox.showinfo(title=self.website, message=f'Email: {username}\nPassword: {password}')
            else:
                messagebox.showinfo(title='No data found', message=f'No data for {self.website} exist.')

    def create_window(self) -> None:
        """
        Setting up GUI and buttons events
        :return:            None
        """
        window = Tk()
        window.title('Password manager')
        window.config(padx=20, pady=20)
        window.resizable(False, False)

        # Creating main window (canvas)
        canvas = Canvas(width=200, height=200)
        lock_img = PhotoImage(file='resources/img/lock.png')
        canvas.create_image(100, 100, image=lock_img, anchor='center')
        canvas.grid(column=1, row=0)

        # Creating labels
        website_label = Label(text='Website:', font=('Arial', 14), anchor='e', justify='right')
        website_label.grid(column=0, row=1)

        username_label = Label(text='Username or Email:', font=('Arial', 14), anchor='e')
        username_label.grid(column=0, row=2)

        password_label = Label(text='Password:', font=('Arial', 14), anchor='e')
        password_label.grid(column=0, row=3)

        # Creating textboxes
        self.website_input = Entry(width=21, justify='left')
        self.website_input.grid(column=1, row=1)
        self.website_input.focus()

        self.username_input = Entry(width=38, justify='left')
        self.username_input.grid(column=1, row=2, columnspan=2)
        self.username_input.insert(0, self.tool_manager.get_email())

        self.password_input = Entry(width=21, justify='left')
        self.password_input.grid(column=1, row=3)

        # Creating buttons
        gen_pwd_btn = Button(text='Generate Password', borderwidth=1, border=1, width=13, command=self.insert_password)
        gen_pwd_btn.grid(column=2, row=3)

        add_pwd = Button(text='Add password to the file', borderwidth=1, border=1, width=36, command=self.empty_field_check)
        add_pwd.grid(column=1, row=4, columnspan=2)

        search_btn = Button(text='Search record', borderwidth=1, border=1, width=13, command=self.search_password)
        search_btn.grid(column=2, row=1)

        window.mainloop()

# Running the application
if __name__ == "__main__":
    program = Program()
    program.create_window()
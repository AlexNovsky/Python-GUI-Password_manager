from tkinter import *
import clipboard
import yaml
import os


class ToolManager:
    """
    Class for common methods, used by other methods in the main application and Generators classes.
    """

    def __init__(self):
        self.config_folder = os.path.join(os.path.dirname(__file__), '..', 'resources')
        self.config_file_path = os.path.join(self.config_folder, 'data.yaml')

    def clear(self, entry) -> None:
        """
        Clear the texbox
        :param entry:               Location or name/variable of the textbox desired to be cleared
        :return:                    None
        """
        entry.delete(0, END)

    def get_email(self) -> str:
        """
        Retrieving the default email/username, stated in the data.yaml file
        :return:                    String, representing the default email
        """
        with open(self.config_file_path, 'r') as file:
            data = yaml.safe_load(file)
        default_email = data['user_data']['email']
        return str(default_email)

    def get_value(self, entry) -> str:
        """
        Retrieving text from the texbox and returning its value as a string
        :param entry:               Location or name/variable of the textbox desired to be cleared
        :return:                    String, representing user's input (text)
        """
        value = entry.get()
        return value

    def copy_generated_password(self, text_to_copy) -> None:
        """
        Copying provided text to the clipboard
        :param text_to_copy:        Text, that should be copied to clipboard
        :return:                    None
        """
        clipboard.copy(text_to_copy)

    def make_data(self, website, username, pwd) -> dict:
        """
        Makes a dictionary in defined format with information, entered by the User
        :param website:             String parameter with information, entered into the appropriate textbox
        :param username:            String parameter with information, entered into the appropriate textbox
        :param pwd:                 String parameter with entered or generated password
        :return:                    Dictionary in defined format with required information
        """
        data_to_write = {
            website: {
                'username': username,
                'password': pwd,
            }
        }
        return data_to_write

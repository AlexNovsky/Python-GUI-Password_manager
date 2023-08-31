import random
import yaml
import os


class PasswordGen:
    """
    Class,
    """
    def __init__(self):
        self.config_folder = os.path.join(os.path.dirname(__file__), '..', 'resources')
        self.config_file_path = os.path.join(self.config_folder, 'data.yaml')

    def get_whitelisted_digits(self) -> int:
        """
        Retrieving int variable with whitelisted in configuration yaml file digits
            :return:                Integer variable, representing whitelisted_digits
        """
        with open(self.config_file_path, 'r') as file:
            data = yaml.safe_load(file)
        whitelisted_digits = data['whitelisted_characters']['digits']
        return whitelisted_digits

    def get_whitelisted_letters(self) -> str:
        """
        Retrieving str variable with whitelisted in configuration yaml file letters
            :return:                String, representing whitelisted_letters
        """
        with open(self.config_file_path, 'r') as file:
            data = yaml.safe_load(file)
        whitelisted_letters = data['whitelisted_characters']['letters_basic']
        return whitelisted_letters

    def get_whitelisted_basic_symbols(self) -> str:
        """
        Retrieving str variable with whitelisted in configuration yaml file symbols
            :return:                String, representing basic_symbols
        """
        with open(self.config_file_path, 'r') as file:
            data = yaml.safe_load(file)
        basic_symbols = data['whitelisted_characters']['symbols_basic']
        return basic_symbols

    def get_whitelisted_extended_symbols(self) -> str:
        """
        Retrieving str variable with whitelisted in configuration yaml file additional symbols
            :return:                String, representing extended_symbols
        """
        with open(self.config_file_path, 'r') as file:
            data = yaml.safe_load(file)
        extended_symbols = data['whitelisted_characters']['symbols_extended']
        return extended_symbols

    def generate_password(self) -> str:
        """
        Randomly generates unique 15 symbols length password (configurable) with all configured whitelisted symbols
            :return:                String, representing generated_password
        """
        password_len = 15
        generated_password = ''
        digits = str(self.get_whitelisted_digits())
        letters = str(self.get_whitelisted_letters())
        symbols = str(self.get_whitelisted_basic_symbols())
        extra_symbols = str(self.get_whitelisted_extended_symbols())
        password_characters = f'{digits}{letters}{symbols}{extra_symbols}'
        for n in range(password_len):
            generated_password += ''.join(random.choice(str(password_characters)))
        return str(generated_password)

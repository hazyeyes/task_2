import keyboard
import sys
from colorama import Back, Fore, Style, init, deinit
from pyfiglet import Figlet

init()

def print_introd(text, font="speed", text_color=Fore.BLACK, bg_color=Back.LIGHTWHITE_EX):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{bg_color}{text_color}{formatted_text}{Fore.RESET}{Back.RESET}")

def print_instruction_1(text, font="cybermedium", text_color=Fore.BLACK, bg_color=Back.LIGHTWHITE_EX):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{bg_color}{text_color}{formatted_text}{Fore.RESET}{Back.RESET}")

def print_instruction_2(text, font="cybermedium", text_color=Fore.WHITE):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{text_color}{formatted_text}{Fore.RESET}")

def print_information_header(text, font="slant", text_color=Fore.BLACK, bg_color=Back.LIGHTWHITE_EX):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{bg_color}{text_color}{formatted_text}{Fore.RESET}{Back.RESET}")

def print_information(text, font="digital", text_color=Fore.BLACK):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{text_color}{formatted_text}{Fore.RESET}")

def print_end_1(text, font="standard", text_color=Fore.BLACK, bg_color=Back.LIGHTWHITE_EX):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{bg_color}{text_color}{formatted_text}{Fore.RESET}{Back.RESET}")

def print_end_2(text, font="smkeyboard", text_color=Fore.WHITE):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{text_color}{formatted_text}{Fore.RESET}")

def print_repeat(text, font="poison", text_color=Fore.RED):
    figlet = Figlet(font=font)
    formatted_text = figlet.renderText(text)
    print(f"{text_color}{formatted_text}{Fore.RESET}")

def numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print(f"{Fore.LIGHTRED_EX}Invalid input. Please enter a valid number.")

header = "Good day User!"
instruction_1 = "Press space to continue"
print_introd(header)
print()
print()
print()
print()
print()
print_instruction_1(instruction_1)
print()

def on_space(event):
    if event.name == 'space':
        print_instruction_2("In order to continue, please enter the following information below...")

        name = input(f"{Fore.WHITE}   Name   : ")
        age = numeric_input(f"{Fore.WHITE}   Age    : ")
        address = input(f"{Fore.WHITE}   Address: ")
        email = input(f"{Fore.WHITE}   E-mail : ")
        
        print()
        print_information_header("Personal Information:")
        print_information(f"Name: {name}")
        print_information(f"Age: {age} years old")
        print_information(f"Address: {address}")
        print_information(f"E-mail: {email}")
        print()

    confirmation = input(f"{Fore.WHITE}Do you confirm that the information you entered is correct? (yes/no): ")
    if confirmation.lower() == "yes":
        print_end_1("Thank you for choosing X Corporation!")
        print_end_2("We will e-mail you as soon as we can.")
        sys.exit()
    if confirmation.lower() == "no":
        print_repeat("Error!")
 
keyboard.on_press_key('space', on_space)

keyboard.wait('esc')
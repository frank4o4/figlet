import pyfiglet

def generate_ascii_art(word, color):
    ascii_art = pyfiglet.figlet_format(word)
    color_code = get_color_code(color)
    colored_ascii_art = color_code + ascii_art + '\033[0m'  # Adding the color code and reset code
    print(colored_ascii_art)

def get_color_code(color):
    color_codes = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m'
    }
    return color_codes.get(color.lower(), '\033[0m')  # Default to reset code if color not found

# Example usage
word = input("Enter a word: ")
color = input("Enter a color (black, red, green, yellow, blue, magenta, cyan, white): ")
generate_ascii_art(word, color)

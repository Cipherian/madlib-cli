import re

small_template = "assets/dark_and_stormy_night_template.txt"
large_template = "assets/template.txt"
Mad_libs_dict ={
    """Stores the stripped strings in text_templates and stores adjectives, verbs and nouns in the list"""
    "text_templates": "",
    "adjective": []
}

def welcome():
    print('Welcome to my Mad Lib game!')
    print('Follow the instructions and input the text in each corresponding field')


def parse_template(text):
    """Uses regex to parse the template taken from the read_template function"""
    regex_pattern = re.compile(r"\{[^}]*}", re.IGNORECASE)
    regex = re.sub(regex_pattern, '{}', text)
    Mad_libs_dict['text_templates'] = regex

    words_list = re.findall(regex_pattern, text)

    words = []

    for word in words_list:
        word = word.strip("{}")
        words.append(word)
        Mad_libs_dict['adjective'].append(word)

    return regex, tuple(words)


def read_template(file):
    """Opens a file which is specified by the user"""
    try:
        with open(file, 'r') as text:
            item = text.read()
            return item
    except FileNotFoundError as error:
        print(error)
        raise FileNotFoundError

def merge(text, substring):
    return text.format(*substring)

def save_story(story):
    with open("assets/saved_stories.txt", "w") as file:
        file.write(story)

def play_game(text_file):
    entries = []
    content = read_template(text_file)
    parse_template(content)
    for word in Mad_libs_dict['adjective']:
        print(f"I need a(n): {word}")
        user_input = input("Fill in words here: ")
        entries.append(user_input)

    story = merge(Mad_libs_dict['text_templates'], tuple(entries))
    print(story)
    save_story(story)
    print('Thank you for playing my mad libs game!')
    exit()

def mad_libs_game():
    print('Type DARK to play a dark and stormy night madlib \n Type GAMING to play a gaming madlib \n type quit to exit.')
    user_input = input("> ")
    while user_input.lower() != 'quit'.lower():
        if user_input.lower() == 'DARK'.lower():
            play_game(small_template)
        if user_input.lower() == "GAMING".lower():
            play_game(large_template)
        else:
            print('Play some other time!')


if __name__ == "__main__":
    welcome()
    mad_libs_game()





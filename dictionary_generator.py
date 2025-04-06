class List:
    def __init__(self):
        self.items = []

    def __contains__(self, item):
        return item in self.items

    def __iter__(self):
        while self.items:
            yield self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def append(self, item, front=False):
        for variant in (item, item.lower(), item.title(), item.upper()):
            if variant in self.items:
                continue
            if front:
                self.items.insert(0, variant)
            else:
                self.items.append(variant)


class PassGen:
    def __init__(self):
        self.words = []
        self.birthdays = []
        self.active = True
        self.password_list = List()
        self.suffixes = [str(i) for i in range(124)]

    def get_input(self):
        print(" Welcome to the Password List Generator\n")
        while self.active:
            print("Enter a keyword, name, password, number, symbol, or birthday (mm-dd-yyyy).")
            print("Type 'generate' to create your password list.")

            try:
                user_input = input("\n$> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nSession ended.")
                self.active = False
                break

            if not user_input:
                continue

            if user_input.lower() == "generate":
                self.generate()
                self.active = False
            else:
                self.append_data(user_input)
                print("\n Input added.\n")

    def append_data(self, data):
        if len(data.split('-')) == 3:  # Birthday format
            if data not in self.birthdays:
                self.birthdays.append(data)

        elif data.isdigit():  # Number
            if data not in self.suffixes:
                self.suffixes.insert(0, data)
            self.password_list.append(data, front=True)

        elif len([c for c in data if c.isdigit()]) == (len(data) - 1):  # Float-like numbers
            if data not in self.suffixes:
                self.suffixes.insert(0, data)
                self.suffixes.insert(0, ''.join(c for c in data if c.isdigit()))
            self.password_list.append(data, front=True)
            self.password_list.append(''.join(c for c in data if c.isdigit()), front=True)

        elif data.isalpha():  # Alphabetic words
            if data.lower() not in self.words:
                self.words.append(data)

        elif all(not c.isalnum() for c in data):  # Symbols
            if data not in self.suffixes:
                self.suffixes.insert(0, data)

        else:  # Password or other mixed input
            self.password_list.append(data, front=True)

    def generate(self):
        print("\n Generating password list. Please wait...\n")

        for suffix in self.suffixes:
            for word in self.words:
                self.password_list.append(word)
                self.password_list.append(f'{word}{suffix}')
                self.password_list.append(f'{suffix}{word}')
                self.password_list.append(f'{suffix}{word}{suffix}')

                for bday in self.birthdays:
                    day, month, year = bday.split('-')[1], bday.split('-')[0], bday.split('-')[-1]
                    plain_bday = bday.replace('-', '')

                    combos = [
                        plain_bday,
                        f'{word}{year}', f'{word}{year[2:]}', f'{word}{plain_bday}',
                        f'{day}{word}', f'{day[-1]}{word}',
                        f'{year}{word}', f'{year[2:]}{word}',
                        f'{month}{word}', f'{month[-1]}{word}',
                        f'{month}{day}{word}', f'{month[-1]}{day}{word}',
                        f'{month}{day[-1]}{word}', f'{month[-1]}{day[-1]}{word}',
                        f'{day}{month}{word}', f'{day[-1]}{month}{word}',
                        f'{day}{month[-1]}{word}', f'{day[-1]}{month[-1]}{word}',
                        f'{month}{day}{word}{year}', f'{month}{day}{word}{year[2:]}',
                        f'{month[-1]}{day}{word}{year}', f'{month[-1]}{day}{word}{year[2:]}',
                        f'{month}{day[-1]}{word}{year}', f'{month}{day[-1]}{word}{year[2:]}',
                        f'{month[-1]}{day[-1]}{word}{year}', f'{month[-1]}{day[-1]}{word}{year[2:]}',
                        f'{month}{word}{suffix}', f'{month[-1]}{word}{suffix}',
                        f'{day}{word}{suffix}', f'{day[-1]}{word}{suffix}',
                        f'{suffix}{word}{month}', f'{suffix}{word}{month[-1]}',
                        f'{suffix}{word}{day}', f'{suffix}{word}{day[-1]}',
                        f'{suffix}{word}{year}', f'{suffix}{word}{year[2:]}',
                    ]

                    for combo in combos:
                        self.password_list.append(combo)

        with open('pass.txt', 'wt', encoding='utf-8') as f:
            print(f"\n Password list generated with {len(self.password_list)} entries.")
            print(" Saved as 'pass.txt'.\n")
            for pwd in self.password_list:
                f.write(f'{pwd}\n')


if __name__ == '__main__':
    PassGen().get_input()

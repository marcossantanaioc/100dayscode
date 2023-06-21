SOURCE_LETTER = 'Input/Letters/starting_letter.txt'
NAMES_FILE = 'Input/Names/invited_names.txt'


def add_name_to_letter(names_path: str = NAMES_FILE, source_letter_path: str = SOURCE_LETTER):
    with open(names_path, 'r') as f:
        names = [line.strip() for line in f.readlines()]

    for name in names:
        all_lines = []
        with open(source_letter_path, 'r') as f:
            for line in f.readlines():
                line = line.strip()
                line = line.replace("[name]", name)
                all_lines.append(line)

        with open(f'Output/ReadyToSend/{name}_letter.txt', 'w') as o:
            for line in all_lines:
                o.write(f"{line}\n")

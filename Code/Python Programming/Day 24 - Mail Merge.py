PLACEHOLDER = '[name]'

with open('../Data/invited_names_24.txt', mode='r') as f:
    names = f.readlines()

with open('../Data/starting_letter_24.txt', mode='r') as f:
    letter = f.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        with open('../Data/letter_to_send_24.txt', mode='a') as f:
            f.write(new_letter)

    
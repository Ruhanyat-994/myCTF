# Open the original file for reading
with open('file.txt', 'r') as file:
    lines = file.readlines()

# Write the updated content to a new file
with open('updated_file.txt', 'w') as updated_file:
    count = 1
    for line in lines:
        # Replace ### with ### <number>.
        if line.strip().startswith('###'):
            line = line.replace('###', f'### {count}.', 1)
            count += 1
        updated_file.write(line)

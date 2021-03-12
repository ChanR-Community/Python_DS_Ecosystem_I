from os import getcwd, listdir, chdir, makedirs

folders_to_make = ['src', 'notes', 'data']

for folder in folders_to_make:
    makedirs(folder)


for folder in folders_to_make:
    data_path = getcwd() + f"/{folder}"
    with open(f"{data_path}/starter.md", "w") as my_file:
        my_file.write(f"This file was created in {folder}")
    my_file.close()
    

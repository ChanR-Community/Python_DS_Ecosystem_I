from os import getcwd, listdir, chdir, makedirs, system

folders_to_make = ['src', 'notes', 'data']

for folder in folders_to_make:
    makedirs(folder)


for folder in folders_to_make:
    data_path = getcwd() + f"/{folder}"
    system(f"rm -rf {data_path}/*.md")

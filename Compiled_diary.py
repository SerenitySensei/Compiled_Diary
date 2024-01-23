import os

def extract_free_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    free_text_started = False
    free_text = []

    for line in lines:
        if line.startswith("##### "):
            free_text_started = True
            continue
        if free_text_started:
            free_text.append(line)
    
    return free_text

def compile_diary(folder_path):
    diary_entries = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            diary_entries.extend(extract_free_text(file_path))

    with open('Sammanställd_dagbok.txt', 'w', encoding='utf-8') as compiled_file:
        compiled_file.writelines(diary_entries)

# Replace 'your_folder_path' with the path to your folder containing the text files
compile_diary('your_folder_path')

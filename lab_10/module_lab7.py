# module_lab7.py 
 
def process_file(file_path): 
    Пример функции для обработки файла. 
    with open(file_path, "r") as file: 
        data = file.read() 
    print(f"Processing file: {file_path}") 
    # Добавьте здесь логику обработки файла 
    return data 

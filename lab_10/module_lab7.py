# module_lab7.py 
 
def process_file(file_path): 
    �ਬ�� �㭪樨 ��� ��ࠡ�⪨ 䠩��. 
    with open(file_path, "r") as file: 
        data = file.read() 
    print(f"Processing file: {file_path}") 
    # ������� ����� ������ ��ࠡ�⪨ 䠩�� 
    return data 

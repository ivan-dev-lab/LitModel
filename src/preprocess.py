import nltk
import pandas as pd
import os
import string

# прочтение всех необработанных корпусов с текстами
def get_corpuses (dirpath: str) -> list[dict]:
    path_list = os.listdir(dirpath)
    text_list = []

    for filepath in path_list:
        with open(f"{dirpath}/{filepath}", encoding='utf8') as txt_file:
            text = {}
            text[filepath.split('.')[0]] = txt_file.readlines()
            
            text_list.append(text)
    
    return text_list
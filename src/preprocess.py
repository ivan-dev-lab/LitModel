import nltk
import pandas as pd
import os
import string

# прочтение всех необработанных корпусов с текстами
def get_corpus (dirpath: str) -> dict:
    path_list = os.listdir(dirpath)
    corpus = {}

    for filepath in path_list:
        with open(f"{dirpath}/{filepath}", encoding='utf8') as txt_file:
            corpus[filepath.split('.')[0]] = ' '.join(txt_file.readlines())

    return corpus


def clean_text (corpus_data: dict) -> dict:
    cleaned_corpus = {}
    punctuation = string.punctuation + '0123456789' + '\n' + '\xa0' + '«»'
    
    for name, text in corpus_data.items():
        if name != 'PIN': continue # текст Война и Мир очень большой, на время разработки необходимая мера
        
        cleaned_text = text.lower()
        
        trans_table = str.maketrans('', '', punctuation)
        cleaned_text = cleaned_text.translate(trans_table)

        cleaned_corpus[name] = cleaned_text
        
    return cleaned_corpus
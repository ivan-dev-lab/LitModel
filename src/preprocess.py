import nltk
import pandas as pd
import os
import string
import pymorphy3

# прочтение всех необработанных корпусов с текстами
def get_corpus_data (dirpath: str) -> dict:
    path_list = os.listdir(dirpath)
    corpus_data = {}

    for filepath in path_list:
        if 'VIM' in filepath: continue
        with open(f"{dirpath}/{filepath}", encoding='utf8') as txt_file:
            corpus_data[filepath.split('.')[0]] = ' '.join(txt_file.readlines())

    return corpus_data
    
def clean_text (corpus_data: dict) -> dict:
    cleaned_corpus = {}
    punctuation = string.punctuation + '0123456789' + '\n' + '\xa0' + '«—»' + ' '
    
    for name, tokenized_text in corpus_data.items():
        cleaned_text = [token.lower() for token in tokenized_text if token not in punctuation]
        cleaned_corpus[name] = cleaned_text
        
    return cleaned_corpus

def lemmatize (corpus_data: dict) -> dict:
    morph = pymorphy3.MorphAnalyzer(lang='ru')
    lemmatized_corpus = {}

    for name, tokenized_text in corpus_data.items():    
        lemmatized_text = []
        for token in tokenized_text[0:1000]:
            lemmatized_text.append(morph.parse(token)[0].normal_form)
        lemmatized_corpus[name] = lemmatized_text
            
    return lemmatized_corpus
        
def preprocess_data (dirpath: str):
    corpus_data = get_corpus_data('data/RawTexts/')

    tokenized_corpus = {}
    for name, text in corpus_data.items():
        tokenized_corpus[name] = nltk.word_tokenize(text)

    preprocessed_text = lemmatize(
        clean_text(tokenized_corpus)
    )

    return preprocessed_text


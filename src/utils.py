from pathlib import Path
from typing import List, Dict
from src.configs import (
    depara_emb,
    vowels,
    consonants,
    digits,
    punctuations
)
import unidecode
import numpy as np

def get_text(path: Path) -> str:
    return Path(path).read_text(encoding='utf-8')

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = unidecode.unidecode(text)
    return text

def text_to_list(text: str) -> List[str]:
    list_texts = text.split('\n')
    return list_texts

def fill_pad_list(list_: List[int], limit:int = 30):
    if len(list_) > limit:
        list_ = list_[:limit]
    while len(list_) < limit:
        list_.append(depara_emb['pad'])
    return list_

def encodding_text(text: str) -> List[int]:
    transformed_list = []
    for char in text:
        if char in vowels:
            transformed_list.append(depara_emb['vowels'])
        elif char in consonants:
            transformed_list.append(depara_emb['consonants'])
        elif char == ' ':
            transformed_list.append(depara_emb['espace'])
        elif char in digits:
            transformed_list.append(depara_emb['digits'])
        elif char in punctuations:
            transformed_list.append(depara_emb['punctuations'])
        else:
            transformed_list.append(depara_emb['unk'])
    transformed_list_pad = fill_pad_list(transformed_list)
    return transformed_list_pad

def pass_prep_emb(list_text: List[str]) -> List[int]:
    return [encodding_text(x) for x in list_text]

def make_target(list_text_emb: List[int], label: int) -> List[int]:
    target = [label] * len(list_text_emb)
    return np.array(target)

def list_to_numpy(list_text_emb):
    return np.array(list_text_emb)

def union_x_and_y(x, y) -> np.array:
    return np.hstack((x, y.reshape(-1,1)))

def union_classes(x_0, x_1):
    return np.vstack((x_0, x_1))

def get_data(labels_dict: Dict[int, str]) -> np.array:
    list_data = []
    for label, label_name in labels_dict.items():
        text_raw = get_text(f'data/{label_name}.txt')
        text_prep = preprocess_text(text_raw)
        text_list = text_to_list(text_prep)
        text_list_emb = pass_prep_emb(text_list)
        X = list_to_numpy(text_list_emb)
        y = make_target(X, label=label)
        data = union_x_and_y(X, y)
        list_data.append(data)
    print('Finish ...')
    return union_classes(list_data[0], list_data[1])

def prep_one_text(text: str):
    text_prep_initial = preprocess_text(text)
    text_list = text_to_list(text_prep_initial)
    text_list_emb = pass_prep_emb(text_list)
    return text_list_emb

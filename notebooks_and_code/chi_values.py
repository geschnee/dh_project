import math
import pandas as pd


def chi_value_dataframe(freqs, freqs_artist):
    sum_plain = 0
    for i in freqs.values():
        sum_plain+=i

    sum_artist = 0
    for i in freqs_artist.values():
        sum_artist+=i

    word_chi_values ={}    
    for w, freq_artist in freqs_artist.items():
        word_artist = freq_artist
        word_plain = freqs[w]
        others_artist = sum_artist - word_artist
        others_plain = sum_plain - word_plain
        total = sum_artist + sum_plain
        word = word_artist + word_plain
        others = others_artist + others_plain
        expected_word_artist = (word * sum_artist) / total
        expected_word_plain = (word * sum_plain) / total
        expected_others_artist = (others * sum_artist) / total
        expected_others_plain = (others * sum_plain) / total
        
        word_chi_values[w] = [math.pow(word_artist - expected_word_artist,2)/expected_word_artist \
            + math.pow(word_plain - expected_word_plain,2)/expected_word_plain \
            + math.pow(others_artist - expected_others_artist,2)/expected_others_artist\
            + math.pow(others_plain - expected_others_plain,2)/expected_others_plain , word_artist]

    chi_values = pd.DataFrame.from_dict(word_chi_values, orient="index", columns = ["chi_values", "word_frequency"])
    chi_values.index.name = 'word'

    chi_values.sort_values("chi_values", axis=0, ascending=False, inplace=True)
    chi_values.reset_index(inplace=True)
    return chi_values

def single_chi_value(freqs, freqs_artist, word):
    sum_plain = 0
    for i in freqs.values():
        sum_plain+=i

    sum_artist = 0
    for i in freqs_artist.values():
        sum_artist+=i

    word_chi_values ={}    
    
    word_artist = freqs_artist[word]
    word_plain = freqs[word]
    others_artist = sum_artist - word_artist
    others_plain = sum_plain - word_plain
    total = sum_artist + sum_plain
    word = word_artist + word_plain
    others = others_artist + others_plain
    expected_word_artist = (word * sum_artist) / total
    expected_word_plain = (word * sum_plain) / total
    expected_others_artist = (others * sum_artist) / total
    expected_others_plain = (others * sum_plain) / total

    if expected_word_artist == 0:
        print(w)
        print(f'{word_artist} | {word_plain} || {word}')
        print(f'{others_artist} | {others_plain} || {others}')
        print(f'{sum_artist} | {sum_plain} || {total}')

        print(f'{expected_word_artist} | {expected_word_plain}')
        print(f'{expected_others_artist} | {expected_others_plain}')
    chi_value = [math.pow(word_artist - expected_word_artist,2)/expected_word_artist \
        + math.pow(word_plain - expected_word_plain,2)/expected_word_plain \
        + math.pow(others_artist - expected_others_artist,2)/expected_others_artist\
        + math.pow(others_plain - expected_others_plain,2)/expected_others_plain , word_artist]
    
    return chi_value
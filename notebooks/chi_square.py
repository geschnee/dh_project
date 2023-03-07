
stopwords=read_stopwords()
stopwords.append("greg")
stopwords.append("rutkowski")

freqs = compute_freq(exact_matches, "prompt", stopwords)
print(f'finished')

greg_df = my_utils.exact_match_dataframe(exact_matches, "greg rutkowski")
freqs_greg = compute_freq(greg_df, "prompt", stopwords)
print(f'finished')

import math

print(f'{len(freqs.keys())} items in plain, {len(freqs_greg.keys())} items in greg')

sum_plain = 0
for i in freqs.values():
    sum_plain+=i
    
sum_greg = 0
for i in freqs_greg.values():
    sum_greg+=i

word_chi_values ={}    
for w, freq_greg in freqs_greg.items():
    word_greg = freq_greg
    word_plain = freqs[w]
    others_greg = sum_greg - word_greg
    others_plain = sum_plain - word_plain
    total = sum_greg + sum_plain
    word = word_greg + word_plain
    others = others_greg + others_plain
    expected_word_greg = (word * sum_greg) / total
    expected_word_plain = (word * sum_plain) / total
    expected_others_greg = (others * sum_greg) / total
    expected_others_plain = (others * sum_plain) / total
    word_chi_values[w] = math.pow(word_greg - expected_word_greg,2)/expected_word_greg \
        + math.pow(word_plain - expected_word_plain,2)/expected_word_plain \
        + math.pow(others_greg - expected_others_greg,2)/expected_others_greg\
        + math.pow(others_plain - expected_others_plain,2)/expected_others_plain
    
    
    #print(f'{word_greg} | {word_plain} || {word}')
    #print(f'{others_greg} | {others_plain} || {others}')
    #print(f'{sum_greg} | {sum_plain} || {total}')
    
    #print(f'{expected_word_greg} | {expected_word_plain}')
    #print(f'{expected_others_greg} | {expected_others_plain}')
    #print(f'{w} --> {word_chi_values[w]}')
    
#print(word_chi_values)

chi_values = pd.DataFrame.from_dict(word_chi_values, orient="index", columns = ["chi_values"])
chi_values.index.name = 'word'

chi_values.sort_values("chi_values", axis=0, ascending=False, inplace=True)
chi_values.reset_index(inplace=True)

print(f'amount of words with higher than threshold chi value: {chi_values[chi_values["chi_values"]>=chi_square_value].shape}')

print(chi_values.head(40))

    

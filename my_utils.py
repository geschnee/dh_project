from difflib import SequenceMatcher as SM

def read_lines_as_list(filename):
    result = []
    f = open(filename, "r")
    for x in f.readlines():
      n = x[0:-1]
      if len(n) >= 2:
          result.append(n)
    
    return result

def painter_included_fuzzy(ga, parts, similarity_threshold):
    painter_components = [x for x in re.split(';|,|\.| |:|-', ga) if len(x)>0]
    components_found = 0
    for ac in painter_components:
        for p in parts:
            # print(f'{p} {ac} {SM(None, p, ac).ratio()}')
            if SM(None, p, ac).ratio() >= similarity_threshold: ## fuzzy comparison possible here
                components_found += 1
                break
    if components_found == len(painter_components):
        return True
    else:
        return False

import re
def extract_painters_fuzzy(str, given_painters, similarity_threshold):
    painters = []
    parts = [x.lower() for x in re.split(';|,|\.| |:|-', str) if len(x)>0]
    #print(parts)
    for ga in given_painters:
        if painter_included_fuzzy(ga, parts, similarity_threshold):
            painters.append(ga)
    
    return painters

def extract_painters_exact(str, given_painters):
    painters = []
    
    for gp in given_painters:
        if gp in str:
            painters.append(ga)
    
    return painters



def extract_painters_fuzzy_test():
    given_painters = ["greg rutkowsky", "Vincent van Gogh", "Banksy", "Salvador Dalí", "Hans-Werner Sahm"]
    given_painters = [x.lower() for x in given_painters]
    

    similarity_threshold = 0.8

    assert extract_painters_fuzzy("artwork by greg rutkowsky", given_painters, similarity_threshold) == ["greg rutkowsky"], extract_painters_fuzzy("artwork by greg rutkowsky", given_painters, similarity_threshold)
    
    assert extract_painters_fuzzy("artwork, by greg rutzky", given_painters, similarity_threshold) == [], extract_painters_fuzzy("artwork, by greg rutzky", given_painters, similarity_threshold)
   
    search = extract_painters_fuzzy("artwork by greg rutkowsky and Salvador Dalí", given_painters, similarity_threshold)
    assert search == ["greg rutkowsky", "salvador dalí"], f'search is {search}'
    
    search = extract_painters_fuzzy("artwork by greg rutkowsky and Salvador Dalí and Banksy", given_painters, similarity_threshold)
    assert search == ["greg rutkowsky", "banksy", "salvador dalí"], f'search is {search}'
   
    # TYPO: "bansky" instead of "banksy"
    search = extract_painters_fuzzy("bansky", given_painters, similarity_threshold)
    assert search == ["banksy"], f'search is {search}'
    
    search = extract_painters_fuzzy("Hans-Werner Sahm", given_painters, similarity_threshold)
    assert search == ["hans-werner sahm"], f'search is {search}'
    
    # Missing dash for doublename
    search = extract_painters_fuzzy("Hans Werner Sahm", given_painters, similarity_threshold)
    assert search == ["hans-werner sahm"], f'search is {search}'
    
    # TYPO
    search = extract_painters_fuzzy("painting by Vinncent van Gogh", given_painters, similarity_threshold)
    assert search == ["vincent van gogh"], f'search is {search}'

    print("All tests passed")

    
    
def exact_match_dataframe(df, name):
    result = df.copy()
    result['artist'] = result['prompt'].apply(
        lambda prompt: name if name in prompt else "NONE")
    result = result.loc[result['artist'] == name]
    return result

def read_occurences_list(filename):
    result = dict()
    f = open(filename, "r")
    for x in f.readlines():
        splits = x.split(":")
        assert len(splits)==2
        artist = splits[0]
        occs = int(splits[1])
        result[artist]=occs
    return result

if __name__ == "__main__":
    extract_painters_fuzzy_test()



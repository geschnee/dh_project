from difflib import SequenceMatcher as SM

def read_lines_as_list(filename):
    result = []
    f = open(filename, "r")
    for x in f.readlines():
      n = x[0:-1]
      if len(n) >= 1:
          result.append(n)
    
    return result

def artist_included_fuzzy(ga, parts, similarity_threshold):
    artist_components = [x for x in re.split(';|,|\.| |:|-', ga) if len(x)>0]
    components_found = 0
    for ac in artist_components:
        for p in parts:
            # print(f'{p} {ac} {SM(None, p, ac).ratio()}')
            if SM(None, p, ac).ratio() >= similarity_threshold: ## fuzzy comparison possible here
                components_found += 1
                break
    if components_found == len(artist_components):
        return True
    else:
        return False

import re
def extract_artists_fuzzy(str, given_artists, similarity_threshold):
    artists = []
    parts = [x.lower() for x in re.split(';|,|\.| |:|-', str) if len(x)>0]
    #print(parts)
    for ga in given_artists:
        if artist_included_fuzzy(ga, parts, similarity_threshold):
            artists.append(ga)
    
    return artists

def extract_artists_exact(str, given_artists):
    artists = []
    str = str.lower()
    
    for gp in given_artists:
        if gp in str:
            artists.append(gp)
    
    return artists



def extract_artists_fuzzy_test():
    given_artists = ["greg rutkowsky", "Vincent van Gogh", "Banksy", "Salvador Dalí", "Hans-Werner Sahm"]
    given_artists = [x.lower() for x in given_artists]
    

    similarity_threshold = 0.8

    assert extract_artists_fuzzy("artwork by greg rutkowsky", given_artists, similarity_threshold) == ["greg rutkowsky"], extract_artists_fuzzy("artwork by greg rutkowsky", given_artists, similarity_threshold)
    
    assert extract_artists_fuzzy("artwork, by greg rutzky", given_artists, similarity_threshold) == [], extract_artists_fuzzy("artwork, by greg rutzky", given_artists, similarity_threshold)
   
    search = extract_artists_fuzzy("artwork by greg rutkowsky and Salvador Dalí", given_artists, similarity_threshold)
    assert search == ["greg rutkowsky", "salvador dalí"], f'search is {search}'
    
    search = extract_artists_fuzzy("artwork by greg rutkowsky and Salvador Dalí and Banksy", given_artists, similarity_threshold)
    assert search == ["greg rutkowsky", "banksy", "salvador dalí"], f'search is {search}'
   
    # TYPO: "bansky" instead of "banksy"
    search = extract_artists_fuzzy("bansky", given_artists, similarity_threshold)
    assert search == ["banksy"], f'search is {search}'
    
    search = extract_artists_fuzzy("Hans-Werner Sahm", given_artists, similarity_threshold)
    assert search == ["hans-werner sahm"], f'search is {search}'
    
    # Missing dash for doublename
    search = extract_artists_fuzzy("Hans Werner Sahm", given_artists, similarity_threshold)
    assert search == ["hans-werner sahm"], f'search is {search}'
    
    # TYPO
    search = extract_artists_fuzzy("painting by Vinncent van Gogh", given_artists, similarity_threshold)
    assert search == ["vincent van gogh"], f'search is {search}'

    print("All tests passed")

def artist_in_list(l, artist):
    l = l.tolist()
    #rint(l)
    assert type(l) == list, f'type is {type(l)}'
    if artist in l:
       #print(f'fnd in {l}')
        return True
    else:
        return False
    
def exact_match_dataframe(df, name):
    name = name.lower()
    result = df.copy()
   #result['included'] = result['artists'].map(
   #    lambda artists: artist_in_list(artists, name))
    result['included'] = result['artists'].map(
       lambda artists: True if name in artists.tolist() else False)
    #print(result)
    assert "included" in result.columns, f'included is not in {result.columns}'
   #print(f'result columns {result.columns}')
    result = result.loc[result['included'] == True]
    return result



def search_prompt_splits(df, str):
    str = str.lower()
    result = df.copy()
    result['included'] = result['prompt'].map(
       lambda prompt: True if str in re.split(';|,|\.| |:|-', prompt.lower()) else False)
    #print(result)
    assert "included" in result.columns, f'included is not in {result.columns}'
   #print(f'result columns {result.columns}')
    result = result.loc[result['included'] == True]
    return result

if __name__ == "__main__":
    extract_artists_fuzzy_test()



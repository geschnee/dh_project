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
    

if __name__ == "__main__":
    extract_artists_fuzzy_test()
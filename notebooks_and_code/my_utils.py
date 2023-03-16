from difflib import SequenceMatcher as SM

def read_lines_as_list(filename):
    result = []
    f = open(filename, "r")
    for x in f.readlines():
      n = x[0:-1]
      if len(n) >= 1:
          result.append(n)
    
    return result

def extract_artists_exact(prompt, artist_dict):
    # artist_dict: 
    # key = artist copy_paste_name
    # value = artist names and pseudonyms as list
    
    artists = []
    prompt = prompt.lower()
    
    for cp_name, aliases in artist_dict.items():
        for name in aliases:
            if name.lower() in prompt:
                artists.append(cp_name)
                continue
    
    return artists


def extract_styles_exact(str, style_names):
    styles = []
    
    for sn in style_names:
        if sn.lower() in str:
            styles.append(sn)
    
    return styles

def artist_in_list(l, artist):
    l = l.tolist()
    assert type(l) == list, f'type is {type(l)}'
    if artist in l:
        return True
    else:
        return False
    
def exact_match_dataframe(df, name):
    result = df.copy()
    result['included'] = result['artists'].map(
       lambda artists: True if name in artists.tolist() else False)
    assert "included" in result.columns, f'included is not in {result.columns}'
    result = result.loc[result['included'] == True]
    return result

def exact_match_dataframe_style(df, name):
    assert 'styles' in df.columns
    
    result = df.copy()
    result['included'] = result['styles'].map(
       lambda styles: True if name in styles else False)
    assert "included" in result.columns, f'included is not in {result.columns}'
    result = result.loc[result['included'] == True]
    return result


def search_prompt_splits(df, str):
    str = str.lower()
    result = df.copy()
    result['included'] = result['prompt'].map(
       lambda prompt: True if str in re.split(';|,|\.| |:|-', prompt.lower()) else False)
    assert "included" in result.columns, f'included is not in {result.columns}'
    result = result.loc[result['included'] == True]
    return result




import my_utils
import time
import pandas as pd

excel_artist_names = my_utils.read_lines_as_list("sources/excel_artists_copy_paste_name.txt")
exact_matches = pd.read_parquet('results/artists_exact_match_large.parquet', engine='pyarrow')
print(exact_matches.dtypes)


cols = ["artist", "mentions"]

artist_mentions =  pd.DataFrame(columns=cols)

starttime = time.time()
c=0
for name in excel_artist_names:
    print(f'{c} {name}',flush=True)
    
    
    c+=1
    
    #if c == 15:
    #      break
    new_row = dict()
    new_row['artist'] = name
    mdf = my_utils.exact_match_dataframe(exact_matches, name)
    #print(mdf)
    new_row['mentions'] = mdf.shape[0]
    
    new_row = pd.Series(new_row)
    #print(new_row)
    
    artist_mentions = pd.concat([artist_mentions, new_row.to_frame().T], ignore_index=True)
    
    duration = time.time() - starttime
    print(f'analysing {c} artists took {duration / 60} minutes',flush=True)
    print(f'time remaining estimate {(duration/c)*(len(excel_artist_names)-c)/60} minutes',flush=True)

artist_mentions.sort_values("mentions", axis=0, ascending=False)
    
artist_mentions.to_csv("results/artist_mentions.csv", escapechar = "\\")
artist_mentions.to_parquet("results/artist_mentions.parquet")
print("finished")

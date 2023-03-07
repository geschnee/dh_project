def visualize_rankings(values_plain, values_artist, artist):
    #artist = name
    import pandas as pd
    
    freqs_df = pd.DataFrame.from_dict(values_plain, orient="index", columns = ["counts_plain"])
    freqs_df.index.name = 'word_plain'

    freqs_df.sort_values("counts_plain", axis=0, ascending=False, inplace=True)
    #freqs_df['length']=freqs_df.word_plain.apply(lambda x: len(x))
    freqs_df.reset_index(inplace=True)
    freqs_sum = freqs_df.counts_plain.sum()
    freqs_df['frequency_plain']=freqs_df.counts_plain.apply(lambda x: x / freqs_sum)

    #print(freqs_df.head(20))

    freqs_artist_df = pd.DataFrame.from_dict(values_artist, orient="index", columns = ["counts_artist"])
    freqs_artist_df.index.name = 'word_artist'

    freqs_artist_df.sort_values("counts_artist", axis=0, ascending=False, inplace=True)
    freqs_artist_df.reset_index(inplace=True)
    freqs_artist_sum = freqs_artist_df.counts_artist.sum()
    freqs_artist_df['frequency_artist']=freqs_artist_df.counts_artist.apply(lambda x: x / freqs_artist_sum)
    #print(freqs_artist_df.head(20))

    result = pd.concat([freqs_df, freqs_artist_df], axis=1)
    print(result.shape)
    print(result.head(20))
    
    
    
    
    
    offset = 0.1 # offset for plt plot text
    word_amount = 40 # amount of words to plot
    words = []
    for index, series in result.iterrows():
        if series.word_plain not in words:
            words.append(series.word_plain)
        if series.word_artist not in words:
            words.append(series.word_artist)
        if len(words)>=word_amount:
            break

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    fig, ax1 = plt.subplots(figsize=(20,6))

    max_x=0
    max_y=0
    x_artist, y_artist =[], []
    x_plain,y_plain=[], []
    x_equal,y_equal=[], []
    for w in words:
        x=result.index[result['word_plain'] == w].tolist()[0] + 1
        #print(x)
        y=result.index[result['word_artist'] == w].tolist()[0] + 1

        if x>max_x:
            max_x = x
        if y>max_y:
            max_y = y
        if x>y:
            #plt.scatter(x,y,color='green', marker= '.', label="higher rank in artist Rutkowski prompts")
            x_artist.append(x)
            y_artist.append(y)
        elif x==y:
            #plt.scatter(x,y,color='black', marker= '.', label="equal rank")
            x_equal.append(x)
            y_equal.append(y)
        else:
            #plt.scatter(x,y,color='red', marker= '.', label="lower rank in artist Rutkowski prompts")
            x_plain.append(x)
            y_plain.append(y)
        plt.text(x+offset, y+offset, f'{w}', horizontalalignment='left', size='medium', color='blue', weight='normal')

    plt.scatter(x_artist,y_artist,color='green', marker= '.', label=f'higher rank in {artist} prompts')
    plt.scatter(x_equal,y_equal,color='black', marker= '.', label="equal rank")
    plt.scatter(x_plain,y_plain,color='red', marker= '.', label=f'lower rank in {artist} prompts')

    t = min(max_x,max_y)
    plt.plot([1,t], [1, t], color = 'lightblue', alpha=0.5)
    #plt.colorbar(mpl.colormaps["coolwarm"], ax1)
    plt.xlabel("ranking in entire dataset")
    plt.ylabel(f'ranking in {artist} prompts')
    plt.title(f'Top {word_amount} words ranking comparison')
    plt.legend()

    plt.show()
    
def visualize_tf_idf_rankings(values_plain, values_artist, artist, ranking_amount):
    #artist = name
    import pandas as pd
    
    freqs_df = pd.DataFrame.from_dict(values_plain, orient="index", columns = ["tf_idf_plain", "query_mentions"])
    freqs_df.index.name = 'word_plain'

    freqs_df.sort_values("tf_idf_plain", axis=0, ascending=False, inplace=True)
    #freqs_df['length']=freqs_df.word_plain.apply(lambda x: len(x))
    freqs_df.reset_index(inplace=True)

    #print(freqs_df.head(20))

    freqs_artist_df = pd.DataFrame.from_dict(values_artist, orient="index", columns = ["tf_idf_artist", "query_mentions"])
    freqs_artist_df.index.name = 'word_artist'

    freqs_artist_df.sort_values("tf_idf_artist", axis=0, ascending=False, inplace=True)
    freqs_artist_df.reset_index(inplace=True)
    

    result = pd.concat([freqs_df, freqs_artist_df], axis=1)
    print(result.shape)
    print(result.head(5))
    print("tail")
    print(result.tail(5))

    
    offset = 0.1 # offset for plt plot text
    word_amount = ranking_amount # amount of words to plot
    words = []
    for index, series in result.iterrows():
        if series.word_plain not in words:
            words.append(series.word_plain)
        if series.word_artist not in words:
            words.append(series.word_artist)
        if len(words)>=word_amount:
            break

    import matplotlib.pyplot as plt
    import matplotlib as mpl
    fig, ax1 = plt.subplots(figsize=(20,6))

    max_x=0
    max_y=0
    x_artist, y_artist =[], []
    x_plain,y_plain=[], []
    x_equal,y_equal=[], []
    for w in words:
        x=result.index[result['word_plain'] == w].tolist()[0] + 1
        #print(w)
        #print(result.index[result['word_artist'] == w].tolist())
        y=result.index[result['word_artist'] == w].tolist()[0] + 1

        if x>max_x:
            max_x = x
        if y>max_y:
            max_y = y
        if x>y:
            #plt.scatter(x,y,color='green', marker= '.', label="higher rank in artist Rutkowski prompts")
            x_artist.append(x)
            y_artist.append(y)
        elif x==y:
            #plt.scatter(x,y,color='black', marker= '.', label="equal rank")
            x_equal.append(x)
            y_equal.append(y)
        else:
            #plt.scatter(x,y,color='red', marker= '.', label="lower rank in artist Rutkowski prompts")
            x_plain.append(x)
            y_plain.append(y)
        plt.text(x+offset, y+offset, f'{w}', horizontalalignment='left', size='medium', color='blue', weight='normal')

    plt.scatter(x_artist,y_artist,color='green', marker= '.', label=f'higher rank in {artist} prompts')
    plt.scatter(x_equal,y_equal,color='black', marker= '.', label="equal rank")
    plt.scatter(x_plain,y_plain,color='red', marker= '.', label=f'lower rank in {artist} prompts')

    t = min(max_x,max_y)
    plt.plot([1,t], [1, t], color = 'lightblue', alpha=0.5)
    #plt.colorbar(mpl.colormaps["coolwarm"], ax1)
    plt.xlabel("ranking in entire dataset")
    plt.ylabel(f'ranking in {artist} prompts')
    plt.title(f'Top {word_amount} words ranking comparison')
    plt.legend()

    plt.show()
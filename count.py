import read
import pandas as pd
from collections import Counter

#import and read previously defined dataframe
data = read.load_data()

#combine all the headlines into one long string, lowercase every words, then split into a list of words
headlines = data['headlines']
new_headline = ''
for hd in headlines:
    new_headline += (' ' + str(hd))
    
split_lowered = new_headline.lower().split()

common = Counter(split_lowered).most_common(100)

if __name__ == "__main__":
    print(common)

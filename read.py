import pandas as pd
import numpy as np
from collections import Counter
import read

def load_data():
    data = pd.read_csv('hn_stories.csv')
    data.columns = ['submission_time', 'upvotes', 'url', 'headlines']
    return data

if __name__ == "__main__":
    
    print(load_data().head())

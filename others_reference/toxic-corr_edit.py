import pandas as pd
import sys
from scipy.stats import ks_2samp

first_file = sys.argv[1]
second_file = sys.argv[2]

def corr(first_file, second_file):
    # assuming first column is `class_name_id`
    first_df = pd.read_csv(first_file, index_col=0)
    second_df = pd.read_csv(second_file, index_col=0)
    class_names = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

    for class_name in class_names:
        # all correlations
        print('\n Class: %s' % class_name)
        print(' Pearson\'s correlation score: %0.6f' %
              first_df[class_name].corr(
                  second_df[class_name], method='pearson'))

corr(first_file, second_file)

import numpy as np
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

def extract_data(message_file):
    data = pd.DataFrame(columns=['Message', 'Spam'])

    # Open the file
    with open(message_file, 'r') as file:
        for line in file:
            if line.split()[0] == 'ham':
                spam = 0
                line = line[4:]
            elif line.split()[0] == 'spam':
                spam = 1
                line = line[8:]
                
            data = data.append([[line, spam]])
    
    return data


###############################################################################
## -------------------------------- Main ----------------------------------- ##
###############################################################################

# Extract the dataframe from the file
data = extract_data('messages.txt')
print(data.head)
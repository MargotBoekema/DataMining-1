# Data Mining Techniques
# Koen Smallegange 
# Margot Boekema 2717237
# april 2023
# 
# This script controls all code
# 
# ---------------------------------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from clean import clean_frame
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from collections import Counter

# define path to data
path = 'data.csv'

# get a clean dataframe and save as csv
df = clean_frame(path)

# use new clean csv for new dataframe
dfc = pd.read_csv('clean.csv')


# # rename the headers if you want 

# df.rename(
#     columns=({ 'Tijdstempel': 'time', 'What is your gender?': 'gender', 'What programme are you in?': 'programme',
#                'Have you taken a course on machine learning?': 'ML course',
#                'Have you taken a course on information retrieval?': 'IR course', 'When is your birthday (date)?': 'birthday',
#                'How many students do you estimate there are in the room?':'student guess',
#                'Did you stand up to come to your previous answer?': 'stand up', 'What is your stress level (0-100)?':'stress level',
#                'Have you taken a course on statistics?': 'statistics course', 'Have you taken a course on databases?' : 'databases course',
#                'I have used ChatGPT to help me with some of my study assignments ': 'used chatGPT',
#                'How many hours per week do you do sports (in whole hours)?': 'sports hours',
#                'Give a random number': 'random number', 'Time you went to bed Yesterday':'bed time',
#                'What makes a good day for you (1)?': 'good day 1', 'What makes a good day for you (2)?': 'good day 2'}),
#     inplace=True,
# )

#Wordcloud

#Combine colums about good days
good_day = dfc[['What makes a good day for you (1)?', 'What makes a good day for you (2)']]
dfc['What makes a good day for you (1)?'] = dfc['What makes a good day for you (1)?'].astype(str)
dfc['What makes a good day for you (2)?'] = dfc['What makes a good day for you (2)?'].astype(str)

# Concatenate the two columns into a single string
text = ' '.join(dfc['What makes a good day for you (1)?'].tolist() + dfc['What makes a good day for you (2)?'].tolist()).lower()

remove_list = ["good", "nice"]
text = remove_words(text, remove_list)

# Create a WordCloud
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(text)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

#Most common words
word_counts = Counter(text.split())
most_common_words = word_counts.most_common(6)
print(most_common_words)
    
       

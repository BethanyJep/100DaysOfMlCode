# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing a passage from Through the Looking Glass
from looking_glass import looking_glass_text
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

# Change text to another string:
text = 'Random sampling is used to select a sample that is unbiased. Within each area, every part of the area must have an equal chance of being chosen. Random sampling with quadrats is used to examine differences between contrasting habitats within an habitat.'

cleaned = re.sub('\W+', ' ', text).lower()
tokenized = word_tokenize(cleaned)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]
# Comment out the print statement below
# print(normalized)

# Define bag_of_looking_glass_words & print:
bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)

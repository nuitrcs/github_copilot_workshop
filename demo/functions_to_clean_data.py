# Module with functions to clean data

# This module contains functions that will be used to clean the text from Reddit posts and their titles
# Cleaning means:
#   remove URLs from the text,
#   lowercasing,
#   keeping only alphanumeric characters,
#   removing stopwords,
#   tokenizing into unigrams, bigrams, and trigrams

# The functions are:
#   remove_urls: removes URLs from a text
#   lowercasing: lowercases a text
#   keep_alphanumeric: keeps only alphanumeric characters from a text
#   remove_stopwords: removes stopwords from a text
#   tokenize_text: tokenizes a text into unigrams, bigrams, and trigrams
#   clean_text: applies all the above functions to a text

# Loading libraries
import re
import nltk
nltk.download('punkt')
nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('english')
nltk.download('wordnet')

# Defining remove_urls function
def remove_urls(text, replacement_text=""):
  """
  Function to remove URLs from a string.

  Inputs:
    text (string)
    replacement_text (string)
  Output: text_without_urls (string)

  Dependencies: re

  Code taken from: https://www.geeksforgeeks.org/remove-urls-from-string-in-python/
  """
  # Define a regex pattern to match URLs
  url_pattern = re.compile(r'https?://\S+|www\.\S+') # https?:// protocol (optional s), \S+ one or more non-white space characters, | or, www\.\S+ URLs starting with www.
  # Use the sub() method to replace URLs with the specified replacement text
  text_without_urls = url_pattern.sub(replacement_text, str(text))
  # Return the text without URLs
  return text_without_urls

# Tests for remove_urls function
test_text_1 = "Check out this cool website: https://www.google.com"
test_text_2 = "Check out this cool website: www.google.com"
assert remove_urls(test_text_1) == "Check out this cool website: "
assert remove_urls(test_text_2) == "Check out this cool website: "
print("All tests for remove_urls function passed.")

# Defining lowercasing function



# # Tests for lowercasing function
# test_text_1 = "Hello, World!"
# test_text_2 = "HELLO, WORLD!"
# test_text_3 = "hello, world!"
# assert lowercasing(test_text_1) == "hello, world!"
# assert lowercasing(test_text_2) == "hello, world!"
# assert lowercasing(test_text_3) == "hello, world!"
# print("All tests for lowercasing function passed.")

# Defining keep_alphanumeric function

# Tests for keep_alphanumeric function

# Defining remove_stopwords function

# Tests for remove_stopwords function

# Defining tokenize_text function

# Tests for tokenize_text function

# Defining clean_text function

# Tests for clean_text function

if __name__ == "__main__":
  print("Module functions_to_clean_data.py ran as a script.")
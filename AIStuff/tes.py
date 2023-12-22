# def extract_values_with_keywords(text, keywords):
#     results = {}
#     for keyword in keywords:
#         index = text.find(keyword)
#         if index != -1:
#             value_start = index + len(keyword)
#             value = text[value_start:].strip()
#             # Extract only until the next comma or end of the string
#             comma_index = value.find(',')
#             if comma_index != -1:
#                 value = value[:comma_index].strip()
#             results[keyword] = value
#     return results

# # Example usage:
# input_text = "Height is about 12-21 inch, Fur color is Brown, Weight arounds 5 kg"
# keywords = ["Height", "Fur color", "Weight"]
# result = extract_values_with_keywords(input_text, keywords)
# print(result)

# def extract_values(text, keywords):
#     results = []
#     for keyword in keywords:
#         index = text.find(keyword)
#         if index != -1:
#             value_start = index + len(keyword)
#             value = text[value_start:].strip()
#             # Extract only until the next comma or end of the string
#             comma_index = value.find(',')
#             if comma_index != -1:
#                 value = value[:comma_index].strip()
#             results.append(value)
#     return results

# # Example usage:
# input_text = "Height: 12-21 inch, Fur color: Brown, Weight: 5 kg"
# keywords = ["Height:", "Fur color:", "Weight:"]
# result = extract_values(input_text, keywords)
# print(result)
# for i, value in enumerate(result):
#     print(f"{i + 1}: {value}")


# Just need another function to extract value of this extracted text, maybe another keywords like this, but make it a tuple of this parameters

# def extract_value_after_keyword(text, keyword):
#     index = text.find(keyword)
#     if index != -1:
#         value_start = index + len(keyword)
#         value = text[value_start:].strip()
#         # Extract only until the next comma or end of the string
#         comma_index = value.find(',')
#         if comma_index != -1:
#             value = value[:comma_index].strip()
#         return value
#     else:
#         return None

# # Example usage:
# input_text = "Height: 12-21 inch, Fur color: Brown, Weight: 5 kg"
# keyword = "Height:"
# result = extract_value_after_keyword(input_text, keyword)
# print(result)

# def extract_keywords(text, keywords):
#     results = []
#     for keyword in keywords:
#         index = text.find(keyword)
#         if index != -1:
#             results.append(keyword)
#     return results

# # Example usage:
# input_text = "Height: 12-21 inch, Fur color: Brown, Weight: 5 kg"
# keywords = ["inch", "brown", "kg"]
# result_variable = extract_keywords(input_text, keywords)

# # Now result_variable contains the extracted keywords
# print(result_variable)

# def extract_words_before_keywords(text, keywords):
#     results = {}
#     words = text.split()
#     for keyword in keywords:
#         try:
#             # Find the index of the keyword in the list of words
#             keyword_index = words.index(keyword)
            
#             # Extract the word immediately before the keyword
#             if keyword_index > 0:
#                 word_before = words[keyword_index - 1].strip()
#                 results[keyword] = word_before
#             else:
#                 # Handle the case where the keyword is the first word
#                 results[keyword] = None
#         except ValueError:
#             # Handle the case where the keyword is not found in the text
#             results[keyword] = None
#     return results

# # Example usage:
# input_text = "The height is 12-21 inch, fur color is Brown, and weight is 5 kg"
# keywords = ["inch,", "is", "kg"]
# result_variable = extract_words_before_keywords(input_text, keywords)

# # Now result_variable contains the words before the keywords
# print(result_variable)

# def remove_words_with_keywords(input_text, keywords):
#     for keyword in keywords:
#         input_text = input_text.replace(keyword, "")
#     return input_text.strip()

# # Example usage:
# input_text = "The quick brown fox jumps over the lazy dog"
# keywords_to_remove = ["quick ", "lazy "]
# result_text = remove_words_with_keywords(input_text, keywords_to_remove)

# print(result_text)

# def process_height(input_text):
#     # Find the position of the word "height"
#     height_index = input_text.lower().find("height")

#     if height_index != -1:
#         # Remove the word "inch" that follows "height"
#         input_text = input_text[:height_index] + input_text[height_index:].replace("inch", "", 1)

#         # Find the word before "inch"
#         before_inch_index = input_text.lower().rfind(" ", 0, height_index)
#         if before_inch_index != -1:
#             word_before_inch = input_text[before_inch_index+1:height_index].strip()
#             return input_text, word_before_inch

#     return input_text, None

# # Example usage:
# input_text = "The height is 12-21 inch, fur color is Brown, and weight is 5 kg"
# result_text, word_before_inch = process_height(input_text)

# print("Processed Text:", result_text)
# print("Word Before Inch:", word_before_inch)

# def process_height(input_text):
#     # Find the position of the word "inch"
#     inch_index = input_text.lower().find("inch")

#     if inch_index != -1:
#         # Find the word before "inch"
#         before_inch_index = input_text.lower().rfind(" ", 0, inch_index)
#         if before_inch_index != -1:
#             word_before_inch = input_text[before_inch_index+1:inch_index].strip()

#             # Remove "inch" from the text
#             input_text = input_text[:before_inch_index] + input_text[inch_index+len("inch"):]

#             return input_text.strip(), word_before_inch

#     return input_text.strip(), None

# # Example usage:
# input_text = "The height is 12-21 inch, fur color is Brown, and weight is 5 kg"
# result_text, word_before_inch = process_height(input_text)

# print("Processed Text:", result_text)
# print("Word Before Inch:", word_before_inch)

# input_string = "apple,orange,banana"

# # Convert the string into an array (list) using a comma as the delimiter
# string_array = input_string.split(',')

# # Print the array
# print(string_array)

import numpy as np

my_list = [1, 2, 3, 4, 5]

# Convert the list to a NumPy array
my_array = np.array(my_list)

# Print the array
print(my_array)

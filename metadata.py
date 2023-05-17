# Read multiline input from the user and store it in 'text'
print("Enter your text to be set as metadata. Enter 'end' to finish:")
lines = []
line = ""
while line.lower() != 'end':
    line = input()
    if line != "" and line != 'end':
        lines.append(line)
text = "\n".join(lines)

# remove symbols
chars_to_remove = ".,;:!?/<>()*&^%$#~`{[]}-_=+\|"
translation_table = str.maketrans("", "", chars_to_remove)
clean_text = text.translate(translation_table)
words = clean_text.split()

# list of words to remove from word doc
stopwords = ["the", "of", "then", "in", "a", "an", "and", "or", "to", "on", "by", "as", "your", "may", "you", "which", "they", "will", "all", "during", "with", "some", "at", "for", "that", "this", "if", "be", "are", "is", "it", "was", "were", "have", "has", "had", "but", "so", "can", "could", "should", "would", "also", "other", "about", "from", "there", "their", "these", "any", "such", "not", "more", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "first", "second", "third", "next", "last", "many", "much", "several", "only", "own", "those", "just", "how", "when", "where", "why", "who", "what", "its", "his", "her", "he", "she", "him", "them", "our", "we", "us", "after", "before", "up", "down", "out", "into", "over", "under", "again", "then", "once", "here", "there", "when", "where", "why", "how", "almost", "always", "never", "sometimes", "usually", "each", "every", "few", "less", "least", "own", "other", "able", "about", "above", "across", "against", "along", "among", "around", "behind", "below", "beneath", "beside", "between", "beyond", "both", "do", "does", "did", "done", "doing", "else", "ever", "far", "former", "latter", "least", "less", "lots", "must", "near", "off", "often", "onto", "perhaps", "quite", "rather", "really", "some", "such", "through", "toward", "towards", "until", "upon", "whatever", "whenever", "wherever", "whether", "while", "whichever", "within", "without", "since", "called"]

# add words to a set using a set comprehension, removes any duplicates due to nature of set
filtered_words_set = {word for word in words if word.lower() not in stopwords}

#convert set to list
filtered_words = list(filtered_words_set)

# Combine the filtered words into a single string and append it to the list
combined_string = ' '.join(filtered_words)
filtered_words.append(combined_string)

# Create a comma-delimited string of the filtered words
comma_separated_words = ', '.join(filtered_words)

print(comma_separated_words)

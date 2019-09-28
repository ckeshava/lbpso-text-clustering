# Reference: Jack Baker, https://blog.cambridgespark.com/tutorial-preprocessing-text-data-a8969189b779

# Text datasets
from bs4 import BeautifulSoup
import nltk
# nltk.download('stopwords')
import sklearn
import re
import string

def pre_process():
	# Load in each data file (zfill pads out integers with leading zeros)
	text_data = []
	for index in range(22):
		filename = 'dataset/reut/reut2-{0}.sgm'.format(str(index).zfill(3))
		with open(filename, 'r', encoding = 'utf-8', errors = 'ignore') as infile:
			text_data.append(infile.read())
	# Print first 300 characters of first file
	# print(text_data[0][:300])

	#================== Tokenization ===========================
	articles = []
	for textfile in text_data:
		# Parse text as html using beautiful soup
		parsed_text = BeautifulSoup(textfile, 'html.parser')
		# Extract article between <BODY> and </BODY> and convert to standard text. Add to list of articles
		articles += [article.get_text() for article in parsed_text.find_all('body')]
	# print the first article as an example
	# print("\n\n <================== Sample ==================> " + " \n" + articles[0])

	# Convert each article to all lower case
	articles = [article.lower() for article in articles]

	# Strip all punctuation from each article
	# This uses str.translate to map all punctuation to the empty string
	table = str.maketrans('', '', string.punctuation)
	articles = [article.translate(table) for article in articles]

	# Convert all numbers in the article to the word 'num' using regular expressions
	articles = [re.sub(r'\d+', 'num', article) for article in articles]
	# Print the first article as a running example
	# print("\n\nStemming ==================> " + " \n" + articles[0])

	#================== Stop-word removal ===========================
	# Create stopwords list, convert to a set for speed
	# stopwords = set(nltk.corpus.stopwords.words('english') + ['reuter', '\x03'])
	stopwords = set(nltk.corpus.stopwords.words('english'))
	articles = [[word for word in article.split() if word not in stopwords] for article in articles]

	#================== Stemming ===========================
	stemmer = nltk.stem.PorterStemmer()
	articles = [" ".join([stemmer.stem(word) for word in article]) for article in articles]
	# print the first article as a running example
	print("\n\n <================== Stop-word-removal ==================> " + " \n" + articles[0])

	#================== Term weighting ===========================
	# Generate bag of words object with maximum vocab size of 1000
	# counter = sklearn.feature_extraction.text.CountVectorizer(max_features = 1000)
	# Get bag of words model as sparse matrix
	# bag_of_words = counter.fit_transform(articles)
	# Generate tf-idf object with maximum vocab size of 1000
	tf_counter = sklearn.feature_extraction.text.TfidfVectorizer(max_features = 1000)
	# Get tf-idf matrix as sparse matrix
	tfidf = tf_counter.fit_transform(articles)
	# Get the words corresponding to the vocab index
	print("\n\n <================== Features ================> \n")
	print(tf_counter.get_feature_names())

if __name__ == "__main__":
	pre_process()


# import scipy.io
# mat = scipy.io.loadmat('.mat')
# print(mat)
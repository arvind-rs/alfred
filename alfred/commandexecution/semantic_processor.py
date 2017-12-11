
# The semantic_processor is responsible for taking the input sentence and comparing it with the predefined sentence list using DeepSiam model
# Author: ArvindRS
# Date: 04/07/2017

from keras.models import load_model
import numpy, time, csv, re
import gensim
import keras
from keras.preprocessing.sequence import pad_sequences


def tokenize(sent):
	'''Return the tokens of a sentence including punctuation.

	>>> tokenize('Bob dropped the apple. Where is the apple?')
	['Bob', 'dropped', 'the', 'apple', '.', 'Where', 'is', 'the', 'apple', '?']
	'''
	return [x.strip() for x in re.split('(\W+)?', sent) if x.strip()]

def create_word2vec_model(sentences):
	# Function to create a word2vec model using gensim

	model = gensim.models.Word2Vec(sentences, min_count=1, sg = 0, size = vector_dim)

	return model

def load_word2vec_model(filename):
	# Function to load the saved gensim model

	model = gensim.models.Word2Vec.load(filename)

	return model

def vectorize_sentences(sentence_list, model):
	# This function will convert a sentence into a sequence of word vectors

	sequence_list = []

	for sentence in sentence_list:
		sequence = []
		tokens = tokenize(sentence)
		for word in tokens:
			word_vector = model[word]
			sequence.append(word_vector)
		sequence_list.append(sequence)
		
	return sequence_list

def main(input_text):
	# Main function

	# Load the word2vec model
	filename = 'models/word2vec_model'
	word2vec_model = load_word2vec_model(filename)

	# Load the model
	model = load_model('models/regression_model.h5')

	# Define sentence_1 and sentence_2
	sentence_1_list = ['A brown dog is attacking another animal in front of the tall man in pants','Two dogs are wrestling and hugging','A person is wearing a straw hat and smoking a cigarette','A person in a black jacket is doing tricks on a motorbike']
	sentence_2_list = ['A brown dog is attacking another animal in front of the man in pants','A brown dog is attacking another animal in front of the tall man in pants','A dog is near the red ball in the air','A man in a black jacket is doing tricks on a motorbike']

	# Create word vectors of the sentences
	sentence_1_vector = vectorize_sentences(sentence_1_list,word2vec_model)
	sentence_2_vector = vectorize_sentences(sentence_2_list,word2vec_model)
	sentence_1_vector = pad_sequences(sentence_1_vector, padding = 'post', dtype = 'float32', truncating='post', maxlen=40)
	sentence_2_vector = pad_sequences(sentence_2_vector, padding = 'post', dtype = 'float32', truncating='post', maxlen=40)

	# Make prediction
	predictions = model.predict([sentence_1_vector,sentence_2_vector])
	for s1,s2,p in zip(sentence_1_list,sentence_2_list,(predictions * 5)):
		print s1,s2,p





if __name__ == '__main__':
	input_text = "A brown dog is attacking another animal in front of the tall man in pants"
	main(input_text)
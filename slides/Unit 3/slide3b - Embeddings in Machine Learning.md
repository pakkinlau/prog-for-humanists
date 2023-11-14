## Understanding Embeddings
Embeddings in the context of machine learning are numerical, low-dimensional representations of high-dimensional data. They are primarily used to transform categorical variables into a form that can be input into machine learning algorithms. 

These numerical representations, known as embeddings, are capable of capturing complex relationships between different data points while preserving the semantics of the original data. This ability makes them invaluable across numerous fields including Natural Language Processing (NLP), computer vision, and recommendation systems. 

In NLP, for instance, embeddings are used to convert words, sentences, or even entire documents into vectors of real numbers. These are respectively known as word, sentence, and document embeddings.

## Classical Embeddings: One-hot Embedding / Bag-of-words (BoW)
One of the earliest embedding models is the one-hot embedding. This model employs a 1-to-1 mapping to translate each unique word into a binary vector. In this binary vector, all elements are zero except for one that corresponds to the index of the word in the dictionary.

One limitation of one-hot embeddings is the creation of high dimensionality, especially with large vocabularies. Moreover, this method doesn't capture semantic relationships between words. The vectors for "dog" and "puppy", for example, would be just as different as the vectors for "dog" and "apple", despite the clear semantic relationship between "dog" and "puppy".

![One Hot Encoding](https://miro.medium.com/max/1200/1*YEJf9BQQh0ma1ECs6x_7yQ.png)

## Capturing Word Importance: TF-IDF
Term Frequency-Inverse Document Frequency (TF-IDF) is an improvement over the BoW model. It not only considers the frequency of a word in a specific document (Term Frequency) but also how unique the word is across all documents (Inverse Document Frequency). 

The idea of TF-IDF is to assigns more weight to words that occur frequently in a particular document but rarely in others, making them potentially important for classification. Despite this advantage, TF-IDF still struggles with capturing semantic relationships between words.

- Figure: Illustration of frequency data collected in a corpus. The application of TF-IDF highlights the elevated significance of the term "Romeo" within the document where it is featured, emphasizing its importance over the mere occurrence of the word "Romeo." in that document. 
![](../../Pasted%20image%2020231115055614.png)

## Capturing Semantic Relationships in Word Embeddings
The limitations of the aforementioned methods led to the development of more advanced techniques that map words into meaningful indices expressing semantic relationships. 

Word embeddings represent words as vectors in a high-dimensional space where the spatial relationships between vectors capture semantic and syntactic similarities. This provides a dense and expressive representation of words, which is more efficient and capable of capturing subtleties than traditional BoW or TF-IDF representations.

There are various algorithms to determine these word embeddings. These include methods like Word2Vec, GloVe (Global Vectors for Word Representation), and FastText, each with their own strengths and weaknesses. They will be discussed in more detail in the following sections.

![](../../Pasted%20image%2020231115053347.png)
- Figure: Words with similar meaning form clusters in 2D PCA projection of word embedding. X and y axis of this 2D (low dimension) figure tries to capture the most significant components from high dimensional word embeddings)
- Source: https://www.researchgate.net/figure/2D-PCA-projection-of-word-embeddings-Five-different-word-clusters-are-shown_fig2_332892222

![](../../Pasted%20image%2020231115060140.png)
- Figure: Relational properties of the GloVe vector space. 

---
# Two types of word embeddings

##  Static embeddings:
- Static embeddings, also known as word embeddings, are algorithms that represent words in a high-dimensional vector space where semantically similar words are placed close together. 
- They were developed approximately around the years 2013 to 2015. 
- Advantage:
	- Static embeddings are context-independent, meaning each word in the language is assigned a fixed vector regardless of its context. This simplifies the process and reduces computational load. However, this can also be a limitation as words often have different meanings based on their context, which static embeddings fail to capture.
- Examples:
	- Word2Vec, developed by researchers at Google in 2013.
	- GloVe (Global Vectors for Word Representation), introduced by Stanford researchers in 2014.
- These models are trained on large corpora and create a static word embedding for each word in the vocabulary, capturing semantic and syntactic properties of the words. They are widely used for tasks like text classification, semantic similarity, and even as a starting point for more complex models.
- The details of static embeddings are not covered in this course. 

## Contextual embeddings
- Definition of contextual embedding:
	- Contextual embeddings are representations of words that are dynamically computed based on their context, i.e., the words around them in a sentence or a document. 
- The first contextual embedding model, Google's BERT) published in 2018. 
- Compared to static embeddings, contextual embeddings are dynamic and capable of capturing the context in which words appear. This means that the same word can have different embeddings based on its surrounding words, allowing the model to handle polysemy (words with multiple meanings) and other complex linguistic phenomena.
- Contextual embeddings are generated by models that process text sequentially, thereby considering the entire context (words that appear before and after the target word) to generate the word's representation. 
- Examples:
	- BERT (Bidirectional Encoder Representations from Transformers), developed by Google AI in 2018.
	- ELMo (Embeddings from Language Models), introduced by Allen Institute for AI in 2018.
	- RoBERTa (A Robustly Optimized BERT Pretraining Approach), developed by Facebook AI in 2019.
	- GPT (Generative Pre-trained Transformers), introduced by OpenAI. GPT-1 in 2018, then followed by improved versions GPT-2 in 2019 and GPT-3 in 2020.
- These models generate embeddings that are sensitive to the context, greatly improving the performance on a wide range of natural language processing tasks compared to static embeddings. They have been critical in advancing the state-of-the-art in tasks such as question answering, named entity recognition, and sentiment analysis.

---
## Bias in word embeddings

- There are biases and tendency of interpreting words in different ways across different ages. This properties also showing in word embedding models. 
- Recent research focuses on the way to try to remove these biases. While those debasing may reduce bias in embeddings, they do not eliminate it.
- Historical embeddings are also being used to measure biases in the past. 
- Example insights:
	- Analyzing the cosine distance of words to see the association between classes in the society - For example, examine the distance between word "librarian" to different names of various ethnicities or genders across the 20th century. 
	- Replicating old surveys of ethnic stereotypes - Such as measuring the adjectives like "industrious" and ethnicity such as "Chinese" in the corpus of 1930s. 

![](../../Pasted%20image%2020231115060348.png)
- Figure: Semantic change of 3 words in word2vec vectors. If the underlying corpus collection is different, the values in the embeddings of word would be different. 


import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import BartTokenizer, BartForConditionalGeneration
import numpy as np
from nltk.tokenize import sent_tokenize

# Download NLTK resources
nltk.download('punkt')

def summarize_with_tfidf(text, top_n=3):
    sentences = sent_tokenize(text)
    if len(sentences) == 0:
        return "No content available for summarization."

    organized_sent = {k: v for v, k in enumerate(sentences)}

    tfidf = TfidfVectorizer(stop_words='english')
    sentence_vectors = tfidf.fit_transform(sentences)
    sent_scores = np.array(sentence_vectors.sum(axis=1)).ravel()

    top_n_sentences = [sentences[index] for index in np.argsort(sent_scores, axis=0)[::-1][:top_n]]
    mapped_sentences = sorted([(sentence, organized_sent[sentence]) for sentence in top_n_sentences], key=lambda x: x[1])
    
    return " ".join([element[0] for element in mapped_sentences])

def summarize_with_bart(text):
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')

    inputs = tokenizer([text], max_length=1024, return_tensors='pt', truncation=True)
    summary_ids = model.generate(inputs['input_ids'], num_beams=4, max_length=150, early_stopping=True)
    
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)

import nltk

def information_Extractor():

    documents = ['I want to build a football news verification bot. it will detect genuine news from the internet, while ignoring the rumors.'
                 , 'i will build it using nltk. i will also use stanford NLTK', 'i will use Python on top of-course.']

    #print(nltk.sent_tokenize(documents))
    sentences=[]    
    for doc in documents:
        sent=nltk.sent_tokenize(doc)
        sent=[nltk.word_tokenize(s) for s in sent]
        sent=[nltk.pos_tag(s) for s in sent]
        sentences.append(sent)

    #cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
        cp = nltk.RegexpParser('CHUNK: {<NN><NN>}')
    cp.parse(sentences[0][0])
    
    for sent in sentences:
        for ins in sent:
            tree = cp.parse(ins)
            for subtree in tree.subtrees():
                if subtree.label() == 'CHUNK': print(subtree)

information_Extractor()


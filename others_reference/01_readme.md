

## 01_0.9772_NB-SVM strong linear baseline_Jeremy Howard
(https://www.kaggle.com/jhoward/nb-svm-strong-linear-baseline)

columns: id, comment_text
toxic, severe_toxic, obscene, threat, insult, identity_hate (6 different categorization: 0 or 1)

(1) Count the number of strings (mean:394) 

    train.comment_text.str.len()

(2) Create a new column <b>train['none']</b> : if neither 6 categorization, put 1 in train['none'] 

~~(3) He mentioned that there are a few empty comments, and fill the values as "unknown", but I couldn't find any Null value when I used the task:~~

    train.isnull().values.any()
    
 (4) <b>Tfidf Vectorizer</b>
 
     vec = TfidfVectorizer(ngram_range=(1,2), tokenizer=tokenize,
               min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
               smooth_idf=1, sublinear_tf=1 )
 
 one. CountVectorizer implements both tokenization and occurence counting in single class:
 
    from sklearn.feature_extraction.text import CountVectorizer
    vectorizer = CountVectorizer()
    vectorizer                     
    CountVectorizer(analyzer=...'word', binary=False, decode_error=...'strict',
        dtype=<... 'numpy.int64'>, encoding=...'utf-8', input=...'content',
        lowercase=True, max_df=1.0, max_features=None, min_df=1,
        ngram_range=(1, 1), preprocessor=None, stop_words=None,
        strip_accents=None, token_pattern=...'(?u)\\b\\w\\w+\\b',
        tokenizer=None, vocabulary=None)
        
     corpus = [
    ...     'This is the first document.',
    ...     'This is the second second document.',
    ...     'And the third one.',
    ...     'Is this the first document?',  
     ... ]
    X = vectorizer.fit_transform(corpus)
    X                              
    <4x9 sparse matrix of type '<... 'numpy.int64'>'
    with 19 stored elements in Compressed Sparse ... format>
    >>> X.toarray()           
    array([[0, 1, 1, 1, 0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 2, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0, 1]]...)

two. TfidfTransformer
In a large text corpus, some words will be very present (e.g. “the”, “a”, “is” in English) hence carrying very little meaningful information about the actual contents of the document. If we were to feed the direct count data directly to a classifier those very frequent terms would shadow the frequencies of rarer yet more interesting terms.

In order to re-weight the count features into floating point values suitable for usage by a classifier it is very common to use the tf–idf transform.

three. <b>TfidVectorizer</b> combines all the options of CountVectorizer and TfidfTransformer in a single model

    from sklearn.feature_extraction.text import TfidfVectorizer
    vectorizer = TfidfVectorizer()
    vectorizer.fit_transform(corpus)
    <4x9 sparse matrix of type '<... 'numpy.float64'>'
    with 19 stored elements in Compressed Sparse ... format>
    
More details : http://scikit-learn.org/stable/modules/feature_extraction.html

His code:

    vec = TfidfVectorizer(ngram_range=(1,2), tokenizer=tokenize,
               min_df=3, max_df=0.9, strip_accents='unicode', use_idf=1,
               smooth_idf=1, sublinear_tf=1 )
    trn_term_doc = vec.fit_transform(train[COMMENT])
    test_term_doc = vec.transform(test[COMMENT])
    

(5) <b>Applying Naive Bayes + LogisticRegression</b>

    def naive_bayes(y_i, y):
        p = x[y==y_i].sum(0)
        return (p+1) / ((y==y_i).sum()+1)
        
    def get_mdl(y):
        y = y.values
        print(naive_bayes(1,y))
        r = np.log(naive_bayes(1,y) / naive_bayes(0,y))
        m = LogisticRegression(C=4, dual=True)
        x_nb = x.multiply(r)
        return m.fit(x_nb, y), r

    preds = np.zeros((len(test), len(label_cols)))
    for i, j in enumerate(label_cols):
        print('fit', j)
        m,r = get_mdl(train[j])
        preds[:,i] = m.predict_proba(test_x.multiply(r))[:,1]

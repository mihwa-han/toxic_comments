## Only use TfidfVectorizer - use these features to fit Logistic Regression
## (1) analyzer = 'word', ngram_range = (1,1)
## (2) analyzer = 'char', ngram_range= (2,6)

The sample code is here:

    word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='word',
    token_pattern=r'\w{1,}',
    stop_words='english',
    ngram_range=(1, 2),
    max_features=10000)
    word_vectorizer.fit(all_text)
    train_word_features = word_vectorizer.transform(train_text)
    test_word_features = word_vectorizer.transform(test_text)
    
    char_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    strip_accents='unicode',
    analyzer='char',
    stop_words='english',
    ngram_range=(2, 6),
    max_features=50000)
    char_vectorizer.fit(all_text)
    train_char_features = char_vectorizer.transform(train_text)
    test_char_features = char_vectorizer.transform(test_text)
    
    train_features = hstack([train_char_features, train_word_features])
    test_features = hstack([test_char_features, test_word_features])
    
    model.fit(train_features, train_target) ## train_target = target value for each class

## 1. fillna
## 2. Tokenizer

text -> toknizer.fit_on_text(list)
list_token = tokenizer.text_to_sequences
sequence.pad_sequence(list_token,maxlen=maxlen)

    tokenizer = text.Tokenizer(num_words=max_features)
    tokenizer.fit_on_texts(list(list_sentences_train))
  
    list_tokenized_train = tokenizer.texts_to_sequences(list_sentences_train)
    list_tokenized_test = tokenizer.texts_to_sequences(list_sentences_test)

    X_t = sequence.pad_sequences(list_tokenized_train, maxlen=maxlen)
    X_te = sequence.pad_sequences(list_tokenized_test, maxlen=maxlen)
    
## 3. model = get_model(): (Bidirection LSTM)
Input
Embedding
Bidirectional(LSTM(50))(x)
GlobalMaxPool1D()(x)
Dropout(0.1)(x)
Dense(50)(x)
Dropout(0.1)(x)
Dense(6)(x)

    model.fit(x,y)
    model.load_weights(file_path)
    yu_test=model.predict(x_Test)

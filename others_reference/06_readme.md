## 1. Tokenizer

tokenizer.fit_on_texts
tokenizer.texts_to_sequences
sequence.pad_sequences

## 2. Embedding file : crawl-300d-2M.vec -> embeddings_index -> embedding_vector --> embedding_matrix

## 3. Model
Input
Embedding (<b>weights=[embedding_matrix)</b>)(input)
SpatialDropout1D(0.2)(X)
Bidirectional(GRU(80))(x)
GlobalAveragePooling1D()(x)
GlobalMaxPooling1D()(x)
Dense(6)(conc)

## train-validation set 95:5

## three differnce with 06 kernel

1. using different pre-trained embedding model
"../input/glove.840B.300d.txt" -> maybe this is better

2. change characters to lower characters.... ( i dunno how much this is useful)

    raw_text_train = X_train["comment_text"].str.lower()
    raw_text_valid = X_valid["comment_text"].str.lower()
    raw_text_test = test["comment_text"].str.lower()

3. after GRU layer, add CNN1D

    x = Conv1D(64, kernel_size = 2, padding = "valid", kernel_initializer = "he_uniform")(x)
   
etc... more numbers of filters...? more epochs... overall... looks better... should be


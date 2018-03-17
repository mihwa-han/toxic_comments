## Same to other kernels, but different model -> Use CNN2D...!! (Note that this is not image data!!! COOL)

filter_sizes = [1,2,3,5]
num_filters = 32

    def get_model():    
        inp = Input(shape=(maxlen, ))
        x = Embedding(max_features, embed_size, weights=[embedding_matrix])(inp)
        x = SpatialDropout1D(0.4)(x)
        x = Reshape((maxlen, embed_size, 1))(x)

        conv_0 = Conv2D(num_filters, kernel_size=(filter_sizes[0], embed_size), kernel_initializer='normal',
                                                                                        activation='elu')(x)
        conv_1 = Conv2D(num_filters, kernel_size=(filter_sizes[1], embed_size), kernel_initializer='normal',
                                                                                        activation='elu')(x)
        conv_2 = Conv2D(num_filters, kernel_size=(filter_sizes[2], embed_size), kernel_initializer='normal',
                                                                                        activation='elu')(x)
        conv_3 = Conv2D(num_filters, kernel_size=(filter_sizes[3], embed_size), kernel_initializer='normal',
                                                                                        activation='elu')(x)

        maxpool_0 = MaxPool2D(pool_size=(maxlen - filter_sizes[0] + 1, 1))(conv_0)
        maxpool_1 = MaxPool2D(pool_size=(maxlen - filter_sizes[1] + 1, 1))(conv_1)
        maxpool_2 = MaxPool2D(pool_size=(maxlen - filter_sizes[2] + 1, 1))(conv_2)
        maxpool_3 = MaxPool2D(pool_size=(maxlen - filter_sizes[3] + 1, 1))(conv_3)

        z = Concatenate(axis=1)([maxpool_0, maxpool_1, maxpool_2, maxpool_3])   
        z = Flatten()(z)
        z = Dropout(0.1)(z)

        outp = Dense(6, activation="sigmoid")(z)

        model = Model(inputs=inp, outputs=outp)
        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        return model

    model = get_model()

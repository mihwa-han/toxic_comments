## This is an interesting kernel to see.

## use logistic regression, but do some feature engineering before

### (1) stemmed
am, are, is $\Rightarrow$ be 
car, cars, car's, cars' $\Rightarrow$ car
studies => studi
studying => study

### (2) lemmatized
studies=>study
studying=>studying

## use TfidfVectoizer (word and char)

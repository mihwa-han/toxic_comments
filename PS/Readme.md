## It is time to work!!!

## 03/09/2018
- Ran Logistic Regression kaggle kernel -  using words n char ngrams -> KaggleClone_Logistic.ipynb

## 03/11/2018
- Tried running this kernel https://www.kaggle.com/ogrellier/wordbatch-fm-ftrl-using-mse-lb-0-9804 
- the wordbatch package is not compatible on my mac, ran it in pieces on kaggle itself. (Takes more than 60 minutes to run on kaggle)
- Took a weighted average between the Logistic Model and this one - LB .9814

## 03/16/2018
- Took the preprocessed data files (without any punctuation) into an xgboost implementation. The CV for toxic and obscene were .988 approx. Created a new submission file - used the predictions for these two categories from this xgb implementation and the predictions for others from the blend of low correlation models (LB .9860). The final submission only reached .9833 :( 

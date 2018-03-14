## It is time to work!!!

## 03/12/2018 (0.9859)
- start to pick Top20 kernels and run them.
- The best kernel so far with a single model is 15th BI GRU CNN (0.9839) and 20th (0.9837) Bidirectional LSTM with Convolution.
- Today's best kernel - 01(nb_svm:0.9772) + 03(logistic:0.9792) + 15(GRU_CNN:0.9839) + 18(LGBM) + 20(LSTM) : 0.9859

[plan]
- ~~use 5 submissions every day (although there is no kernel, rerun old kernel to check the consistent (with different seed. need to carefully choose ... don't waste the limitation of submission)
- pick TOP30 kernels and stop to copy other kernels. (3/12-3/13)
- Calculate model correlation : https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/discussion/50827 (3/14)~~
- organize by different model category and try to find the best combination (3/15)
- make my own kernel (3/16 - 3/18)
- decide the final kernel carefully (3-19 - 3/20)


## 03/11/2018 (0.9847)
- submit several results from TOP10 kernels.
- best score is from 09th kernel (Toxic Avenger by the1owl) : 0.9814 - this is also based on the result of 08, which means 01 + 03 + 07 + 09 
       
- combine two kernels (03 + 06 + 09) : got the best score (0.9847) 
- next best score is 03 + 09:0.9828 next-next best score is from 03+08:0.9826

## 03/10/2018
- pick TOP10 kernels (put them in the other folder) and run most of them (put the public score in the title).
- start to learn from the first kernel.
- <b>TfidfVectorizer</b> - super cool package
- using <b>Naive Bayes feature</> - need to study more

## 03/09/2018 (0.9809 from 8th kernel)
- Starting this project!!


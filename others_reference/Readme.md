## Others' scripts!
_______

Let's learn from others!!! Always excited to learn :D


## 01_0.9772_NB-SVM strong linear baseline_Jeremy Howard
(https://www.kaggle.com/jhoward/nb-svm-strong-linear-baseline)

columns: id, comment_text
toxic, severe_toxic, obscene, threat, insult, identity_hate (6 different categorization: 0 or 1)

(1) ount the number of strings (mean:394) 

    train.comment_text.str.len()

(2) create a new column <b>train['none']</b> : if neither 6 categorization, put 1 in train['none'] 

~~(3) He mentioned that there are a few empty comments, and fill the values as "unknown", but I couldn't find any Null value when I used the task:~~

    train.isnull().values.any()
    
 

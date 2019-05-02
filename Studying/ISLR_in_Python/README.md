# An introduction to Statistical Learning with Applications in R
---

So, this is a very famous book of data science much recommended by companies that are hiring right now.

Thus, I've decided to tackle the this book, but, instead of using R, I will try to adapt it to Python.

Datasets used in the book can be found at [Stat Learning](www.StatLearning.com) website, ISLR, MASS libraries in R or in **/data/raw** in this repo. To export it as csv, I went to R and used the command `write.csv2(Dataset, file='name.csv')` with the libraries ISLR and MASS activated.

There are two datasets (Khan, NCI60) that I haven't download yet because they are not regular tables. For instance, Khan has the data splited in X_train, Y_train, X_test, Y_test lists. So I still have to figure out how to make python read these R lists.
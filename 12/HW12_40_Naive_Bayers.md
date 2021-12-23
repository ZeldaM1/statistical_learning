# program discription
Implement the naive Bayes algorithm (with Laplace smoothing and
adjustable α) by yourself. Use the dataset in Table 3 for training, and
x = (1, M ) for test. Give the results when α = 0 and α =1. 
# training data 
```
[[1, "S", -1], 
[1, "M", -1], 
[1, "M", 1],
[1, "S", 1],
[1, "S", -1], 
[2, "S", -1],
[2, "M", -1], 
[2, "M", 1], 
[2, "L", 1],
[2, "L", 1], 
[3, "L", 1]])
```
# testing data 
```
 [1, "M"]
```
# solution 
see HW12_40_Naive_Bayers.py

# results
```
alpha = 0:
Y=1： 0.35714285714285715
Y=-1： 0.6428571428571429
test dataset is categorized into -1 class


alpha = 1:
Y=1： 0.40875912408759124
Y=-1： 0.5912408759124088
test dataset is categorized into -1 class

```
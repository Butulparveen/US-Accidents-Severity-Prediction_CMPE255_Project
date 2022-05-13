# US Accidents Severity Prediction	


### Team Members :
### Varun Reddy Yedulla
### Butul parveen
### Varun Teja Maguluri
### Varun Raj Badri

## Dataset - https://www.kaggle.com/datasets/sobhanmoosavi/us-accidents

### Introduction:
Road accidents can be caused by a variety of meteorological and topographical factors, in addition to human mistake. Due to slick roadways, a 100-car pileup occurred recently. Road accidents are more likely under certain circumstances. Several research have been undertaken in order to acquire sufficient data on elements that may contribute to the likelihood of accidents. Nonetheless, "What are the major elements that cause road accidents?" and "How can we forecast them?" remain open questions. We propose analyzing a road accident data set collected in the United States from February 2016 to December 2021 in order to learn about the primary elements that cause accidents and maybe forecast them with a good accuracy.

### Tools / Technologies:
Programming language: Python

Libraries used: NumPy, SciPy, Pandas, Scikit-Learn.

Tools: Jupyter Notebook, Google Colab 

Framework : Flask

### Preprocessing:
The dataset includes 47 columns with severity as the output variable. This includes accidents data from 49 states. We have analysed the data and noticed that it has null values. We are have dropped the columns with. In preprocessing we have visualized accident data from all states. And also visualized top 10 accident states in US and top 10 accident cities in Us Analyzing accidents per year and per month. We have analysed severity by day of the week, accidents count by day and accidents count by day of the week. We have plotted Accidents and severity per hour of the day. When we have visualised the output varible, one of the output label ie., severity 2 is doiminating over all the output labels. We have also plotted the sevrity labels by years. We have plotted distribution of temperature, humidity and pressure with severity. We have plotted the hotspots of the accidents severity on the US map. We have label encoded the columns which are categorical. We have normalised the columns of the dataset using Standard scalar. And we have taken a split of 0.75 training samples and 0.25 testing samples. We have developed four machine learning models, They are:
1. Logistic Regression
2. Decision Tree
3. Convolutional Neural Network 
4. Random Forest

## Preprocessing outputs:

![image](https://user-images.githubusercontent.com/55958864/167739142-9a8eec86-e4bd-4ab1-81ed-2b568c8f6289.png)

![image](https://user-images.githubusercontent.com/55958864/167739178-3a0b5d24-0758-459b-8230-a7e27e400022.png)

![image](https://user-images.githubusercontent.com/55958864/167739241-a01c9c5e-b9f2-4e3b-a99c-738a35fcb9cf.png)

![image](https://user-images.githubusercontent.com/55958864/167739262-4bb2e469-4b6a-4fe9-a659-c457f369611e.png)

![image](https://user-images.githubusercontent.com/55958864/167739314-af578109-f006-4e36-a679-7f7ca42495d5.png)

![image](https://user-images.githubusercontent.com/55958864/167739330-aa458baa-69ce-4bcb-a70d-18a44859dd89.png)

![image](https://user-images.githubusercontent.com/55958864/167739360-c253f6bd-4510-4e6e-9c84-d486f18bd0df.png)

![image](https://user-images.githubusercontent.com/55958864/167739383-9e8718e3-520e-4734-890d-55be5dc697c5.png)

![image](https://user-images.githubusercontent.com/55958864/167739401-e330c813-a693-416c-adf6-24294b93c6c8.png)

![image](https://user-images.githubusercontent.com/55958864/167739408-ba25964a-cc00-42d7-a9f4-dceec22543d8.png)

![image](https://user-images.githubusercontent.com/55958864/167739417-40b531c8-ae71-40f8-9ebf-a8b4cbbb0dbf.png)

![image](https://user-images.githubusercontent.com/55958864/167739434-d2ac7b8a-c84c-40f5-985f-fcc2ceb5ef98.png)

### Model Outputs:

## Results of Logistic Regression

### Accuracy    :  0.8946384706560979

### Recall      :  0.8946384706560979

### Precision   :  0.8539889299254698

### Confusion Matrix   : 

[[   325   6071      0      3]

 [   267 589469   5089    889]
 
 [    57  30526   3013    309]
 
 [    39  25701   1006   1207]]
 
 

## Results of Decision Tree


### Accuracy    :  0.9040967150673749

### Recall      :  0.9040967150673749

### Precision   :  0.9061424711701926

### Confusion Matrix   : 

[[  4309   1440    484    166]

 [  1456 566478  14603  13177]
 
 [   455  13523  16628   3299]
 
 [   170  11576   3328  12879]]
 
![image](https://user-images.githubusercontent.com/55958864/167756485-b1e527b2-f5d0-44ec-b8b8-516901285c2b.png)


## Results of Neural Network

### Accuracy    :  0.9203564613514746

### Recall      :  0.9203564613514746

### Precision   :  0.9060166938882748

### Confusion Matrix   : 

[[  3384   2676    281     58]

 [   663 588052   3414   3585]
 
 [   349  20712  10608   2236]
 
 [   219  17026   1662   9046]]
 
 
## Results of Random Forest

### Accuracy    :  0.9039777339672967

### Recall      :  0.9039777339672967

### Precision   :  0.901722354710279

### Confusion Matrix   : 

[[  5275   1066     57      1]

 [  4118 583827   7651    118]
 
 [   524  24230   9111     40]
 
 [   142  13008  12801   2002]]



### API CALL

![Screenshot (411)](https://user-images.githubusercontent.com/55958864/167752993-5d4e1439-9936-4e39-a7ba-ed57bf7158a5.png)


### Learnings and future scope:  
From the four models thet we developed ie., logistic regression, decision tree, neural network and random forest, neural network has outperformed with an accuracy greater than 92% on this huge and imbalanced dataset. The future scope of this is we can built an application where we can guild users to go through areas which are less prone to accidents or we can notify the users which are highly accident prone.

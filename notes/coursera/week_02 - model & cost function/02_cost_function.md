# Cost Function
---

1. We can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

> * **J(θ<sub>0</sub>θ<sub>1</sub>)** 
    = 1/2m*(**Σ**<sup>m</sup><sub>i≡1</sub>(y<sub>i</sub> - y<sub>i</sub>)<sup>2</sup>) 
    = 1/2m*(**Σ**<sup>m</sup><sub>i≡1</sub>(**h**θ(**x**<sup>(i)</sup>) - **y**<sup>(i)</sup>)<sup>2</sup>)

* To break it apart:
    * it is 1/2x, where **x** is the mean of the squares of (**h**θ(**x**<sup>(i)</sup>) - **y**<sup>(i)</sup>)
    * or the difference between the predicted value and the actual value.


* This function is otherwise called the *"Squared error function"*, or *"Mean squared error"*. 
  * The mean is halved (1/2) as a convenience for the computation of the **gradient descent**, as the derivative term of the square function will cancel out the 1/2 term. 

  * This image summarizes what the cost function does:
![img_01.png](img_01.png)

## Linear regression

---

* Minimize over θ<sub>0</sub>θ<sub>1</sub> -- 1/**2m** that causes [2](2) to be minimized
* Find the values of θ<sub>0</sub> & θ<sub>1</sub>, such that the average of 1 over 2m (1/2m) times the sum of square errors between the predictions of the training set minus the actual values of the house is minimized 

- Sum training set 
    - S*1* = (**h**θ(**x**<sup>(i)</sup>) - **y**<sup>(i)</sup>)<sup>2</sup>
    - Σ<sup>m</sup><sub>i≡1</sub>(S*1*) where
        1. m = number of training examples
        2. [2]. **h**θ(**x**<sup>(i)</sup>) = θ<sub>0</sub>θ<sub>1</sub>x<sup>(i)</sup> 

- Cost function:
    - **J(θ<sub>0</sub>θ<sub>1</sub>)** = 1/2m*(Σ<sup>m</sup><sub>i≡1</sub>(**h**θ(**x**<sup>(i)</sup>) - **y**<sup>(i)</sup>)<sup>2</sup>)
    - squared error cost function most commonly used for regression problems

- minimize θ<sub>0</sub>θ<sub>1</sub> J(θ<sub>0</sub>θ<sub>1</sub>)

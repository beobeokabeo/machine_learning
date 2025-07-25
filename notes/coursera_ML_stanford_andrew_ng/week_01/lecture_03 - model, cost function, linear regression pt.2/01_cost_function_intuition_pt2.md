# Cost Function pt.2

* Hypothesis **h<sub>θ</sub>(x<sup>(i)</sup>)**
* Cost function for **J(θ<sub>0</sub>θ<sub>1</sub>)**
 
![img_00.jpg](img_00.jpg)

![img_01.jpg](img_01.jpg)

### Cost Function - Intuition II
---

A contour plot is a graph that contains many contour lines. 

A contour line of a two variable function has a constant value at all points of the same line. An example of such a graph is the one to the right below.

![img_02.png](img_02.png)

Taking any color and going along the 'circle', one would expect to get the same value of the cost function. 

For example, the three green points found on the green line above have the same value for **J(θ<sub>0</sub>θ<sub>1</sub>)**
and as a result, they are found along the same line. The circled x displays the value of the cost function for the graph on the left when **θ<sub>0</sub>= 800** and **θ<sub>0</sub>= -0.15**

Taking another h(x) and plotting its contour plot, one gets the following graphs:

![img_03.png](img_03.png)

When **θ<sub>0</sub> = 360** and **θ<sub>1</sub> = 0**  the value of **J(θ<sub>0</sub>θ<sub>1</sub>)** in the contour plot gets closer to the center thus reducing the cost function error. Now giving our hypothesis function a slightly positive slope results in a better fit of the data.

![img_04.png](img_04.png)


The graph above minimizes the cost function as much as possible and consequently, the result **θ<sub>1</sub> = 0.12** and **θ<sub>0</sub> = 250**.

Plotting those values on our graph to the right seems to put our point in the center of the inner most 'circle'.

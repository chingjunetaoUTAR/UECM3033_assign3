UECM3033 Assignment #3 Report
========================================================

- Prepared by: Ching June Tao
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/chingjunetaoUTAR/UECM3033_assign3](https://github.com/chingjunetaoUTAR/UECM3033_assign3)


Explain how you implement your `task1.py` here.

An integral over [a,b] must be changed into an integral over [-1,1] before applying the Gaussian quadrature rule. This interval transformation can be done in the following way.

$$ u = T(x) = \frac{b-a}{2}x + \frac{b+a}{2} $$

$$\int_a^{b}f(x) dx= \frac{b-a}{2}\int_{-1}^{1} f(\frac{b-a}{2}x + \frac{a+b}{x} )  dx$$ 

Applying the Gaussian quadrature rule then results in the following approximation.

$$\int_a^{b}f(x) dx= \frac{b-a}{2}\sum_{i=1}^{n} w_i f(\frac{b-a}{2}x_i + \frac{a+b}{x} ) $$


Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

x_i and w_i can be obtained by the polynomial module in python. The function is stated below.

x,w = np.polynomial.legendre.leggauss(n)

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.


Put your graphs here and explain.

Is the system of ODE sensitive to initial condition? Explain.

-----------------------------------

<sup>last modified: 16/4/2016 </sup>

---
title: "Formulas for Linear Models"
parent: "Analyze Data"
grand_parent: "R Language"
nav_order: 4
---

# Formulas for linear models

## Basic form
- In __R__ linear models are specified using a _model formula_, which is an expression that contains a tilde (the `~` character).
- The _response_ is on the left-hand side of `~`, typically as the name of a variable, e.g. `optden`, but it can also be a function call, e.g. `log(BrainWt)`.
- The right-hand side of the formula is composed of _model terms_ separated by `+`.

## Fitting linear models is not trivial
- Although it may seem straightforward, fitting a linear model can be quite involved.
- Complications arrive from
    - missing data
    - categorical covariates
    - terms that are function calls
    - several possible auxiliary arguments such as `subset`, `na.action`, `constrasts`, ...
    - provision for analysis of variance and other testing procedures

## Model frames and model matrices
- Because the same issues are encountered in any statistical model that is based on a model matrix, there is a standard approach.
    - Create a `model.frame` by examining the formula/data specification, applying a `subset` specification, handling `NAs`, evaluating function calls, re-ordering terms if necessary.
    - Create a `model.matrix` and `model_response` from the model frame. Associate columns in the model matrix with terms in the model frame.
- Note the use of the term "model matrix".  Sometimes $\bf X$ in $\bf X\beta$ is called a "design matrix" but that is a misnomer.

## A simple example - Formaldehyde
- The `Formaldehyde` data in the `datasets` package is from a calibration experiment in which the optical density in an assay is measure for various carbohydrate concentrations.


``` r
str(Formaldehyde)
```

```
## 'data.frame':	6 obs. of  2 variables:
##  $ carb  : num  0.1 0.3 0.5 0.6 0.7 0.9
##  $ optden: num  0.086 0.269 0.446 0.538 0.626 0.782
```
## Formaldehyde data plot
![plot of chunk formplot](data:image/png;base64,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L7xg2267rU2fPt3tub/00ktuyNr4V40SIoBAWAL77bef6Q4addmTEECgMATWubbqHPywYcMKozaUEgEEEEAAAQScQNYjeIwQQAABBBBAoDAFCPCF2W6UGgEEEEAAgawCBPisPHyJAAIIIIBAYQoEnoO/7bbb3GAWdVVp5MiR7mraur7ncwQQQAABBBCIViAwwOtq2a5du9ZZsg4dOtT5HV8ggAACCCCAQPQCgQFeA1von9LkyZPtq6++srVr17qhaxcsWOBum2vdunX0pacECCCAAAIIIBAoEBjg/Sn1BKkBAwa4gL5mzRo3wMWyZcusT58+/iT8RQABBBBAAIEYCmS9yE6D2txwww12yy232N5772162IyeD7969eoYVoUiIYAAAggggIAvkDXAN2/e3Jo2bWo777yzC+760Z577ml6nCwJAQQQQAABBOIrkLWL/vjjj7devXq5AN+iRQu79NJL7emnn7aJEyfGt0aUDAEEEEAAAQQs6xH8TjvtZBMmTLDS0lIbN26cexb8rbfealtuuSV0CCCAAAIIIBBjgawB/ttvvzU9Ue7777+3zTff3F1Ff/3119dZnYqKCpsyZYrNnTu3zml0Rf6qVavq/J4vEEAAAQQQQGDjBbIG+CeeeMKGDx9uBxxwgMvprrvusq222srefffdWjnrUZIjRoywTz75xDQQzrRp02pNox2FCy64wH788cda3/EBAggggAACCIQnkPUcvO59nzNnTrXclixZYrr4rmaaOnWqdezY0QYOHGi77babjR8/3oYMGZKeTPO688473fn89IfeCx3N+zsDurc+Do+j1POu41COTKeoXstBO2/FnFgezN0ii0OVA+tE1dZADpWVlcW8aXDrRZxjRdYAr/vdjzrqKHfE3qNHD3vzzTfdxn7HHXes1aizZs1yAV5ftG/fvtaOgc7hH3vssS7wZ/549uzZduGFF7qPTjjhBDvvvPMyv47ktTZkTZo0iSTvuGXaqlWruBUp7+XR8qDrUIo5lZSUmP41bty4mBncBl13FpHMWrZsWfQMcdk21HXretYA37lzZ3vxxRfdlfPqXv/tb39r++yzT2CjqqL+3pyO1jMD5Jdffmmffvqpu8Vu0aJFbmQ87QQo6XnzysNP2lGIOpWVldnSpUujLkbk+atHZv78+UV/BF9eXm7quSrmpHVC6/jixYuLmcH1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)

## Fitting a simple linear regression model

``` r
summary(m1 <- lm(optden ~ 1 + carb, Formaldehyde))
```

```
## 
## Call:
## lm(formula = optden ~ 1 + carb, data = Formaldehyde)
## 
## Residuals:
##         1         2         3         4         5         6 
## -0.006714  0.001029  0.002771  0.007143  0.007514 -0.011743 
## 
## Coefficients:
##             Estimate Std. Error t value Pr(>|t|)
## (Intercept) 0.005086   0.007834   0.649    0.552
## carb        0.876286   0.013535  64.744 3.41e-07
## 
## Residual standard error: 0.008649 on 4 degrees of freedom
## Multiple R-squared:  0.999,	Adjusted R-squared:  0.9988 
## F-statistic:  4192 on 1 and 4 DF,  p-value: 3.409e-07
```

## Extractor methods

``` r
class(m1)
```

```
## [1] "lm"
```
- There are many extractor methods defined for this class.  Use `methods(class="lm")` to see them.

## A model frame contains information on terms

``` r
str(model.frame(m1))
```

```
## 'data.frame':	6 obs. of  2 variables:
##  $ optden: num  0.086 0.269 0.446 0.538 0.626 0.782
##  $ carb  : num  0.1 0.3 0.5 0.6 0.7 0.9
##  - attr(*, "terms")=Classes 'terms', 'formula'  language optden ~ 1 + carb
##   .. ..- attr(*, "variables")= language list(optden, carb)
##   .. ..- attr(*, "factors")= int [1:2, 1] 0 1
##   .. .. ..- attr(*, "dimnames")=List of 2
##   .. .. .. ..$ : chr [1:2] "optden" "carb"
##   .. .. .. ..$ : chr "carb"
##   .. ..- attr(*, "term.labels")= chr "carb"
##   .. ..- attr(*, "order")= int 1
##   .. ..- attr(*, "intercept")= int 1
##   .. ..- attr(*, "response")= int 1
##   .. ..- attr(*, ".Environment")=<environment: 0xb819d9e00> 
##   .. ..- attr(*, "predvars")= language list(optden, carb)
##   .. ..- attr(*, "dataClasses")= Named chr [1:2] "numeric" "numeric"
##   .. .. ..- attr(*, "names")= chr [1:2] "optden" "carb"
```

## Model matrix relates columns to terms

``` r
model.matrix(m1)
```

```
##   (Intercept) carb
## 1           1  0.1
## 2           1  0.3
## 3           1  0.5
## 4           1  0.6
## 5           1  0.7
## 6           1  0.9
## attr(,"assign")
## [1] 0 1
```

## `lm` objects have many components


``` r
str(m1)
```

```
## List of 12
##  $ coefficients : Named num [1:2] 0.00509 0.87629
##   ..- attr(*, "names")= chr [1:2] "(Intercept)" "carb"
##  $ residuals    : Named num [1:6] -0.00671 0.00103 0.00277 0.00714 0.00751 ...
##   ..- attr(*, "names")= chr [1:6] "1" "2" "3" "4" ...
##  $ effects      : Named num [1:6] -1.12146 0.55996 0.00514 0.00992 0.01069 ...
##   ..- attr(*, "names")= chr [1:6] "(Intercept)" "carb" "" "" ...
##  $ rank         : int 2
##  $ fitted.values: Named num [1:6] 0.0927 0.268 0.4432 0.5309 0.6185 ...
##   ..- attr(*, "names")= chr [1:6] "1" "2" "3" "4" ...
##  $ assign       : int [1:2] 0 1
##  $ qr           :List of 5
##   ..$ qr   : num [1:6, 1:2] -2.449 0.408 0.408 0.408 0.408 ...
##   .. ..- attr(*, "dimnames")=List of 2
##   .. .. ..$ : chr [1:6] "1" "2" "3" "4" ...
##   .. .. ..$ : chr [1:2] "(Intercept)" "carb"
##   .. ..- attr(*, "assign")= int [1:2] 0 1
##   ..$ qraux: num [1:2] 1.41 1.15
##   ..$ pivot: int [1:2] 1 2
##   ..$ tol  : num 1e-07
##   ..$ rank : int 2
##   ..- attr(*, "class")= chr "qr"
##  $ df.residual  : int 4
##  $ xlevels      : Named list()
##  $ call         : language lm(formula = optden ~ 1 + carb, data = Formaldehyde)
##  $ terms        :Classes 'terms', 'formula'  language optden ~ 1 + carb
##   .. ..- attr(*, "variables")= language list(optden, carb)
##   .. ..- attr(*, "factors")= int [1:2, 1] 0 1
##   .. .. ..- attr(*, "dimnames")=List of 2
##   .. .. .. ..$ : chr [1:2] "optden" "carb"
##   .. .. .. ..$ : chr "carb"
##   .. ..- attr(*, "term.labels")= chr "carb"
##   .. ..- attr(*, "order")= int 1
##   .. ..- attr(*, "intercept")= int 1
##   .. ..- attr(*, "response")= int 1
##   .. ..- attr(*, ".Environment")=<environment: 0xb819d9e00> 
##   .. ..- attr(*, "predvars")= language list(optden, carb)
##   .. ..- attr(*, "dataClasses")= Named chr [1:2] "numeric" "numeric"
##   .. .. ..- attr(*, "names")= chr [1:2] "optden" "carb"
##  $ model        :'data.frame':	6 obs. of  2 variables:
##   ..$ optden: num [1:6] 0.086 0.269 0.446 0.538 0.626 0.782
##   ..$ carb  : num [1:6] 0.1 0.3 0.5 0.6 0.7 0.9
##   ..- attr(*, "terms")=Classes 'terms', 'formula'  language optden ~ 1 + carb
##   .. .. ..- attr(*, "variables")= language list(optden, carb)
##   .. .. ..- attr(*, "factors")= int [1:2, 1] 0 1
##   .. .. .. ..- attr(*, "dimnames")=List of 2
##   .. .. .. .. ..$ : chr [1:2] "optden" "carb"
##   .. .. .. .. ..$ : chr "carb"
##   .. .. ..- attr(*, "term.labels")= chr "carb"
##   .. .. ..- attr(*, "order")= int 1
##   .. .. ..- attr(*, "intercept")= int 1
##   .. .. ..- attr(*, "response")= int 1
##   .. .. ..- attr(*, ".Environment")=<environment: 0xb819d9e00> 
##   .. .. ..- attr(*, "predvars")= language list(optden, carb)
##   .. .. ..- attr(*, "dataClasses")= Named chr [1:2] "numeric" "numeric"
##   .. .. .. ..- attr(*, "names")= chr [1:2] "optden" "carb"
##  - attr(*, "class")= chr "lm"
```

## Other extractors
- `model.response` goes through `model.frame`
- `fitted` and `residuals` just extract components
- the `qr` component provides a QR decompositon of $\bf X$
- the `effects` component, $\bf Q'\bf y$, is used for analysis of variance, `anova`
- many extractors such as `hatvalues`, `cooks.distance`, `dfbeta`, `dfbetas`, `rstandard`, `rstudent` and `kappa` are related to regression diagnostics.

## Anova and effects


``` r
effects(m1)^2
```

```
##  (Intercept)         carb                                                     
## 1.257668e+00 3.135496e-01 2.641354e-05 9.832048e-05 1.143173e-04 6.014870e-05 
## attr(,"assign")
## [1] 0 1
## attr(,"class")
## [1] "coef"
```

``` r
anova(m1)
```

```
## Analysis of Variance Table
## 
## Response: optden
##           Df   Sum Sq  Mean Sq F value    Pr(>F)
## carb       1 0.313550 0.313550  4191.8 3.409e-07
## Residuals  4 0.000299 0.000075
```

# Formula examples

## Covariate names in the examples
- In the formulas below we write the response as `y`, continuous covariates as `x,z,u,...` and categorical covariates as `f` and `g`.  
- Note that the categorical covariates are assumed to be stored as `factors`

## Simple linear regression

``` r
y ~ x
```
denotes the simple linear regression model
$$
y_i = \beta_0+\beta_1 x_i + \epsilon_i, \quad i = 1,\dots,n
$$

- In this formula, the intercept term is implicit.  To make it explicit use

``` r
y ~ 1 + x
```

- For clarity I prefer to use the explicit form.  
- We are still debating the formula terms for the __Julia__ language.  Right now the prevailing opinion is __not__ to assume an implicit intercept term.

## Regression through the origin

- To suppress an intercept term use

``` r
y ~ 0 + x
```

- An alternative formula is

``` r
y ~ x - 1
```

- Both of these generate the model
$$
y_i = \beta_1 x_i + \epsilon_i, \quad i = 1,\dots, n
$$

## Zero intercept for Formaldehyde?


``` r
m2 <- lm(optden ~ 0 + carb, Formaldehyde)
anova(m2,m1)
```

```
## Analysis of Variance Table
## 
## Model 1: optden ~ 0 + carb
## Model 2: optden ~ 1 + carb
##   Res.Df        RSS Df  Sum of Sq      F Pr(>F)
## 1      5 0.00033073                            
## 2      4 0.00029920  1 3.1526e-05 0.4215 0.5516
```

``` r
coef(summary(m1))
```

```
##                Estimate  Std. Error    t value     Pr(>|t|)
## (Intercept) 0.005085714 0.007833679  0.6492115 5.515953e-01
## carb        0.876285714 0.013534536 64.7444207 3.409192e-07
```


## Multiple linear regression
- Multiple covariate terms can be given, as in

``` r
y ~ 1 + x + z + sqrt(u)
```
corresponding to
$$
y_i = \beta_0 + \beta_i x_i+\beta_2 z_i+\beta_3 \sqrt{u_i}+\epsilon_i, \quad i=1,\dots,n
$$

## Polynomial regression
- To include polynomial terms you must protect the `^` operator by wrapping it in `I()`.
- That is, the model
$$
y_i=\beta_0+\beta_1 x_i+\beta_2 x_i^2 + \beta_3 x_i^3+\epsilon_i,\quad i=1,\dots,n
$$
is written

``` r
y ~ 1 + x + I(x^2) + I(x^3)
```

## Orthogonal polynomial terms
- Another specification for a polynomial regression model uses the `poly()` function which generates _orthogonal polynomial_ terms

``` r
y ~ poly(x, 3)
```

- The fitted responses will be the same from the model using `I(x^2)`, etc. but the coefficients will be different.
- Orthogonal polynomials allow for backward elimination of higher order polynomial terms without refitting the model.  (Not a consideration these days)
- Fitting high order polynomials is discouraged.  Smoothing approaches are preferred.

## Quadratic for Formaldehyde?

``` r
m3 <- lm(optden ~ 1 + carb + I(carb^2), Formaldehyde)
coef(summary(m3))
```

```
##                Estimate  Std. Error   t value     Pr(>|t|)
## (Intercept) -0.01168268 0.006001455 -1.946642 1.467548e-01
## carb         0.97112338 0.026782523 36.259593 4.613325e-05
## I(carb^2)   -0.09621212 0.026309447 -3.656942 3.532047e-02
```

``` r
m4 <- lm(optden ~ poly(carb,2), Formaldehyde)
coef(summary(m4))
```

```
##                   Estimate  Std. Error    t value     Pr(>|t|)
## (Intercept)     0.45783333 0.001745171 262.342918 1.221350e-07
## poly(carb, 2)1  0.55995503 0.004274779 130.990397 9.809825e-07
## poly(carb, 2)2 -0.01563262 0.004274779  -3.656942 3.532047e-02
```

## A single categorical covariate

- A one-way analysis of variance model for the levels of a factor, `f`, is written


``` r
y ~ 1 + f
```

- Often we use the function `aov()` to fit such a model instead of `lm()`.  The result is the same except for the class which changes the way that the fitted model is summarized.

- The model being fit is sometimes written
$$
y_{ij}=\mu+\alpha_i+\epsilon_{ij},\quad i=1,\dots,I\;j=1,\dots,n_i
$$
although it is not fit in that form.

## InsectSprays


``` r
str(InsectSprays)
```

```
## 'data.frame':	72 obs. of  2 variables:
##  $ count: num  10 7 20 14 14 12 10 23 17 20 ...
##  $ spray: Factor w/ 6 levels "A","B","C","D",..: 1 1 1 1 1 1 1 1 1 1 ...
```
![plot of chunk insectspraysplot1](data:image/png;base64,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sdauXTt77733XJz/HXfc0Tp37pyH0ilLEQgPgUAVPK3q999/v0ztd955Z/MWgilzQF9EoEAJfPzxx7Zs2TLbfffdjUUcJLklQG/dW9Hw999/tzfffNOOO+44e+CBB2zatGmuMDvttFNuC6XciobAkiVLbPLkya6h2KlTp6KpV6yKBKrgWW1nyJAh1qdPn0heLVq0kIKP0NBGoRO47rrr7KGHHnJLvaJcpk6dag0aNEi62KtXr7ZHHnnEli5danh6b7nllklf65346quv2kcffWS77rqrHXjggd7unH3++OOPNnjwYLcC2c0332wtW7bMWd5ktPnmm9vs2bNdnizTucUWW7ht/iWr2FnJb/To0W5FvxNPPNFq164dSUMbuSPAs/T0008bv6VTTz3VNtpoo9xl/k9OkyZNsokTJ1rDhg3tiCOOsCOPPNK+//5714jECjR8+PCslmnVqlV2wQUX2A8//OA+O3bsmNX8/IkHquBJmKUJe/fu7c9D2yIQCgKzZs2ye++9N9J7pNB8v/baa5MqPxasbt26OQcwXmiPPvqo/fe//7Vtttkmqeu9/G677TbjpYBSYpnPfv36JX19pif+9ttv1qZNm8j64V27drUnn3zS9thjj0yTTvr6448/3j788EN3Pj15evB0Hlj6NBnBEW/PPfd0yp3rnn/+eadk6tWrl8zlOicgAjzDWMG4B+utt5699NJLbubDpptuGlAOiZOhsXzGGWcYzzWWZJ6Fb775JvJ8f/LJJzZjxgyjI5qp8Ky+/vrr7reLZaBmzZouyVatWtnKlSvddt++fe3OO+90jf9M80vm+uR+Mcmk9M85ixYtco4xfKXFdPTRR7sjvPBOO+00t73LLru41pz7EtC/ypUru5T8jjgBJV1SycCxVBmOGDGijHLnxtPST7b3N336dGOuNs86Mm/ePHvnnXesbdu27nsy/2gQ8GJEMCU+++yzds455yRzaSDneNYLLzFezij4gw46yNuV9c/77ruvTB40cngJJ9vzobeGQqHsCPfh008/te23375MuqXwBQsIv+lkn+EgmTDLYYMNNnCzHtauXev8Kr7++ms74IADgswmbloM66DcEX6bM2fONJh4guJFESfiw/OEAveGjrzr/Z/4ibzxxhvu98tMjy+++ML12rHqeUIngCmeJ598srcrkE/vWY9OLHAFD6hjjjnG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pBBWBa8x+GDuv1IRAREQAREQgYIiIAVfULdDhREBERABERCBYAhIwQfDUamIgAiIgAiIQEERkIIvqNuhwoiACIiACIhAMASk4IPhqFREQAREQAREoKAISMEHdDvmz59vPXv2tLZt27rpbcxzl4iACIiACIhAvggo0E1A5An2QuhZZNGiRXbPPffYoEGDAkpdyYiACIiACIhAagTUg0+NV4Vnb7XVVpFj9N5ZLU4iAiIgAiIgAvkiIAUfEHniyHsx5gnb2rFjx4BSVjIiIAIiIAIikDoBmehTZxbziuHDh9sJJ5xgxJE/5JBD7Nhjj415nnaKgAiIgAiIQC4ISMEHRLlatWpuydSAklMyIiACIiACIpARAZnoM8JXPBezwMwFF1xg++yzj915553FUzHVRAREQARKlIB68CV646Or3aFDB1u8eLEbYvjiiy+sbt261qdPn+jT9F0EREAERCAkBALrwTNFbNKkSe6PtcmXLFkSEgQqJgQ22mgjp9zZ/u233+ytt95iUyICIiACIhBSAoEp+FWrVjnT7rx582zatGl20UUX2YQJE0KKJbVi41g3bNgwO+yww+zQQw81WKQqOOntuOOOhjf+Cy+8kOrl9u233xpz8Zs2bZqWg1+NGjXK5MnyiKnKuHHjXK9///33N9aHl+SHwJgxY6xXr17WtWtXW7hwYX4KoVxFQATyTiCw9eB//fVX+9e//uUCvFArxnRPOukke+KJJ2JWcsGCBTH3p7uTdcwR8s213HzzzXbvvffamjVrrFKlSu7FOmrUqKSLQW/Z73VPGs8884y1a9cuqTRoUGyzzTZlzj3++OPtxhtvLLMv3pcGDRqUO0x0vmQFs36XLl0ip+N0+O6771r9+vUj+0plI5/rwY8fP97OOuss+/nnnx3uJk2a2GuvvWbe7yNM90DrwWd+t7QefOYMSSGs68FnbQyeFwp/y5Yts5o1a9rq1attt912c7Q7depkd999dzDko1LZeOONo/Zk/+uXX37plDs50Zv/7rvvrF69ekln/N5775U5lzT69etn119/vQ0cOLDMsVhfUKT8kL1IepzDcEkqZYiVbirXjx07tkwS3O+RI0fa0KFDy+wvpS+p8AuKy2effRZR7qRJY3HlypXWvHnzoLLIaTooeUnmBPLxLGZeaqWQLAHet7EkroKfOXOm1a5d2/3FujjRPhQO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nx5LCPEHJCIgAiIgAiKQLoFATfTpFqKQrmO+I2vKEyyG7V69erngMdku4zvvvOOmIXpemoQKJpzudtttl+2slb4IiIAIiEAREpCCj3FT6cGPHDkyxpHs7YqexkIEOvZJwWePuVIWAREQgWImIAWf4d1l3fkPP/zQCA5EONh0pXXr1sb8da8HT+AX9klEQAREQAREIB0CUvDpUPvnms8++8y6d+/uZg0wHeX00083YsqnIwQRIu468+FZ6pYhgho1aqSTlK4RAREQAREQAZOCz+AhYGEUL6Y+PW9i9qer4CkG5nji0ktEQAREQAREIFMC8qLPgGCjRo3KXB108J4yieuLCIiACIiACKRAQAo+BVjRp55zzjluaVOm0hHiliA/EhEQAREQAREoBAIy0WdwF1DqX331lU2fPt3q1KnjVkPLIDldKgIiIAIiIAKBEZCCzxAlcfdTXdwmwyx1uQiIgAiIgAgkJCATfUJEOkEEREAEREAEwkdACj5890wlFgEREAEREIGEBKTgEyLSCSIgAiIgAiIQPgJS8OG7ZyqxCIiACIiACCQkIAWfEJFOyBeBhQsXGovwzJo1K19FUL4iIAIiEFoCUvChvXXFXfBvv/3WunbtameddZZ17NjRJk6cWNwV9tXugw8+sKOPPto6depkU6dO9R3RZi4IzJs3z95//31jPQiJCISZgKbJhfnuFXHZBw4caIsXL47U8IYbbnChgCM7inRj9uzZ1qNHj0jtjj/+eHvhhReMtQok2SfAwlEnn3yyy2jRokU2YcIEsc8+duWQJQLqwWcJrJLNjMDmm29eJgHM9aUgrE5IbAVPWDb466+/9r4W/CfDKffdd5899NBDRtnDJih3FDt/yPXXXx+2Kqi8IhAhoB58BIU2ConAqaeeauPGjXOhgFF49OhLQRo3buyWDfbq+uuvv1qzZs28rwX9OX/+fOvbt69h4q5WrZobVhkxYoStt154+hFEp/SUO7DnzJlT0MxVOBGIRyA8v7x4tdCxoiOw1157OQVx++2324MPPmgnnnhi0dUxVoV23HFHo84sGbzbbrvZo48+ai1atIh1asHte/jhh51yp2CrV682rBFhc5A87rjjrFKlSo4tDcuLLrqo4DjnqkAsh33++efbaaedJn+EXEEPOJ9Ae/AzZ850rV9+IPXq1VNs9oBvVikkt3z5cluzZo1tttlmrucalt5rkPdmzz33NHq+LB+84YYbBpl00mn98ssvxhLI3IdkhWGVKlWq2B9//OEu+fHHH2399QN9xSRbFHfesmXLbO3atSnV4ZhjjnHvLYZFeIdtsMEG7nnkMx+ydOlS1+CoWbNmTrPHCtOtW7dInlOmTLHx48dbjRo1Ivu0UfgEAu3BP/PMM87rF7PWI488YiNHjix8AiphwRCYPHmyHXrooc57vk+fPk7BFEzhclQQGsm77rqrHX744U7R8D3XMnbsWHcfOnfubOeee679/fffSRUB5diwYUPzFD1m+oMPPthQtLmWJ554wtVhn332scsuuyyl7Nu3b2+1a9e2E044wahTkyZN8mKJ4P3J74EG3y233JJSHTI9GWXuWTJICx8YrEmScBGotO7Hm9yvN4l68RAeeOCBttNOO9mqVavswgsvtGHDhrkrcbj59NNP3famm24aeEtwo402cmmTryR9AnDMB8OffvrJtt9++0jB6bleffXV7iUb2RmSjapVqxp/jJ+nKvQa6XV6gqne+914+7L5SYOC4RHPQa569ep299132yGHHJJUtlzHkIJfqTMuf9dddyV1vf8kGgiY+lMVhgb222+/CEfeNzj+denSJemkWB3SL7Vq1cqps+NHH33kmGNFQch/1KhR7t74y5Vou3Llyu5diyUgFXnttdeM4Qq/euCZpmePMLvg/vvvN363sG3atGkqyYfuXCw4/C79v81CqgT3ZpNNNilXpMDtZ4yXYsZhHjNjN55gdh08eLD7uscee9ill17qHQrk03PkyZcpLZBKFEAicMwHQ8y5vCR4bpDffvvNvUxybZoM4hbQ8+EvnbLD3q/UeIGi4EmrVatWQRQvbhqY12lUeC/yFStWGMMmqdRlyy23LKPgv/zyy5Su9woIQ15cqQrvGqwInrPcypUrXaM1lTpE50ljLZPro9NL9P33339379ElS5a4U/nOc5FOGfhNp3pd7969DUdX2HlCY4N0ZsyYYT179vR2OysDDRIap8UqPIv+xk6h1ZPnI5YEruCPPPJIa9mypf3www92xx13GMqcViQ9sldeeSVShgULFkS2g9jwWi+8jCTpE4BjPhjSU6SnxcuIXuAWW2zhrEEouLAJzzq9z1R7TdQT8/ykSZMiVealQg+YHjEWjf79+0eOZWOjfv367h54LzS+8xtO5T5gFmcMm8YCLOg5p3K9Vy+eCRoYqQoNDL+gmOCaShlQZH4rBO+0VK7355/OdpN1wwKeFYXrsarhgJlqGfCBoPef6nXkyXP3wAMPsOmEe0k6r7/+euR3ygGeUZ7Zvffe+/9PLML/1J3nyLOoFFoV+a3EksAVPL13HHMYw+LG0wKUY0Ys9NrnJ4Bz1tNPP20XX3yxaxDSQ2jdurX/lJLYZuy4V69eNntdwBt683Pnzo28nIcPH+7MttExAoIEg+f46NGjXSQ9lArzwhlXT0U8Sx1WAF76ROXLpaDQmGJ5+eWXO7MlwYKY/paK0CNlFgOWpDZt2tiTTz6ZyuUZn8sQwdtvv21XXnmle5cyiyQVh8eMC7AugWuuucY1Ml5++WUX7MdT9o0aNTIUijcEhdJP9RkJonxKIzGBwMfgMd/wkqCl065dO+PHFUvUg49FJf/78tWDz3/NgytBJj14fymuuOKKMj0oXvAorlSVlT/NRNuY+hhDx8yNUBccZhmXz7Wk24PPZjl5r02fPt3NFthhhx2ymVW5tL/55htnpqcn7w1JljspakcmPfiopMp8RdkPHTrUDefQoOvQoUOZ48X2JQw9eM+K7WcfaA++lOeM+qFqWwSCIICTEy9SXtI4PxKbP5vKnTLjA0HvkSE2hB7su+++mxcF7wpQQP8wmdNh+eqrr9wwFh729LBzIXfeeadraNHAwDrKcGc6/glBlfWkk04y/iSFTSBQBV/YVVXpRCBcBJo3b27Tpk2zt956yzk37b///lmvAMqd8XdP6BXgdCcxYxowCwF5s0xYI4ChJHrU2RR67sxk8PIlRsGYMWNyPvSRzToq7ewQkILPDlelKgKBEMAsz5h8roTxfaY/4UWNYifYCZaEMAnxFFgJDufAIMet8WL3eyszjOENZWSTD3nSa/cUPN9R8hIRSERACj4RIR0XgRIjsMsuu+R0zneQeJm5Q4AYhhZQiCwzHFQ0RCwoNH4I5IVTKI2HXDiC4sGPNYdGC40M1iugASYRgUQEpOATEdJxERCB0BAgxK9/ehvfb7rpprTLzxx+POjpqRO7gwAwmMeZBnnYYYcl7eyWdgHWXYgPBo6Ojz32mFPwWFXo0UtEIBEBKfhEhHRcBEQgNAToVfsV/OLFi9MuO9O/+vXr5xwO8Vpn2hqzGNiXayH/sA2V5JqR8itPINBY9OWT1x4REAERyB0B4sfT4yVoEn/M5U5XmP/NErgIHvSMfeNBLxGBsBBQDz4sd0rlFAERSEhgwIABLqQv49U777xzRtMKsQYwPdEL14o1INZc44SF0gkikCcCUvB5Aq9sRUAEskOAsLRByEEHHeSmxhHVDkU/cOBA5+wWRNpKQwRyQUAKPheUlYcIiEDoCDDuzeJZBP0hbHD0CnOhq5AKXHIEpOBL7parwiIgAqkQiF68JpVrda4I5JOAnOzySV95i4AIiIAIiECWCEjBZwmskhUBERABERCBfBKQgs8nfeUtAiIgAiIgAlkiIAWfJbBKVgREQAREQATySUAKPp/0lbcIiIAIiIAIZImAFHyWwCpZERABERABEcgnASn4fNJX3kVFYPr06da1a1e3PniPHj3szz//LKr6qTIiIALhIqB58OG6X0VVWta0njVrltWrV8+tPR7myrHACcrdkyVLlth//vMfO/HEE71d+hQBERCBnBKQgs8pbmXmEVi0aJEdeuih9vfff7tIYS+88ILttttu3uHQfaLgt956a/vuu+9c2VmPfMaMGaGrhwosAiJQPARkoi+eexmqmpx++uk2b948p9wp+OWXXx6q8kcXlmhnrNFNeFOkcuXKdvDBB0efpu8ikHMCw4cPtw4dOtgOO+xgN998c87zV4b5I6AefP7Yl3TOLOXpl4ULF/q/hm67SpUq9sQTT9jZZ59tVatWtWOPPdbat28funqowMVF4OOPP7ZBgwZF/EEefvhhp+z32muv4qqoahOTQFZ68FOnTnVrJ8fMUTtFYB0BFOAWW2zhWFSvXt169uzptr///nu35jbrb4dNWHHsgQceMJYs/eOPP9wa4vmoA859rFs+Z86ctLNnqCGTtc8//PBDu+uuu2zu3LlplyHfF/700082bdo0W716db6Lknb+3AcanJ5QF/xDwiTz58+3zz//PNJICVPZ813WSuvGQP8OshD8oC+44AI7/vjj45ooFyxYEGS2kXWaly9fHmi6pZYY613niiEvzwkTJljTpk3twAMPtCeffNKGDBnifsgbbrihvfnmm1atWrVQ3YJTTjnFXnnlFedbwApkn3zyidWoUSNndUC59+/f37755hv78ccf7ZprrrHjjjsupfzvvvtue+SRR1wjHb+Cp59+2tZfP3lj3/33329XX311JE9WZOvWrVvke7IbNPxWrFiR7OmBnkfP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)

## More `InsectSprays` plots

![plot of chunk insectspraysplot2](data:image/png;base64,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)
![plot of chunk insectspraysplot3](data:image/png;base64,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)
![plot of chunk insectspraysplot4](data:image/png;base64,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)

## `InsectSprays` fit

``` r
summary(m5 <- aov(sqrt(count) ~ 1 + spray, InsectSprays))
```

```
##             Df Sum Sq Mean Sq F value Pr(>F)
## spray        5  88.44  17.688    44.8 <2e-16
## Residuals   66  26.06   0.395
```

``` r
effects(m5)[1:6]^2
```

```
## (Intercept)      sprayB      sprayC      sprayD      sprayE      sprayF 
## 569.5041501  16.3082599  27.5296750   9.5833274  34.6174157   0.3991945
```

``` r
c(sum(effects(m5)[2:6]^2), sum(effects(m5)[-(1:6)]^2))
```

```
## [1] 88.43787 26.05798
```

## Contrasts and model matrices


``` r
unique(model.matrix(m5))
```

```
##    (Intercept) sprayB sprayC sprayD sprayE sprayF
## 1            1      0      0      0      0      0
## 13           1      1      0      0      0      0
## 25           1      0      1      0      0      0
## 37           1      0      0      1      0      0
## 49           1      0      0      0      1      0
## 61           1      0      0      0      0      1
```

``` r
contrasts(InsectSprays$spray)
```

```
##   B C D E F
## A 0 0 0 0 0
## B 1 0 0 0 0
## C 0 1 0 0 0
## D 0 0 1 0 0
## E 0 0 0 1 0
## F 0 0 0 0 1
```

## Terms in `m5`

``` r
terms(m5)
```

```
## sqrt(count) ~ 1 + spray
## attr(,"variables")
## list(sqrt(count), spray)
## attr(,"factors")
##             spray
## sqrt(count)     0
## spray           1
## attr(,"term.labels")
## [1] "spray"
## attr(,"order")
## [1] 1
## attr(,"intercept")
## [1] 1
## attr(,"response")
## [1] 1
## attr(,".Environment")
## <environment: 0xb819d9e00>
## attr(,"predvars")
## list(sqrt(count), spray)
## attr(,"dataClasses")
## sqrt(count)       spray 
##   "numeric"    "factor"
```

## Two categorical factors
- The _additive_ model is specified as

``` r
y ~ 1 + f + g
```
- The analysis of variance for a model with multiple categorical covariates is the _sequential_ anova.
- For unbalanced data the F statistics for `f` and `g` change if you specify the model as `y ~ 1 + g + f`
- The two-factor model with interactions is

``` r
y ~ 1 + f + g + f:g
```
or, equivalently,

``` r
y ~ 1 + f * g
```

## Examples of additive models

``` r
summary(m6 <- aov(price ~ 1 + carat + cut + color, diamonds))
```

```
##                Df    Sum Sq   Mean Sq  F value Pr(>F)
## carat           1 7.291e+11 7.291e+11 355472.6 <2e-16
## cut             4 6.133e+09 1.533e+09    747.5 <2e-16
## color           6 1.260e+10 2.100e+09   1023.7 <2e-16
## Residuals   53928 1.106e+11 2.051e+06
```

``` r
summary(m7 <- aov(price ~ 1 + carat + color + cut, diamonds))
```

```
##                Df    Sum Sq   Mean Sq  F value Pr(>F)
## carat           1 7.291e+11 7.291e+11 355472.6 <2e-16
## color           6 1.256e+10 2.093e+09   1020.6 <2e-16
## cut             4 6.171e+09 1.543e+09    752.1 <2e-16
## Residuals   53928 1.106e+11 2.051e+06
```

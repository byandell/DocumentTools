---
title: "Examples Using for and apply"
parent: "Curate R Data"
grand_parent: "R Language"
nav_order: 2
---

# Examples Using for and apply

The purpose of the base `apply` family of functions is to SIMPLIFY loops.

## loop approach


``` r
numSimulations <- 10000
ptm <- proc.time()
results <- NULL
for(iS in 1:numSimulations){
  temp <- rnorm(100, 0, 1)
  results <- rbind(results, 
                   c(simNumber = iS, 
                     mean = mean(temp), 
                     min = min(temp),
                     max = max(temp)))
}
(loopTime <- proc.time() - ptm)
```

```
##    user  system elapsed 
##   0.226   0.008   0.235
```

## apply approach - "apply" function


``` r
ptm <- proc.time()
simulation <- function(ID){
  temp <- rnorm(100, 0, 1)
  c(simNumber = ID, 
    mean = mean(temp), 
    min = min(temp), 
    max = max(temp))
}

results <- sapply(1:numSimulations, simulation)
results <- t(results)
(applyTime <- proc.time() - ptm)
```

```
##    user  system elapsed 
##   0.080   0.001   0.081
```

But this is misleading; the bottleneck in the loop
is that the array is being continuously copied and
memory reallocated.  If instead we allocate the memory
initially, then the times become quite close.


``` r
ptm <- proc.time()
results <- matrix(0, nrow = numSimulations, ncol = 4)
for(iS in 1:numSimulations){
  temp <- rnorm(100, 0, 1)
  results[iS,] <- c(simNumber = iS, 
                    mean = mean(temp), 
                    min = min(temp),  
                    max = max(temp))
}
(loopTime2 <- proc.time() - ptm)
```

```
##    user  system elapsed 
##   0.061   0.003   0.064
```

### lapply and sapply

`lapply` takes a vector or list (incl. data.frame) and returns list.
`sapply` does the same but returns a simplified structure.


``` r
myList <- list(a = c(1,2,3,4,5), 
               b = c(6,7,8,9,10), 
               c = c(11,12,13,14,15))
fun_item1 <- function(data1, data2){ data1 }
fun_type1 <- function(data1) { list(typeof(data1), data1) }

lapply(myList, mean)
```

```
## $a
## [1] 3
## 
## $b
## [1] 8
## 
## $c
## [1] 13
```

``` r
sapply(myList, mean)
```

```
##  a  b  c 
##  3  8 13
```

``` r
myVector <- 0:10
lapply(myVector, `^`, 2)
```

```
## [[1]]
## [1] 0
## 
## [[2]]
## [1] 1
## 
## [[3]]
## [1] 4
## 
## [[4]]
## [1] 9
## 
## [[5]]
## [1] 16
## 
## [[6]]
## [1] 25
## 
## [[7]]
## [1] 36
## 
## [[8]]
## [1] 49
## 
## [[9]]
## [1] 64
## 
## [[10]]
## [1] 81
## 
## [[11]]
## [1] 100
```

``` r
sapply(myVector, `^`, 2)
```

```
##  [1]   0   1   4   9  16  25  36  49  64  81 100
```

``` r
myDF <- data.frame(names = c("ann","bob","corinne"),
                   salary = c(15000, 25000, 150000),
                   age = c(50, 40, 60))
lapply(myDF, mean)
```

```
## $names
## [1] NA
## 
## $salary
## [1] 63333.33
## 
## $age
## [1] 50
```

``` r
sapply(myDF, mean)
```

```
##    names   salary      age 
##       NA 63333.33    50.00
```

### vapply

`vapply` works on vectors, returns an array, requires FUN.VALUE


``` r
myStats <- function(data){ 
  c(mean=mean(data), min=min(data), max=max(data))
  }
vapply(myList, myStats, 
       FUN.VALUE = c(Avg = 0, minValue = 0, maxValue = 0))
```

```
##          a  b  c
## Avg      3  8 13
## minValue 1  6 11
## maxValue 5 10 15
```

### apply

`apply` works on the margin of an array


``` r
myArray <- matrix(1:12, ncol=3)
apply(myArray, 1, sum)
```

```
## [1] 15 18 21 24
```

``` r
apply(myArray, 2, sum)
```

```
## [1] 10 26 42
```

### tapply

`tapply` uses factors instead of margins


``` r
myVector <- 1:12
myFactors <- rep(c("a","b"), c(5,7))
tapply(myVector, myFactors, min)
```

```
## a b 
## 1 6
```

### mapply

`mapply` works where functions require more than one argument


``` r
mapply(`^`, 1:4, 2:5)
```

```
## [1]    1    8   81 1024
```

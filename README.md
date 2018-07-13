# info_gain
Implementation of information gain algorithm. There seems to be a debate about how the information gain metric is defined. Whether to use the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) or the [Mutual information](https://en.wikipedia.org/wiki/Mutual_information) as an algorithm to define information gain. This implementation uses the [information gain calculation](https://en.wikipedia.org/wiki/Information_gain_ratio) as defined below:

## Information gain definitions
### Information gain calculation
Definition from [information gain calculation](https://en.wikipedia.org/wiki/Information_gain_ratio) (retrieved 2018-07-13).
Let `Attr` be the set of all attributes and `Ex` the set of all training examples, `value(x, a)` with `x` in `Ex` defines the value of a specific example `x` for attribute `a` in `Attr`, `H` specifies the entropy. The `values(a)` function denotes the set of all possible values of attribute `a` in `Attr`. The information gain for an attribute `a` in `Attr` is defined as follows:

![Information gain formula][ig]

[ig]: https://github.com/Thijsvanede/info_gain/blob/master/images/information_gain_formula.gif

### Intrinsic value calculation
Definition from [information gain calculation](https://en.wikipedia.org/wiki/Information_gain_ratio) (retrieved 2018-07-13).

![Intrinsic value calculation][iv]

[iv]: https://github.com/Thijsvanede/info_gain/blob/master/images/intrinsic_value_formula.gif

### Information gain ratio calculation
Definition from [information gain calculation](https://en.wikipedia.org/wiki/Information_gain_ratio) (retrieved 2018-07-13).

![Intrinsic value calculation][igr]

[igr]: https://github.com/Thijsvanede/info_gain/blob/master/images/information_gain_ratio_formula.gif

## Installation
To install the package via pip use:
```
pip install info_gain
```

To clone the package from the git repository use:
```
git clone https://github.com/Thijsvanede/info_gain.git
```

## Usage
Import the `info_gain` module with:
```
from info_gain import info_gain
```
The imported module has supports three methods:
 * `info_gain.info_gain(Ex, a)` to compute the information gain.
 * `info_gain.intrinsic_value(Ex, a)` to compute the intrinsic value.
 * `info_gain.info_gain_ratio(Ex, a)` to compute the information gain ratio.

### Example
```python
from info_gain import info_gain

# Example of color to indicate whether something is fruit or vegatable
produce = ['apple', 'apple', 'apple', 'strawberry', 'eggplant']
fruit   = [ True  ,  True  ,  True  ,  True       ,  False    ]
colour  = ['green', 'green', 'red'  , 'red'       , 'purple'  ]

ig  = info_gain.info_gain(fruit, colour)
iv  = info_gain.intrinsic_value(fruit, colour)
igr = info_gain.info_gain_ratio(fruit, colour)

print(ig, iv, igr)
```

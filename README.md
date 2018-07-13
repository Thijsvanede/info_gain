# info_gain
Implementation of information gain algorithm. There seems to be a debate about how the information gain metric is defined. Whether to use the [Kullback-Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) or the [Mutual information](https://en.wikipedia.org/wiki/Mutual_information) as an algorithm to define information gain. This implementation uses the [information gain calculation](https://en.wikipedia.org/wiki/Information_gain_ratio) as defined by:

Let `Attr` be the set of all attributes and `Ex` the set of all training examples, `value(x, a)` with `x` in `Ex` defines the value of a specific example `x` for attribute `a` in `Attr`, `H` specifies the entropy. The `values(a)` function denotes the set of all possible values of attribute `a` in `Attr`. The information gain for an attribute `a` in `Attr` is defined as follows:

![Information gain formula][logo]

[logo]: https://github.com/Thijsvanede/info_gain/blob/master/information_gain_formula.gif

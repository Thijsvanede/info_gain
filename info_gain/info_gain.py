from collections import Counter
from scipy.stats import entropy
import math

def _Ex_a_v_(Ex, a, v, nan=True):
    """ Compute the Ex_a_v value given whether nan==nan or nan!=nan.
    
        Parameters
        ----------
        Ex : list of hashable
            A list of hashable objects (examples)
            corresponding to the given attributes a.
            I.e. a[i] <--> Ex[i].

        a : list of hashable
            A list of hashable objects (attributes)
            corresponding to the given examples Ex.
            I.e. a[i] <--> Ex[i].
            
        v : hashable object
            The hashable object for which to compute
            the Ex_a_v value.
            
        nan : boolean, default=True
            Boolean indicating how nan==nan should be evaluated.
            Default == True to avoid division by 0 errors.
            
        Returns
        -------
        result : list of hashable.
            List of Ex where value(a) == v.
            
        """
    if nan:
        return [x for x, t in zip(Ex, a) if (isinstance(t, float) and
                                             isinstance(v, float) and
                                             math.isnan(t)        and
                                             math.isnan(v))       or
                                             (t == v)]
    else:
        return [x for x, t in zip(Ex, a) if t == v]


def info_gain(Ex, a, nan=True):
    """ Compute the information gain of an attribute a for given examples.

        Parameters
        ----------
        Ex : list of hashable
            A list of hashable objects (examples)
            corresponding to the given attributes a.
            I.e. a[i] <--> Ex[i].

        a : list of hashable
            A list of hashable objects (attributes)
            corresponding to the given examples Ex.
            I.e. a[i] <--> Ex[i].
            
        nan : boolean, default=True
            Boolean indicating how nan==nan should be evaluated.
            Default == True to avoid division by 0 errors.

        Returns
        -------
        result : float
            Information gain by knowing given attributes.

        """
    # Check whether examples and attributes have the same lengths.
    if len(Ex) != len(a):
        raise ValueError("Ex and a must be of the same size.")

    # Compute the entropy of examples
    H_Ex = entropy(list(Counter(Ex).values()))

    # Compute the sum of all values v in a
    sum_v = 0
    for v in set(a):
        Ex_a_v = _Ex_a_v_(Ex, a, v, nan)
        sum_v += (len(Ex_a_v) / len(Ex)) *\
                 (entropy(list(Counter(Ex_a_v).values())))

    # Return result
    return H_Ex - sum_v


def intrinsic_value(Ex, a, nan=True):
    """ Compute the intrinsic value of an attribute a for given examples.

        Parameters
        ----------
        Ex : list of hashable
            A list of hashable objects (examples)
            corresponding to the given attributes a.
            I.e. a[i] <--> Ex[i].

        a : list of hashable
            A list of hashable objects (attributes)
            corresponding to the given examples Ex.
            I.e. a[i] <--> Ex[i].
            
        nan : boolean, default=True
            Boolean indicating how nan==nan should be evaluated.
            Default == True to avoid division by 0 errors.

        Returns
        -------
        result : float
            Intrinsic value of attribute a for samples Ex.

        """
    # Check whether examples and attributes have the same lengths.
    if len(Ex) != len(a):
        raise ValueError("Ex and a must be of the same size.")

    # Compute the sum of all values v in a
    sum_v = 0
    for v in set(a):
        Ex_a_v = _Ex_a_v_(Ex, a, v, nan)
        sum_v += (len(Ex_a_v) / len(Ex)) * math.log(len(Ex_a_v) / len(Ex), 2)

    # Return result
    return -sum_v


def info_gain_ratio(Ex, a, nan=True):
    """ Compute the information gain ratio of an attribute a for given examples.

        Parameters
        ----------
        Ex : list of hashable
            A list of hashable objects (examples)
            corresponding to the given attributes a.
            I.e. a[i] <--> Ex[i].

        a : list of hashable
            A list of hashable objects (attributes)
            corresponding to the given examples Ex.
            I.e. a[i] <--> Ex[i].
            
        nan : boolean, default=True
            Boolean indicating how nan==nan should be evaluated.
            Default == True to avoid division by 0 errors.

        Returns
        -------
        result : float
            Information gain ratio by knowing given attributes.
            I.e. information gain normalised with intrinsic value calculation.

        """
    # Check whether examples and attributes have the same lengths.
    if len(Ex) != len(a):
        raise ValueError("Ex and a must be of the same size.")

    # Compute information gain ratio as IG/IV
    return info_gain(Ex, a, nan) / intrinsic_value(Ex, a, nan)

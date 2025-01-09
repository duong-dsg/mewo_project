"""
Mewo - Python library for cat lovers.
"""
__version__ = "0.1.0"

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def first_function(kind=None):
    """
    Return a list of random cat name as strings.
    
    :param kind: Optional "kind" of cat.
    :type kind: list[str] or None
    :raise mewo.InvalidKindError: If the kind is invalid.
    :return: The cat name list.
    :rtype: list[str]
    """
    return ["Anna", "Lucy", "HeeHee"]

def get_random_ingredients(kind=None):
    """
    Return a list of random cat name as strings.

    :param kind: Optional "kind" of cat.
    :type kind: list[str] or None
    :raise mewo.InvalidKindError: If the kind is invalid.
    :return: The cat name list.
    :rtype: list[str]
    """
    return ["Anna", "Lucy", "HeeHee"]

def another_function(kind=None, arg2=None):
    """
    Return a list of random ingredients as strings.
    
    :param kind: Optional "kind" of ingredients.
    :param arg2: Optional.
    :type kind: list[str] or None
    :return: The cat name list.
    :rtype: list[str]
    """
    return ["Anna", "Lucy", "HeeHee"]
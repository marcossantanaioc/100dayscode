# from replit import clear # If not using replit
import os
from art import logo

print(logo)


def clear():
    os.system('clear')


def add(n1, n2):
    """
    Adds two numbers `n1`
    and `n2`
    Parameters
    ----------
    n1 : float or int
      A float or int.
    n2: float or int
      Another float or int.
    Returns
    -------
    result : float
      `n1` + `n2`
    """
    res = n1 + n2
    return res


def subtract(n1, n2):
    """
    Subtract `n1` from `n2`
    Parameters
    ----------
    n1 : float or int
      A float or int.
    n2: float or int
      Another float or int.
    Returns
    -------
    result : float
      `n1` - `n2`
    """
    res = n1 - n2
    return res


def multiply(n1, n2):
    """
    Multiply `n1` by `n2`
    Parameters
    ----------
    n1 : float or int
      A float or int.
    n2: float or int
      Another float or int.
    Returns
    -------
    result : float
      `n1` * `n2`
    """
    res = n1 * n2
    return res


def divide(n1, n2):
    """
    Divides `n1`by `n2`
    Parameters
    ----------
    n1 : float or int
      A float or int.
    n2: float or int
      Another float or int.
    Returns
    -------
    result : float
      `n1` / `n2`
    """
    res = n1 / n2
    return res


calculator = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide}


def get_inputs():
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))

    for key in calculator:
        print(key)
    operation = str(input("Pick an operation from the line above?: "))

    return num1, num2, operation


def calculation(num1, num2, operation):
    """
    Run a given `operation`
    on `num1` and `num2`
    Parameters
    ----------
    num1 : float or int
      A float or int.
    num2: float or int
      Another float or int.
    operation : str
        Mathematical operation run .
    Returns
    -------
    result : float
    """

    do_calculation = True

    while do_calculation:
        func = calculator[operation]
        result = func(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        continue_calculation = str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to exist.: "))

        if continue_calculation == 'y':
            clear()
            num1 = result
            num2 = float(input("What's the second number?: "))
            operation = str(input("Pick an operation from the line above?: "))

        else:
            do_calculation = False
            return result

import time


def print2(first, second):
    print(first)
    print(second)


def print3(first, second, third):
    print(first)
    print(second)
    print(third)


def print4(first, second, third, fourth):
    print(first)
    print(second)
    print(third)
    print(fourth)

def print2w(first, second, wait: float):
    print(first)
    time.sleep(wait)
    print(second)


def print3w(first, second, third, wait: float):
    print(first)
    time.sleep(wait)
    print(second)
    time.sleep(wait)
    print(third)


def print4w(first, second, third, fourth, wait: float):
    print(first)
    time.sleep(wait)
    print(second)
    time.sleep(wait)
    print(third)
    time.sleep(wait)
    print(fourth)


def wait(wait: float):
    time.sleep(wait)
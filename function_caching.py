import time
from functools import lru_cache

@lru_cache(maxsize=3)
def some_work(n):
    #some task taking n seconds
    time.sleep(n)
    return n


if __name__=="__main__":
    print("Now Running Some Work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print("done calling again")
    some_work(3)
    print("called again")
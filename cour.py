def searcher():
    import time
    # some 4 seconds time consuming task
    book = "This is the book which can take time to read. harry it is very good book"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your book is in the book")
        else:
            print("text is not in the book")

try:
    search = searcher()
    print("Search Started")
    next(search)
    print("Next method run")
    search.send("harry")
    search.close()
    search.send("harry")
except StopIteration as e:
    print("error occured", e)




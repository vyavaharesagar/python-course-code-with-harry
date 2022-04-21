from typing import IO


f1 = open("harry.txt")
try:
    open("does.txt")
except EOFError as e:
    print("EOF error aa gaya hai", e)
except Exception as e:
    print(e)
except IOError as e:
    print("IO error aa gaya hai",e)
else:
    print("This will run only when except is not executed")
finally:

    # we use finally for code cleanUp
    # it will execute anyway
    print("Run this anyway")
    f1.close()

print("Important Stuff")


# finally and else


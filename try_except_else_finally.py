f1 = open("harry.txt")

try:
    open("does.txt")

except Exception as e:
    print(e)
finally:
    print("Run this anyway")
    f.close()
    f1.close()


print("Important Stuff")


# finally and else


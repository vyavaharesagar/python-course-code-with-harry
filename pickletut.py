import pickle

# # pickling
# cars = ["Audi","Maruti Suzuki","BMW","Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# depickling
file  = "mycar.pkl"
fileobj = open(file,"rb")
mycar = pickle.load(fileobj)
print(type(mycar))

f = open(r"C:\Users\anugu\Desktop\Anu Study\Python Notes\python 6 week\sample.txt",'r+')
#data = f.read()
f.write("Ducat")
f.seek(0)
print(f.read())
f.close()



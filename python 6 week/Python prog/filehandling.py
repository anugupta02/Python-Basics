'''
File Handling:-
object = open('filename.extention','mode')
Modes:-
    r (read) default mode
	w(write) always create new file
	a(append)
	+ (join mode):
	    r+ read and write
		w+ write and read
		a+ append and read
'''
'''
To create a sample file
f = open("sample.txt",'r')
#f.write("Hello Python")
print(f.read())
f.close()
'''
'''
Writing on txt file:
f = open("sample.txt",'a')
f.write("ABCD")
print("File Created")
f.close()
'''
'''
f = open("sample.txt",'r')
print(f.tell())
print(f.read())
print(f.tell())
f.seek(0)
print(f.read())
f.close()
'''


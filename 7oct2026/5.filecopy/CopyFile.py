f1=open("myfile.txt","r")
f2=open("myfile2.txt","w")
text=f1.read()
print(text)
for line in f1:
        f2.write(line)
f1.close()
f2.close()

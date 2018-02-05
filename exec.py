try:
    file=open("homework\\week 5\\str of letters returns the biggest letter.py","r")
    read=file.read()
    print('"%s"'%read)
    print("Execution of the code:\n")
    exec(read)

except IOError:
    print("cant open this file, or it isnt existing in this dir")

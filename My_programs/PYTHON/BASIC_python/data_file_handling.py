file=open("test457.txt","w")
file.write("hello world")
file.close()

f1=open("test457.txt","r")
#a=f1.read()
b=f1.readlines()
#content =f1.readline()
#print content[:]
#print a
print b
f1.close()



with open("test457.txt","a") as f:
    f.write("some string for demo purpose\n")
    f.write("another line for demo again\n")

"""

<r>	It opens a file in read-only mode while the file offset stays at the root.
<rb>	It opens a file in (binary + read-only) modes. And the offset remains at the root level.
<r+>	It opens the file in both (read + write) modes while the file offset is again at the root level.
<rb+>	It opens the file in (read + write + binary) modes. The file offset is again at the root level.
<w>	It allows write-level access to a file. If the file already exists, then it�ll get overwritten. It�ll create a new file if the same doesn�t exist.
<wb>	Use it to open a file for writing in binary format. Same behavior as for write-only mode.
<w+>	It opens a file in both (read + write) modes. Same behavior as for write-only mode.
<wb+>	It opens a file in (read + write + binary) modes. Same behavior as for write-only mode.
<a>	It opens the file in append mode. The offset goes to the end of the file. If the file doesn�t exist, then it gets created.
<ab>	It opens a file in (append + binary) modes. Same behavior as for append mode.
<a+>	It opens a file in (append + read) modes. Same behavior as for append mode.
<ab+>	It opens a file in (append + read + binary) modes. Same behavior as for append mode.




os.rename(cur_file, new_file)    # for rename
os.remove(file_name)             #for deleting file



<file.close()>	                Close the file. You need to reopen it for further access.

<file.flush()>            	Flush the internal buffer. It�s same as the <stdio>�s <fflush()> function.

<file.fileno()>          	Returns an integer file descriptor.
<file.isatty()>          	It returns true if file has a <tty> attached to it.
<file.next()>	                Returns the next line from the last offset.
<file.read(size)>	        Reads the given no. of bytes. It may read less if EOF is hit.
<file.readline(size)>	        It�ll read an entire line (trailing with a new line char) from the file.

<file.readlines(size_hint)>	It calls the <readline()> to read until EOF. It returns a list of
                                lines read from the file. If you pass <size_hint>, then it reads lines equalling the <size_hint> bytes.
                               
<file.seek(offset[, from])>	Sets the file�s current position.
<file.tell()>	                Returns the file�s current position.
<file.truncate(size)>	        Truncates the file�s size. If the optional size argument is present, the file is truncated to (at most) that size.
<file.write(string)>	        It writes a string to the file. And it doesn�t return any value.
<file.writelines(sequence)>	Writes a sequence of strings to the file. The sequence is possibly
                                an iterable object producing strings, typically a list of strings.



f = open('app.log', mode = 'r', encoding = 'utf-8')          #with encoding
f.close()"""

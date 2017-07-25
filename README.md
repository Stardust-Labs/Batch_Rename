# Batch_Rename

Batch Rename is a tool to rename files sequentially.  It is currently only designed and tested with Windows 8.

To use the tool, select all files that you want to rename and copy their paths into the "Old Paths" area.  They should look like this:

```
"C:\Path\To\File\foo.txt"
"C:\Path\To\File\bar.txt"
"C:\Path\To\File\spam.txt"
"C:\Path\To\File\eggs.txt"
```

Then, enter the new name in the "New name" field and hit the rename button.  The files will be renamed sequentially, for example if the new name is 'Hello World':

```
"C:\Path\To\File\Hello World 1.txt"
"C:\Path\To\File\Hello World 2.txt"
"C:\Path\To\File\Hello World 3.txt"
"C:\Path\To\File\Hello World 4.txt"
```

If the "create new dir" option is checked, the files will be moved into a directory within the current directory, using the new name.  So, if the new name is "Hello World" the files would be renamed to:

```
"C:\Path\To\File\Hello World\Hello World 1.txt"
"C:\Path\To\File\Hello World\Hello World 2.txt"
"C:\Path\To\File\Hello World\Hello World 3.txt"
"C:\Path\To\File\Hello World\Hello World 4.txt"
```

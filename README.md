# mmappython
Here's the example of Memory-Mapped I/O (Zero-Copy) in Python
In this example:

We open a file named "file.bin" in read mode using the open function.
We then use mmap to map the file into memory. The mmap.mmap function takes the file descriptor (file.fileno()), the length (0 for the entire file), mmap.MAP_SHARED for shared memory mapping, and mmap.PROT_READ to specify that we intend to read from the memory-mapped file.
Once the file is mapped into memory, we can access the data directly in the mmapped_data object. In this case, we read the first 100 bytes of the file without the need for an additional copy.
The file is automatically closed when we exit the with block.
This demonstrates the zero-copy technique of Memory-Mapped I/O, where data can be accessed directly from memory-mapped regions without the need for copying data between user and kernel space.










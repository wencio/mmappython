import mmap

# Open a file in read mode
with open("file.bin", "rb") as file:
    # Map the file into memory
    mmapped_data = mmap.mmap(file.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)

    # Access data directly in the mapped memory
    data = mmapped_data[:100]  # Read the first 100 bytes of the file

# The file is automatically closed when the 'with' block exits

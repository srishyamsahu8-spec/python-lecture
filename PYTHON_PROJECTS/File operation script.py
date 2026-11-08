

file_path = "sample_file.txt"

# 1. Create and write initial data
with open(file_path, "w") as f:
    f.write("Hello World! Learning Python File I/O operations.")

print("--- Reading File using seek() and tell() ---")
with open(file_path, "r") as f:
    # Read first 5 characters
    data = f.read(5)
    print(f"Read first 5 bytes: '{data}'")

    # Get current file pointer location
    current_position = f.tell()
    print(f"Current pointer position (tell()): {current_position}")

    # Move pointer directly to byte index 13
    f.seek(13)
    print(f"Pointer repositioned to (seek(13)): {f.tell()}")

    # Read remaining content from index 13
    remaining = f.read()
    print(f"Content from index 13 onwards: '{remaining}'")

print("\n--- Truncating File ---")
# 2. Shorten/Truncate file length
with open(file_path, "a") as f:
    f.truncate(12)  # Retain only first 12 characters ("Hello World!")

with open(file_path, "r") as f:
    print(f"Content after truncate(12): '{f.read()}'")
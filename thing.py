import os
import tempfile

# Save the original stdout fd
stdout_fd = os.dup(1)

# Create a temporary file and get its descriptor
with tempfile.TemporaryFile() as temp:
    # Redirect stdout to our temp file
    os.dup2(temp.fileno(), 1)

    # Run the command - output will go to our temp file
    exec('os.system("ls")')

    # Restore original stdout
    os.dup2(stdout_fd, 1)

    # Read the captured output
    temp.seek(0)
    output = temp.read().decode()
    print(output)

# Close the original fd copy
os.close(stdout_fd)

# 0x17 - Web Stack Debugging #3

For this debugging project, I was given a server running a wordpress site that was returning a 500 error. We were told to use the command `strace` to track down the error and fix it.

Once we fixed the error, we were asked to create a **Puppet File** that would fix this error automatically on any server.

## Main Takeaways:

Here were a few of my main takeaways:

### strace traces a specific program's system calls.

### strace -p <pid> will bind to a specific program and show you its syscalls in real time.

### strace -c <program-name> will give you a table of all the syscalls the program made, and how many times each syscall failed.

### You can use the `file_line` configuration to replace lines within a file using Puppet.

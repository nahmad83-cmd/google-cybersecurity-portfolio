# Algorithm for File Updates in Python

## Project Description

I developed a Python algorithm to maintain an allow list containing IP addresses authorized to access restricted information. The script removes addresses that are no longer authorized and rewrites the allow-list file with the updated contents.

## Workflow

1. Store the allow-list filename in `import_file`.
2. Open the file in read mode using `with open(import_file, "r")`.
3. Use `.read()` to load the file contents into a string.
4. Use `.split()` to convert the string into a list of IP addresses.
5. Iterate through the addresses and compare them with `remove_list`.
6. Remove addresses that should no longer have access.
7. Use `" ".join(ip_addresses)` to convert the list back into a string.
8. Open the original file in write mode and save the revised allow list.

## Security Relevance

The project demonstrates how Python can automate a repetitive access-control task. Rather than manually editing an allow list, the script applies a consistent process for removing unauthorized IP addresses.

## Skills Demonstrated

Python functions, file handling, strings, lists, loops, conditional statements, and security automation.

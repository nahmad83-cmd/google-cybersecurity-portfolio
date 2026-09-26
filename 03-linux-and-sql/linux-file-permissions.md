# Linux File Permissions

## Project Description

This project focused on managing Linux file and directory permissions to enforce appropriate access for users, groups, and others.

## Commands Used

- `ls -la` — inspect files, including hidden files, and review permission strings.
- `ls -l` — inspect standard directory contents and permissions.
- `chmod o-w project_k.txt` — remove write permission from others.
- `chmod g-x drafts` — remove group execute permission from the `drafts` directory.

## Security Tasks

I reviewed permission strings to identify read, write, and execute rights assigned to the user, group, and others. I then modified permissions so that unauthorized users could not write to protected files and access to a sensitive directory was restricted to the appropriate user.

The activity also included a hidden archived file whose write permissions needed to be removed while preserving required read access.

## Key Takeaway

Linux permissions are a practical implementation of access control and least privilege. Correctly assigning read, write, and execute permissions reduces the possibility of unauthorized modification or access to sensitive resources.

## Skills Demonstrated

Linux command line, `ls`, `chmod`, file permissions, directory permissions, user/group access control, and least privilege.

# Command Line notes

## file and directory permissions

`drwxr-xr-x   4 jasonhegarty  staff   128B  5 Jul 13:55 py101`

Broken down:
- **POS**
- 0:      Denotes if the entry is a Directory (d) or not (-)
- 1-3:    Denotes the Read (r) Write (w) and Execute (x) permissions for User 
- 4-6:    Denotes the Read (r) Write (w) and Execute (x) permissions for Group
- 7-9:    Denotes the Read (r) Write (w) and Execute (x) permissions for Other

*If no permissions are granted (-)*

## updating permissions

Use the chmod (Change Mode) command to update permissions.

`chmod +w py101'
The above will give Write permissions to the user for the py101 directory.

You can also set access levels for all 3 (USer, Group & Other) with 3 numbers from 0-7. The numbers represent the 8 permission level combinations. 

| Number | Permissions  |
|:------:|:-------------|
|0       |No permission granted.|

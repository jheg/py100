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

`chmod +w py101`

The above will give Write permissions to the user for the py101 directory.

You can also set access levels for all 3 (USer, Group & Other) with 3 numbers from 0-7. The numbers represent the 8 permission level combinations. 

| Number | Permissions  |
|:------:|:-------------|
|0       |No permission granted.|
|1       |Can execute.|
|2       |Can write.|
|3       |Can write and execute (1+2).|
|4       |Can read.|
|5       |Can read and execute (4+1).|
|6       |Can read and write (4+2).|
|7       |Can read, write and execute (4+2+1).|

Use chmod to update all 3

`chmod 777 py100`

The above will update the permissions from: 

`drwxr-xr-x   4 jasonhegarty  staff   128B  5 Jul 13:55 py101`

to: 

`drwxrwxrwx   4 jasonhegarty  staff   128B  5 Jul 13:55 py101`

## Exercises
1. Which user and group are assigned to the /etc folder on your computer?


```
ls -l
lrwxr-xr-x@  1 root  wheel    11B  9 Feb  2023 etc -> private/etc
```

User: root and group:'wheel'

2. Which user and group are assigned to the $HOME folder?

```
ls -l
drwxr-x---+ 51 jasonhegarty  staff  1632  3 Jul 21:26 jasonhegarty
```

User: jasonhegarty group: staff

*SOLUTION: ls -la $HOME then look for the . directory*

3. What are mary's permissions for the napkins file in the following outputs?
```
$ groups mary
mary travelers vip
$ ls -l custodian_closet
total 0
-rw-rw----  1 acmeair acmeair 0 Jul 21 17:57 napkins
-rw-rw----  1 acmeair acmeair 0 Jul 21 17:57 paper_towels
```

She has no access permissions on this file.


4. What are mary's permissions to the donuts file in the following example:

```
$ groups
mary travelers vip
$ ls -l vip_lounge
$ ls -l ./
...
-rw-rw----  1 acmeair  vip  0 Jul 21 17:57 donuts
...
```

She has read and write access because she belongs to the vip group

5. What are mary's permissions to the laptop file in the following example? What are the permissions for the group acmeinc?

```
$ ls -l vip_lounge
...
-r-xrwx---  1 mary acmeinc 0 Jul 21 17:57 laptop
...
```

Mary has read and execute access 
The acmeinc group has read, write and execute access

6. Practice using sudo to log in as root:

done.
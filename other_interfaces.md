# Other interfaces

## Changing context in Terminal

- Database management commands: mysql, psql, redis-client, mongo
- Text editors: vim, pico, nano, emacs
- REPLs (Read-Evaluate-Print-Loop), interactive scripting consoles: python, irb, node, php, -a
- System monitoring: top, htop
- Reading files or manuals: man, less, more
- Window/Session handling: byobu, screen, tmux

Each provide a totally new interface and you will need to exit (exit) to get back to the normal commaand line.

`$ top`

Activity monitor ^ Type q to exit

`$ python`

Launches the Python REPL. Type exit() to leave python

`$ irb`
Launches the Ruby REPL. Type exit to leave irb.

`$ node`
Launches Javascript REPL. Type Control-D (or Control-C with confirmation) to leave node. 

## Editors

`$ nano`
To exit without saving: Control + 'x' then n to discard changes
To Exit and Save: Control + o then Enter, then Control + x

`$ vim`
To exit without saving: Esc + :q!
To exit and Save: Esc + :wq

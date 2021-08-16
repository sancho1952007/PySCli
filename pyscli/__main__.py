from pyscli import *

cmd=cli('--hello', sensitive=False)

if cmd:
  print('You Successfully Used PySCli!')

else:
 print("""Welcome to PySCli!

This A Module to Get User Commands througn the Terminal/Command Prompt!

Try This:

  Windows:
    python -m pyscli --hello

  linux:
    python3 -m pyscli --hello 


THANK YOU FOR INSTALLING PySCli!

For Help/Official Repository, Visit: https://github.com/sancho1952007/PySCli""")
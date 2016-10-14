# CgkShell
## Contents

CgkShell is a set of libraries for interacting with the shell. Currently it
consists the following classes:

### PersistentBash:

Opens a persistent Bash shell that allows running commands in sequence without
losing the effects of the previous commands. E.g. you can issue a command that
sets up some environment variables once, and then give control back to your
Python application, allowing it to occasionally issue commands to this open
shell.

Example usage:

```
(cgklibs)[14:32] nighty@saltmine CgkShell$ ipython --no-banner
WARNING: Attempting to work in a virtualenv. If you encounter problems, please install IPython inside the virtualenv.

In [1]: from cgkshell import PersistentBash

In [2]: with PersistentBash.PersistentBash() as shell:
   ...:     shell.execute("export parrot='a stiff, bereft of life, it rests in peace'")
   ...:     import datetime
   ...:     print(datetime.datetime.today().year)
   ...:     out = shell.execute('export|grep parr')
   ...:     print('-----')
   ...:     print out
   ...:
2016
-----
declare -x parrot="a stiff, bereft of life, it rests in peace"


In [3]: exit
(cgklibs)[14:34] nighty@saltmine CgkShell$
```

## Installation

```sh
        python setup.py clean build install
```

## Licence

CgkShell is Copyright (c) 2016 Cegeka NV and released under the MIT license. See
LICENSE.txt for details.

## Contribute

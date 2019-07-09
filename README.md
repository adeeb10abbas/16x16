# gridcli
DWSL Grid Testbed client

Files taken from:
dwsl@dwsl-maas:/.virtualenvs/gridclienv/lib/python3.5/site-packages/gridcli/

Development requires virtualenv and virtualenvwrapper using directions similar to:
https://www.sneaku.com/2016/11/17/my-python-virtual-env-setup-instructions/

General process to build:
```
mkvirtualenv gridcli
workon gridcli
pip install -r requirements.txt
```
Then put the python code from this repo into:
~/.virtualenvs/gridcli/lib/python3.5/site-packages/gridcli

To run gridcli in this development system go to:
~/.virtualenvs/gridcli/bin

... and create something akin to the following file (gridcli - chmod to make rx runnable for all):

```
#!/userhomes/krd26/.virtualenvs/gridcli2/bin/python3
 
# -*- coding: utf-8 -*-
import re
import sys
import os # Added by Kapil to suppress warnings when creating containers on grid machines (requires pylxd 2.2.10)

os.environ['PYLXD_WARNINGS']="none" # Added by Kapil to suppress warnings when creating containers on grid machines (requires pylxd 2.2.10)

from gridcli.gridcli import main

if __name__ == '__main__':
	sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
	sys.exit(main())
```

To run:
```
python3 gridcli
```
... or run ./gridcli directly from the command line.  Note that if you do this, the first line of the gridcli file must specify the absolute path to the python3 interpreter in the virtualenvironment (e.g., #!/userhomes/krd26/.virtualenvs/gridcli2/bin/python3)

To stop virtual environment:
```
deactivate
```


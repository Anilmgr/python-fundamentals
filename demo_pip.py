## PIP is a package manager for Python packages ##

# pip install package/module
# pip uninstall package.module
# pip list
# Find more packages at https://pypi.org/

import camelcase

c = camelcase.CamelCase()
txt = "hello world"

print(c.hump(txt))

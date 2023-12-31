# pypkg-builder

A simple GUI based tool for packaging python.

**(formally template-pypackage-builder)

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Author](#author)
- [License](#license)
## Description
This tool walks you through the process of python packaging. Well it doesn't create actual package, more like a template with initial files to start with. The tool conatin following functions to help with package deployment.

* README maker
* LIcense creater
* setup file creater
* directory tree builder

## Installation

Install from pypi

```
pip install pypkg-builder
```

Install from GitHub

```
pip install git+https://github.com/dipson94/packagemaker
```

#### Install requires

* pkg_resources
* pyperclip
* flask
* datetime

## Usage

@terminal
```
pysetup
```

then this will appear on terminal

```
* Serving Flask app 'pypkg_builder.app'
* Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on http://127.0.0.1:5000
```

either click on the link or go to browser and type address http://127.0.0.1:5000.

(Note that the address might change(least likely happens) if the port is not available)

![pypkg](https://github.com/dipson94/packagemaker/assets/123653581/18409ead-38eb-4727-b762-b5d8161ccb87)


### Additional notes on package Building

Additional info about package building

**including path**

To include path in package file use the following command
```
import pkg_resources
relative_path=pkg_resources.resource_filename("packagemaker", "types")
```
This command is used if you want to use the path inside package in site-packages folder. Otherwise the path will be relative to the directory where you imported the package (while programming after importing the module).
Here relative_path refers to the path to types folder inside installed package pypkg-builder.

**`__init__.py` file handeling**

The following is the tree structure of a package showing basic files and directories. From main package directory in source, each modules ( also directories) contain an `__init__.py` file.
```
└── package_name
    ├── License.txt
    ├── MANIFEST.in
    ├── README.md
    ├── setup.py
    └── src
        └── package_name
            ├── __init__.py
            ├── module_1
            │   ├── __init__.py
            │   └── module_1.py
            ├── module_2
            │   ├── __init__.py
            │   └── module_2.py
            └── module_3
                ├── __init__.py
                └── module_3.py
```


There are numberous ways to handel  `__init__.py` file

Rule of thumb : keep all  `__init__.py` files empty at first and then start addding data from main  `__init__.py` file.

Methods

* if you wish to include all the functions and classes in one file, then write all in main  `__init__.py` file and discard other sub-directories (modules).
* if you wish to follow the structure shown in the illustration then you can include those modules in main  `__init__.py` file by 
```
from . import (module_1,module_2,module_3)
__all__ = ["module_1","module_2","module_3"]

```
* Another approach
```
from .module_1 import (function_1,function_2,function_3)
from .module_2 import (function_1,function_2,function_3)
from .module_3 import (function_1,function_2,function_3)
```
Here we are importing functions directly to main `__init__.py` file, so the functions are readly availble when the main module is called (or imported).

**Final thoughts**

pypkg-builder only helps with making a template or initial structure of a package. For making better package, work on the files manually using the editor.

## Author

Dipson

## License

GNU GPL V3

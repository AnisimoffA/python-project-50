[![Actions Status](https://github.com/AnisimoffA/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/AnisimoffA/python-project-50/actions)
[![Anisimoff-check](https://github.com/AnisimoffA/python-project-50/actions/workflows/my_personal_actions.yml/badge.svg)](https://github.com/AnisimoffA/python-project-50/actions/workflows/my_personal_actions.yml)
<a href="https://codeclimate.com/github/AnisimoffA/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/feb3e3685140c80999d4/maintainability" /></a>
[![Test Coverage](https://api.codeclimate.com/v1/badges/feb3e3685140c80999d4/test_coverage)](https://codeclimate.com/github/AnisimoffA/python-project-50/test_coverage)

## What is it?
___
This utility can find differences in 2 files. This information can be obtained in  three different formats.

Supported formats: 

- JSON

- JAML

Supported output formats: 
- intuitive text
- plain format
- JSON format 
  
## How to use?
___
 
This utility can be used in two ways:


#### CLI Tool

```python
usage: gendiff [-h] [-f FORMAT] first_file second_file

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```

### Common library

```
from gendiff import generate_diff


generate_diff('file1.json', 'file2.json', format="stylish / plain / json_format")
```

## Example of utility job with JSON files: 
___
[![asciicast](https://asciinema.org/a/OuUtdNym63f7f5DyQx2AzPYtV.svg)](https://asciinema.org/a/OuUtdNym63f7f5DyQx2AzPYtV)

## Example of package job with JAML files:
___ 
[![asciicast](https://asciinema.org/a/Monu9wlEUCWenuNX19jdcsIoe.svg)](https://asciinema.org/a/Monu9wlEUCWenuNX19jdcsIoe)

## Example of three types of information output:
___
[![asciicast](https://asciinema.org/a/EtYoCaltORvtbt0HIEhr5KusI.svg)](https://asciinema.org/a/EtYoCaltORvtbt0HIEhr5KusI)
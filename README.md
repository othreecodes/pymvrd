# pymvrd
Motor Vehicle Registration Information Search Portal Library for python

> Mvrd Library for Python

## Installation
Requires
 - Python > 2.7 
 - requests 
 - bs4

```shell
pip install requests #install requests
pip install bs4 #install bs4
pip install pymvrd #install pymvrd

```

## Usage

```python

from pymvrd.app import Mvrd

if __name__ == '__main__':
    plate_num = Mvrd('<plate_number>')
    details = plate_num.get_data()
    ## get_data() returns a dict
    print(details)

```
```python
#sample output
{'Isssue Date': '2011-11-24T13:26:31.630', 'Chasis Number': 'XXXXXXXXXXXX', 'Color': 'Ash', 'Plate Number': 'XXXXXXX', 'Model': 'Toyota Rav4', 'Expiry Date': '2012-11-23T13:26:31.630', 'Owner Name': 'Mr. .  XXXXXXXX', 'Vehicle Status': 'Default'}


```

Inspiration https://github.com/unicodeveloper/mvrd by @unicodeveloper

## Liscence
MIT




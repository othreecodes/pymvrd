# pymvrd ![https://pypi.python.org/pypi/pymvrd/0.6](https://badge.fury.io/py/pymvrd.svg)
Motor Vehicle Registration Information Search Portal Library for python

> Mvrd Library for Python

## Installation
Requires
 - Python > 2.7 

```shell
pip install pymvrd #install pymvrd

```

## Usage

```python

from pymvrd.app import Mvrd

if __name__ == '__main__':
    plate_num = Mvrd('<plate_number>')
    details = plate_num.get_data()
    # get_data() returns a dict
    print(details)
    
    # get indiviual Details
    print('Raw data ' + str(data))
    print("Number :" + data.number())
    print("Owner :" + data.owner_name())
    print("Issue date :" + str(data.issue_date()))
    print("Vehicle Status :" + data.vehicle_status())
    print("Chasis Number :" + data.chasis_number())
    print("color :" + data.color())
    print("Expiry :" + str(data.expiry_date()))
    print("Chasis Number :" + data.chasis_number())

    # Raises InvalidPlateError If the plate number does not exist

```

```python
#sample output
{'Isssue Date': '2011-11-24T13:26:31.630', 'Chasis Number': 'XXXXXXXXXXXX', 'Color': 'Ash', 'Plate Number': 'XXXXXXX', 'Model': 'Toyota Rav4', 'Expiry Date': '2012-11-23T13:26:31.630', 'Owner Name': 'Mr. .  XXXXXXXX', 'Vehicle Status': 'Default'}

Raw data {'Plate Number': 'XXXXXX', 'Model': 'Toyota Camry', 'Expiry Date': '2012-11-16T14:36:09.183', 'Color': 'Ash', 'Isssue Date': '2011-11-17T14:36:09.183', 'Chasis Number': 'XXXXXXXXX', 'Vehicle Status': 'Default', 'Owner Name': 'Mr. XXX XXXX  .'}
Number :XXXXX
Owner :Mr. XXX XXX XX  .
Issue date :2011-11-17 14:36:09
Vehicle Status :Default
Chasis Number :XXXXXXXXXXXXXXX
color :Ash
Expiry :2012-11-16 14:36:09
Chasis Number : XXXXXXXXXXX


```

Inspiration https://github.com/unicodeveloper/mvrd by @unicodeveloper

## Liscence
MIT




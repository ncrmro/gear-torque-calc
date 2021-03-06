A simple way to figure out how much torque different sized gears will get out of a a stepper motor (or any input).

Torque units are in nm (newton meters) and lengths should be in mm (millimeters).

Some background on why I wrote this package can be found [here](https://ncrmro.com/posts/writing_a_gear_torque_calculator)

## Usage

```python
from gear_torque_calc import get_torque
import pprint
pp = pprint.PrettyPrinter()
res = get_torque(drive_shaft_diameter=5, drive_shaft_torque=.2, gear_small_diameter=15, gear_large_diameter=55)
pp.pprint(res)
res = get_torque(drive_shaft_diameter=5, drive_shaft_torque=.2, gear_small_diameter=15, gear_large_diameter=55*2)
pp.pprint(res)
```

This should give you the following output
```python
{'gear_ratio': 7.333333333333333,
 'large_gear': {'force': 26.666666666666668,
                'radius': 55.0,
                'torque': 1.4666666666666668},
 'motor': {'force': 80.0, 'torque': 0.2},
 'small_gear': {'force': 26.666666666666668, 'radius': 7.5, 'torque': 0.2}}
{'gear_ratio': 3.6666666666666665,
 'large_gear': {'force': 26.666666666666668,
                'radius': 27.5,
                'torque': 0.7333333333333334},
 'motor': {'force': 80.0, 'torque': 0.2},
 'small_gear': {'force': 26.666666666666668, 'radius': 7.5, 'torque': 0.2}}
```

## Release

`python setup.py bdist_wheel`

`twine check dist/*`

`twine upload dist/*`

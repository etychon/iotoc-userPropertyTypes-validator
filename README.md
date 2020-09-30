# iotoc-userPropertyTypes-validator
IoT OC Validator for userPropertyTypes.xml with JSON encoded strings

Clone this repo:

```
git clone https://github.com/etychon/iotoc-userPropertyTypes-validator.git 
cd iotoc-userPropertyTypes-validator
```

Runs a check on a bad example:

```
python3 ./validate_xml.py bad_example/userPropertyTypes.xml | grep ERROR
```

It should display only errors, in this case there is an issue in the cell0Priority JSON definition:

`**JSON ERROR** {http://www.w3schools.com}seedValues: '[{ "key": "Provide 'cell0Priority' per device", "value": "${far.cell0Priority}" },`

Runs a check on a good example:

```
python3 ./validate_xml.py good_example/userPropertyTypes.xml | grep ERROR
```
There should be no output if there is no error.

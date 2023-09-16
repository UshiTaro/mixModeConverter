# mixMode S-parameter Converter
Convert to mixmode S-parameter from 4 port S-parameter.

## usage
Give the 4-port touchstone file name you want to convert and run it as below．  
`$ python mixModeConversion.py "4port touchstone filename"`  
2-port touchstone files separated into each mode will be output.
## Note
Of the 4 ports, odd numbers (1, 3) and even numbers (2, 4) must be paired.  
```
    1-|      |-2      1 -|dd.s2p|dc.s2p|-2
      |[.s4p]|    ->     |------+------|
    3-|      |-4      1'-|cd.s2p|cc.s2p|-2'
```

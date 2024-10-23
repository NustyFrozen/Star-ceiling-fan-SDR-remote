# RF Protocol for Star 7 ceiling fan's remote
### the rf protocol that the israel company "star" uses for their celling fans
![](./images/remote.jpg "star remote control")


### I've recorded the whole functionality of star's remote and here what i decoded using URH ([Universal Radio Hacker](https://github.com/jopohl/urh)):
<br>
Modulation: ASK (Amplitude Shift Keying)
<br>

``` py
Psuedo Protocol definition
Enum choice{
    ON      = 101101101100,
    OFF     = 100100100101,
    FAN3    = 100101101101,
    FAN2    = 101100101101,
    FAN1    = 100101101100,
    FAN-OFF = 100101101100
}
struct Command {
    bit[6] remote-serial;
    choice choice;
    byte Version;
}
# Example command: Turn On Light
# Command : 96d965b6db6db6cb6d8
# Serial: 96d965b6db6d
# Choice : b6c
# Version: b6d8
```
it is weirdly not 8 bit command size
<br>
## Vulnerabilities In The Protocol
### Simple RF replay attack
the messages are static therfore a simple replay attack works just fine as long as you know the serial

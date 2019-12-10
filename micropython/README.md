# Micropython on esp8266 and esp32

Instructions are well found at [micropython.org](https://micropython.org/download). First I want to know how big my flash size is. The code is 

```
esptool.exe --port COM5 --chip auto flash_id
```

For ESP32 you have to push the 'BOOT' button or connect IO0 to GND, otherwise the esptool is not connecting.

## Prime numbers to 10000

This took 11375 ms on an esp32 with 160 MHz:

```
import math
import time

last = 10000

start = time.ticks_ms()
print("Prime numbers to 10000")

print('2, 3, 5, 7',end='')
for number in range(11, last, 2):
    prime = 1
    for divider in range(2, int(math.sqrt(number))+1, 1):
        if number/divider == int(number/divider):
            prime = 0

    if prime == 1:
        print(',', number,end='')
        
end = time.ticks_ms()
print('\nThis took:', (end - start), 'ms.')
```

In uPyCraft V1.0 the output is lagging behind the streaming of numbers from the esp.

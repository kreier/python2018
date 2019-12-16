# Python 2018

My first steps in python, starting with the workshop at AIS on *November 16, 2018*.

Hello World! and calculating prime numbers work well.

## December 2019

Now python runs on esp8266 and esp32 as well. With REPL you see the result immideately.

It is also possible to compare the code in python and Arduino C accross devices. 

### Prime numbers to 10000

Time in milliseconds.

| esp8266 | esp32 | esp32 | raspberry pi 4 | Xeon X5550  |
|---------|-------|-------|----------------|-------------|
| 40      | 40    | 240   | 1400           | 3060        |
| 24746   |       | 8012  | 215            | 16          |
|         |       | 2516  |                |             |

### Web server on esp8266 and esp32

Simple project, located in [micropython/webserver](micropython/webserver) and copied from [RandomNerdTutorials](https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/) it takes 10 minutes to create a local webserver:

![webserver](micropython/webserver/20191216.gif)


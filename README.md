# elliebox

**WHAT IS IT**
Elliebox is a box made for my niece, Emmanuelle "Ellie" Joy Fischer. It consists of three arcade buttons that light up, each playing a sound when pressed, and it plays music when all three lights are lit. There are also six slots for blocks in the shape of "A B C" and "1 2 3." The box originally contained a puzzle I bought on the internet.


~Technical Notes~

Elliebox uses the Adafruit MAX98357 I2S Class-D Mono Amp to send audio via I2S to a speaker

Installation instructions are partially found here:
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/raspberry-pi-usage

You will also want to follow the instructions here in order to ensure you do not get pops and clicks when a sound file starts and stops:
https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/pi-i2s-tweaks

You can play audio from omxplayer through 'alsa', which supports I2S, using the bash command 'omxplayer -o alsa' followed by the file you want to play.

I had a lot of trouble initially getting my raspberry pi to work with the amp because I *think* that some of the things I'd set up in order to use PWM for neopixels on the ws281x were directly conflicting. To be honest, I had to do a weird combination of things to get audio working. I partially had to undo some of the documented stuff here:

https://github.com/jgarff/rpi_ws281x

Specifically, I commented out the "blacklist" line. Although I don't know if that helped.

I also uncommented the 'dtparam=i2s=on' line in /boot/config.txt

I also did NOT allow the adafruit bash script to turn on the /dev/zero background service because it seemed like every time I enabled it, it broke the audio.



# Hackvent 2017  
## Normal Days:  
### Day 1:  
This years hackvent started out pretty easy, given was the code `HV17-5YRS-4evr-(taken from 2014-12-01)-(taken from 2015-12-01)-(taken from 2016-12-01)`,
in order to solve this day you had to search for the solutions of 12-01-2014, 12-01-2015 and 12-01-2016 and fill in the missing parts.
  
Flag: HV17-5YRS-4evr-IJHy-oXP1-c6Lw  
Reached Points: 2/2

### Day 2:  
Day 2's hint was "The fifth power of two" (2^5=32), it had the file "wishlist.txt" attached.
Since a simple base32 encoded file would be too easy, you had to dig deeper.  
The file was encoded 32 times with base64, I've solved this with a simple python script. 
  
Script: day2.py  
Flag: HV17-Th3F-1fth-Pow3-r0f2-is32  
Reached Points: 2/2

### Day 3:  
Day 3's attachment was a pretty long logcat logfile. The two suspicious lines were the ones with 137 in the second & third column, since they had a different indentation than the rest of the file.  
The first line with 137 said `FAILED TO SEND RAW PDU MESSAGE`, the second one `DEBUG: I 07914400000000F001000B913173317331F300003AC7F79B0C52BEC52190F37D07D1C3EB32888E2E838CECF05907425A63B7161D1D9BB7D2F337BB459E8FD12D188CDD6E85CFE931`.  
PDUs (Packet Data Unit) are used for encoding SMS messages over the network. With a [pdu decoder tool](https://www.diafaan.com/sms-tutorials/gsm-modem-tutorial/online-sms-pdu-decoder/) you can decode the PDU & get the flag which in in the Message field.
  
Flag: HV17-th1s-isol-dsch-00lm-agic  
Reached Points: 2/2

### Day 4:  
Day 4 was rather hard. After some playing around with the file I saw the hint "I'm not fond of this challenge" in the chat.  
Thanks to this hint I extracted the font with https://www.aconvert.com/pdf/extract/ and opened it in [fontforge](https://github.com/fontforge/fontforge), in the font file there was the key hidden.
  
Flag: HV17-RP7W-DU6t-Z3qA-jwBz-jItj  
Reached Points: 3/3

### Day 5:  
Day 5's description contained 6 crc32 hashed strings, with Python, binascii & itertools I created a brute force script which hashes every existing 4 characters long combination of letters & numbers until it finds all of the 6 hashed parts. 
  
Script: day5.py  
Flag: HV17-RP7W-DU6t-Z3qA-jwBz-jItj  
Reached Points: 3/3

### Day 6:  
Thanks to the description "Make sure Santa visits every country", day6 pretty easy to figure out.  
The attached link `http://challenges.hackvent.hacking-lab.com:4200/` led to a site, which showed another country name, encoded as QR code on every reload.
I used a qr code decode API + Python in order to decode all qr codes until I encountered one which contains "HV".  
  
Script: day6.py  
Flag: HV17-eCFw-J4xX-buy3-8pzG-kd3M  
Reached Points: 3/3

### Day 7:  
Day 7's attachment was a .FILE archive, I unpacked it with `unzip` in order to get the .IMA file. Via `strings SANTA.IMA | grep HV17` I was able to find the path  
`Y*C:\Hackvent\HV17-UCyz-0yEU-d90O-vSqS-Sd64.exe`
  
Flag: HV17-UCyz-0yEU-d90O-vSqS-Sd64  
Reached Points: 3/3

### Day 8:  
Day was a small reverse-engineering challenge where you had to find the wanted input.   
In order to get the flag, you had to replace `__1337`, which will now print the code `C=SANTA("?") if C=="1787569".....`, which means the wanted input is 1787569.  
Replace the print with `__1337` again and you will get the flag.
  
Flag: HV17-th1s-ju5t-l1k3-j5sf-uck!  
Reached Points: 3/3

### Day 9:  
Day 9 was awesome! In order to get the flag, you had to write a script which "peels" the json onion which you were given.  
Every layer of the onion was a json code, which had at least the fields "op" and "content".  
op was the operation you had to apply (map, b64, xor, nul or rev), and content was the string you had to apply the operation on.  

There was a trap tho; The json was always in a json array and some later layers would have two operations in one file,  
if you would only parse the first item in the array and ignore the other ones, you would get the flag `THIS-ISNO-THEF-LAGR-EALL-Y...`, by parsing & processing ALL of the array entries you did get the right flag.
    
Operations:  
| op   | Description                                                                             |
| ---- | --------------------------------------------------------------------------------------- |
| map  | Generate a lookup table with the fields mapFrom & mapTo, apply the table to the content |
| gzip | Base64 decode the content and gzip decompress it afterwards                             |
| b64  | Base64 decode the content                                                               |
| nul  | Nothing, just read the content                                                          |
| xor  | Apply a xor to every byte in the content with the given mask                            |
| rev  | Reverse the content                                                                     |
| flag | Nothing, you've got the flag                                                            |

Flag: HV17-Ip11-9CaB-JvCf-d5Nq-ffyi  
Reached Points: 3/3

## Hidden Challenges:  
### Hidden 1:  
If you try to access a invalid day in the challenge.php file, you're greeted by the message
`The resource (#XXX) you are trying to access, is not (yet) for your eyes.`  
The number XXX gets bigger/smaller the further you de/increase the day paremeter. If it reaches 0 (day=1984) you'll see the message
`The resource you are trying to access, is hidden in the header.`  
As the message states, you just have to look into the header, which contains "Flag: HV17-4llw-aysL-00ki-nTh3-H34d" 
  
Flag: HV17-4llw-aysL-00ki-nTh3-H34d  
Reached Points: 1/1

### Hidden 3:  
The robots.txt file was one of the first files I checked while searching for hidden eggs. Initialy I thought that the content was just a joke and there was no sense behind it.
Some days later I checked it again and was able to find my path to the humans.txt, with a stopover at people.txt.

Flag: HV17-bz7q-zrfD-XnGz-fQos-wr2A  
Reached Points: 1/1

### Hidden 4:  
The css/ folder was found with the tool dirb (wordlist common.txt), in this directory there was a file called egg.png which contained a QR code and the number 27.
At first I thought that it was a part of the hacky easter competition, but after some searching around I noticed that the hacky easter competition didn't last for 27 days. Due to the code starting with HE17 instead of HV17 I initially thought I had to use some kind of chifre to translate the HE to HV. After some messing around I notice that it was indeed a valid code and there was no need to decrypt it in some way.

Flag: HE17-W3ll-T00E-arly-forT-his!  
Reached Points: 1/1

### Hidden 5:  
Hidden Egg 5 was hidden on the subdomain challenges.hackvent.hacking-lab.com. Via `nmap -p 1-65535 -T4 -A -v challenges.hackvent.hacking-lab.com` 
you can see besides http, https & ssl a suspicious open tcp port - which is 23/telnet. (Who uses telnet today [(besides for watching star wars?)](http://blinkenlights.nl/services.html#starwars) Upon connecting, I was greeted by Santa Claus himself.
 
Flag: HV17-UH4X-PPLE-ANND-IH4X-T1ME  
Reached Points: 1/1

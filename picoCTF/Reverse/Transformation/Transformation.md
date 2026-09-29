# Transformation - picoCTF - Reverse 

# Mission 
### Find the flag with format academy{...}

# Setup 

Cylab provide a binary file <a href="https://github.com/shr1mppp/shr1mp-solved-ctf/blob/main/picoCTF/Reverse/Transformation/enc">enc. </a> and a line 

```python 
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

```

# Analysis 
First we open the enc. file to see what inside 

`慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽`

Oh, what was that, a bunch of Chinese, Korean, Japanese character?

Could it be...... UTF-16 or something realated?

Ughhhh idk what it is, lets read the line Cylab provide us 

`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])` 

Hmmmmm, I don't understand a thing so I will rewrite it

```python
  for i in range(0, len(flag), 2)
      ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
  ('' part could be enc)
```

Now its look more readable to me. 

So the code is talk about how the flag encrypt to enc. 
Notice the part `chr((ord(flag[i]) << 8) + ord(flag[i + 1])` look like code encrypt the flag by 

Take order of flag[i] left-shifted it by 8-bit then plus order of flag[i+1], then puts the character of the sum number into `enc`. (flag is a character string)

Ohhhhhhh, now I understand that each character in `enc` is formed by 2 characters from `flag`.

So how we can decrypt enc to get the flag ?

  To solve the problem we need to reverse the `encrypt` code. But we can't do anything with character so we need to transform each character first, in this problem I will transfer each character take `ord()` from each character of `enc`. But for visualization problem, I will use `hex` to perform for you guys to easy to see the bitwise.

```text
Why I use hex to visualize instead of binary?

- Not binary because it will be a pain in ass if we perform 16 number 0, 1, it just unefficient, slow, and hard to perform.

-> So `hex` is the superior here. We know that each character of `hex` equal to 4-bit of binary, so we can perform character more easily with hex, we just need **4 or 2 characters** of hex to perform(efficient and fast to write).  
```
Let's take the first character from enc `慣`

`慣 = 24931 = 0x6163`

We have `0x6163` with each character after `0x` is equal to 4-bit. 

We know that the algorithm to encrypt will need to left-shifted a character by 8-bit then add another character into it. 

Hmmmmm, take an example to understand it more clearly. 

Like

`flag = "ab"` 

`enc = chr((ord('a') << 8) + ord('b'))`

ord('a') = 0x61

ord('b') = 0x62

`ord('a') << 8 = 0x6100`

-each number equal to 4-bit so left-shifted 8-bit equal left-shift 2 number-

`0x6100 + 0x62` 

`= 0x6162 = 24930 = 慢`  

Ohhhh, you can see that `hex` with format `0xabcd`, `0xab` is the hex of first character, `0xcd` is the hex of second character. 

Thats miracleeeeeeeeeeeee

Return to `慣 = 24931 = 0x6163`, see that we have the form of `0xabcd` so we can split into 2 parts. `0x61` and `0x63`, which can tranfers to `a` and `c`. Yehhhhhhhhhhh


# Solution
We understand the rule here, but if I continue to do that with all the characters from enc, I would rather kill myself. So we gonna write some code here. 

```python
enc = "慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽"
flag = ""
  
for c in enc:
    c = ord(c) 
    high_hex = (c >> 8)
    low_hex = c & 0xff
    flag += chr(high_hex) + chr(low_hex)
      
print(flag)
```

The code run as order 

`take order of each character in enc`

-> high_hex or ab in `0xabcd` we right-shifted it by 8-bit, it will become `0x00ab`, the leading 0's mean nothing so its will be just `0xab`.

-> low_hex or cd in `0xabcd` we just need to make ab part disappear, so we use `AND with 0xff`. Read below.

-> So `flag` just equal to all those part combine, and we alrighttttttttttttttt

## FLAGGGGGGGGGGG
```text
  academy{16_bits_inst34d_of_8_790ba37e}
```

## Explain the `AND with 0xff`

`0xff = 1111 1111(in binary)` 

Remind that bit-wise `AND` has 2 inputs, and if all inputs are 1, the output is 1, if one of input is 0, the output is 0.

Take `慣 = 24931 = 0x6163` as an example 

In binary its will be 

`0x6163 = 0110 0001 0110 0011`

The solved code will follow:

low_hex = `0x6163` = `0110 0001 0110 0011`

When `AND with 0x00ff`

0110 0001 0110 0011
0000 0000 1111 1111
0000 0000 0110 0011

`0x6163 & 0x00ff = 0x0063 = 'c'`

So the lower 8-bit will remain the same, and the higher 8-bit disappear. So we can save the lower 8-bit value !!!

That's why we use `AND` bitwise here !!!
 


 

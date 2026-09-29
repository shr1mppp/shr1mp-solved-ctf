enc = "慣慤敭祻ㄶ形楴獟楮獴㌴摟潦弸強㤰扡㌷敽"
flag = ""
for c in enc:
    c = ord(c) 
    high_hex = (c >> 8) & 0xff
    low_hex = c & 0xff
    flag += chr(high_hex) + chr(low_hex)

print(flag)
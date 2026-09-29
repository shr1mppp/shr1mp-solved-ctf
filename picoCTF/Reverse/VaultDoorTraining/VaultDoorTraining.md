# Vault Door Training - picoCTF - Reverse 

# Mission 
### Find the flag with format academy{...}

# Setup 
## Cylab provide us a java file name <a href=""> vaultdoortraining.java</a>

# Analysis 

I believe that this problem is the easiest in all of Reverse Engineer problem cause the file contain flag itself, just need a little adjust to match the flag format and its alrighttttttt.

The code start with a class called `VaultDoorTraining` 

With this block of code 

```java
class VaultDoorTraining {                             
  public static void main(String args[]) {               
    VaultDoorTraining vaultDoor = new VaultDoorTraining(); 
    Scanner scanner = new Scanner(System.in);              
    System.out.print("Enter vault password: ");            
    String userInput = scanner.next();                     
    String input = userInput.substring("academy{".length(),userInput.length()-1);
    if (vaultDoor.checkPassword(input)) {                                            
      System.out.println("Access granted.");
    } 
    else {                                                                 
          System.out.println("Access denied!");                                  
      }             
}                                                     
```
The important line is 
```java 
String input = userInput.substring("academy{".length(),userInput.length()-1);
```

Which means that if input string has the format of `academy{some_things` it will cut **academy{** part and last character from the input string leave the string with just `some_thing`. And if input string doesn't has that format, program will cut from the 1st to 8th character and the last character of it.

Eg. 
```text
Input_string = academy{shrimp

Output will be `shrim`
```
```text
Input_string = shrimponiichan

Output will be `iicha` //cut `shrimpon` and letter `n`
```


The code just basically run like this 

```text
       Demand user to enter password
                   ↓
            Input processing
                   ↓
        Program take the part remain
    and compare it with the og password
                   ↓
   If its right print "Access granted" 
        else print "Access denied"
  
```

Ughhhh.. The code continue with

```java
    // The password is below. Is it safe to put the password in the source code?    
    // What if somebody stole our source code? Then they would know what our
    // password is. Hmm... I will think of some ways to improve the security
    // on the other doors.
    // -Minion #9567
    public boolean checkPassword(String password) {
        return password.equals("w4rm1ng_Up_w1tH_jAv4_8352733cecd");
    }
```

You can see that... The password is right there `"w4rm1ng_Up_w1tH_jAv4_8352733cecd"`

# Solution 
Run the java code, by terminal or ide or something

Enter academy{w4rm1ng_Up_w1tH_jAv4_8352733cecd}, get Access granted 

So FLAGGGGGGG will be 

`academy{w4rm1ng_Up_w1tH_jAv4_8352733cecd}`

Ugh... its just like that?

# Postscript
### What I learn from this problem?

Back to the comment author leave in code 

```text
    // The password is below. Is it safe to put the password in the source code?    
    // What if somebody stole our source code? Then they would know what our password is. 
    Hmm... I will think of some ways to improve the security on the other doors.
    // -Minion #9567
```

If you saved the password, key or something to secure access to your program inside source code, there are many chances someone could read it and use it to sneak into your program(or your server).

So the solution is saved it somewhere else or have a `input processing` or a better `checker`.

In the problem we can see author -Minion #9567 use `input processing` to force input to have somewhat a format(basically just delete first 8 character and last character) to grant access of the program but its still kinda naive, just a `string processing`. Program with higher secure will have `input process` or `checker` related to `hash` or some `encryption`.





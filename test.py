def enigma(msg,key):
    ls = list(msg)
    for i in range(len(ls)):
        ls[i] = chr(ord(ls[i]) ^ key)
    return "".join(ls)

print("WELCOME.")
msg = input("ENTER A STRING TO ENCODE OR DECODE\n> ")
key = int(input("ENTER A KEY\n> "))
print(enigma(msg,key))

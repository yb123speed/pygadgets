import sys
if len(sys.argv) < 2:
    print("you have input nothing")
    sys.exit()
option = sys.argv[1]
print(r'''
_______
<%s    >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\  
                ||----w |
                ||      ||''' % option)

# Zig-zag program
import time, sys
indent = 0
indentincrease = True
try:
    while True:
        print(" " * indent, end="")
        print("********")
        time.sleep(0.1) # pause for 0.1 second

        if indentincrease:
            indent = indent + 1
            if indent == 20:
                indentincrease = False
        else:
            indent = indent - 1
            if indent == 0:
                indentincrease = True
except KeyboardInterrupt:
    sys.exit()
# This is an example of an infinite loop that has been edited to implment break/continue
# statements to gracefully deal with potential endless loops.

import time

x = 0

while True:
    x = x + 1
    if x == 2:
        print('Skipping 2')
        time.sleep(3)
        continue
    if x == 5:
        print('Breaking...')
        time.sleep(3)
        break
    print(x)
print('Finished!')

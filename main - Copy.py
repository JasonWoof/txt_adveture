import time
import sys

def slow_print (text):
    for c in text:
        sys.stdout.write (c)
        time.sleep (.02)
    print('')
slow_print ("fhtb  ht bt yt hyth hyth yt hyht lttext")
slow_print ("text t bgt gt bgt bb bt bbgt bgt bgt")
slow_print ("text t bgt gt bgt bb bt bbgt bgt bgt")
slow_print ("text t bgt gt bgt bb bt bbgt bgt bgt")

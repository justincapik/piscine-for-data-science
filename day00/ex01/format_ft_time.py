import time

cur = time.time()
print ("Seconds since January 1, 1970: {:,.4f} or {:.2e} in scientific notation".format(cur, cur))
print (" ".join(time.ctime(cur).split()[i] for i in [1, 2, 4]))
from time import sleep, time

# calculate time with sleep
print("Start with delay")
sleep(5)
print("End")

# epoch time
# Epoch time, also known as Unix time or POSIX time, 
# represents the number of seconds that have elapsed 
# since the Unix epoch (January 1, 1970, at 00:00:00 UTC).

print("Epoch time")
epoch_time = time()
print(epoch_time)

# calculate time with epoch
# print("Start")
# start = time()
# sleep(2)
# end = time()
# print(f"Time taken: {end - start} seconds")

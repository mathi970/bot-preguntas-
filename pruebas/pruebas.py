import time

current_time = time.time()


print(f"el tiempo actual {current_time}")

formatted_time = time.strftime("%H:%M:%S", time.localtime())
print(f"Hora actual: {formatted_time}")
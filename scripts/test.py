
import os


files = [f for f in os.listdir('.') if not f.startswith('.')]
print('\n'.join(files))

for i in range(100):
    print(i,i**23)

#this script installes the needed moduals to run the gui version of  M-E


import os
import time

print('-----------------------------------------------------------------')
print('RPI Installer For M-E')
print('Coded by MDH')
print('This softwear is under a free to use licence')
print('-----------------------------------------------------------------')
time.sleep(5)
EULA = input('Do you agree to let this program add the needed moduals to run M-E? (Y/n):')

if EULA == 'N':
   break

time.sleep(3)
print('------------------------------------------------------------------')
print('Installing System Updates')
print('-------------------------------------------------------------------')
time.sleep(3)
os.system('sudo apt-get update')
os.system('sudo apt-get install')
time.sleep(3)
print('-------------------------------------------------------------------')
print('System has been updated')
time.sleep(3)
print('installing moduals')
time.sleep(3)
print('installing pip for python3')
time.sleep(3)
os.system('sudo apt-get install python3-pip')
time.sleep()
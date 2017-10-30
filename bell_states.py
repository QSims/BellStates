####################################

#Created by: Simsarul Haq Vengasseri
#Date: 30/10/2017

# This program is for generating bell states.
# Please specify the path to the referenceqvm directory to import the api library.



import sys
sys.path.insert(0, '/home/infinitylabs/Documents/QSimulations/QSims/reference-qvm/referenceqvm')
import api
import pyquil.quil as pq
from pyquil.gates import *

qvm = api.SyncConnection()

def generate_bell_state(bell_state):
    if(bell_state==0):
        p = pq.Program().inst(I(0), I(1), H(0), CNOT(0,1))
    elif(bell_state==1):
        p = pq.Program().inst(I(0), X(1), H(0), CNOT(0,1))
    elif(bell_state==2):
        p = pq.Program().inst(X(0), I(1), H(0), CNOT(0,1))
    elif(bell_state==3):
        p = pq.Program().inst(X(0), X(1),H(0), CNOT(0,1))
    qbit_value, cbit_value = qvm.wavefunction(p)
    return qbit_value


if __name__ == '__main__':
    if (len(sys.argv)>1):
        try:
            bell_state = int(sys.argv[1])
            if(bell_state==0 or bell_state==1 or bell_state==2 or bell_state==3):
                result = generate_bell_state(bell_state)
                print result
            else:
                print "Please specify a correct argument to program: \n 0 for B00 \n 1 for B01 \n 2 for B10 \n 3 for B11 \n"

        except ValueError:
            print ("Enter an integer as argument.")
            sys.exit(1)
    else:
        print "Please specify a value as an argument to program: \n 0 for B00 \n 1 for B01 \n 2 for B10 \n 3 for B11 \n"

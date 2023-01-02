
import queue
import sys
import librosa
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import os
import time
import scipy.fftpack



sample_size = 44100


def clear():
    os.system("clear")

        
#functions to tune specific strings from the venezuelan Cuatro

def tune_first_string(signal, note):
    clear()
    print(signal)
    print(note)
    if signal == 247:
	    print("It's tuned!'")
	
    elif signal < 247 and signal > 243:
	    print(" Go a bit higher")
		
    elif signal < 243 :
	    print(" Go higher! ")
	
    elif signal > 247 and signal < 251:
	    print("Go a bit lower! ")
    else:
	    print("Go lower! ")
    


def tune_second_string(signal, note):
    clear()
    print(signal)
    print(note)
    if signal == 185:
	    print("It's tuned!'")
	
    elif signal < 185 and signal > 181:
	    print(" Go a bit higher")
		
    elif signal < 181 :
	    print(" Go higher! ")
	
    elif signal > 247 and signal < 189:
	    print("Go a bit lower! ")
    else:
	    print("Go lower! ")
		

def tune_third_string(signal, note):
    clear()
    print(signal)
    print(note)
    if signal == 147:
	    print("It's tuned!'")
    elif signal < 147 and signal > 143:

	    print(" Go a bit higher")	
    elif signal < 143 :
	    print(" Go higher! ")
	
    elif signal > 147 and signal < 151:
	    print("Go a bit lower! ")
    else:
        print("Go lower! ")


def tune_fourth_string(signal, note):
    clear()
    print(signal)
    print(note)

    if signal == 220:
	    print("It's tuned!'")
	
    elif signal < 220 and signal > 216:
	    print(" Go a bit higher")
		
    elif signal < 216 :
	    print(" Go higher! ")
	
    elif signal > 220 and signal < 224:
	    print("Go a bit lower! ")
    else:
	    print("Go lower! ")
		
def tuner():

    print("Welcome to Cuatro Tuner !")
    

    print("\n[1] Enter 1 to tune first string.")
    print("[2] Enter 2 to tune second string.")
    print("[3] Enter 3 to tune third string.")
    print("[4] Enter 4 to tune fourth string.")
    print("[q] Enter q to quit.")
        

       
tuner()
choose_string = input("\nWhich string would you like to tune?\n")




def audio_callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    
     
    if status:
        print(status, file=sys.stderr)
    
    if any(indata):
       
        indata_np = np.array([i[0] for i in indata]) 
        f0 = np.round(librosa.yin(indata_np, fmin = librosa.note_to_hz('C2'), fmax= librosa.note_to_hz('C7')) * 2, 0)
        notes = librosa.hz_to_note(f0[1])
        clear()
        

        if choose_string == '1':

            print(tune_first_string(f0[1], notes))
                
        elif choose_string == '2':

            print(tune_second_string(f0[1], notes))
        elif choose_string == '3':

            print(tune_third_string(f0[1], notes))
        elif choose_string == '4':
        
            print(tune_fourth_string(f0[1], notes))
        else:
            print("There are just 4 strings!!")
        
    


try:
        

      

    with sd.InputStream(channels=1, callback=audio_callback, blocksize=5000, samplerate=sample_size):
        plt.show()
        while True:
            time.sleep(0.5)
except Exception as exc:
    print(str(exc))
        

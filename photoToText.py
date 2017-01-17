from __future__ import print_function		# for python2 compat
import tkinter as tk
from tkinter.filedialog import askopenfilename
 
from PIL import Image 
import numpy as np

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))

def chooseFile():
    tk.Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    # print(filename) just to be sure if we got the file that we've chosen
    return filename;

def makeArt():
    f = chooseFile()
    SC = .10   # size of the image
    GCF = 3    # tonning of the image
    WCF = 7/4  # width of the image

    img = Image.open(f)
    S = ( round(img.size[0]*SC*WCF), round(img.size[1]*SC) )
    img = np.sum( np.asarray( img.resize(S) ), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
 
    print( "\n".join( ("".join(r) for r in chars[img.astype(int)]) ) )

if __name__=='__main__':
    import sys 

    makeArt()

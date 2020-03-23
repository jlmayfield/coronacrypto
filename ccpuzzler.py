#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:16:59 2020

@author: jlmayfield4
"""

import sys
import argparse
import string
import datetime
import os
from cipher.encipher import encipher
from cipher.monoalphabets import MonoAlphabet
import cipher.monosequences as ms


def buildparser():
    """
    Constructs CLI argument parser for ccpuzzler script. 

    Returns
    -------
    parser : argparser        

    """
    parser = argparse.ArgumentParser(description='Encipher something fun')
    parser.add_argument('fname',nargs=1)
    parser.add_argument('vnum',nargs=1)
    parser.add_argument('-s',type=int,default=0)
    parser.add_argument('-k',type=str,default='')
    parser.add_argument('-r')
    return parser   

def logkeygen(log,args):
    """
    Writes key generation parameters to the puzzle log

    Parameters
    ----------
    log : file
        writable file for logging puzzle details
    args : dict
        dictionary of command-line arguments used for the puzzle

    Returns
    -------
    None.

    """
    if args['k'] != '':
        log.write('Keyword: ' + args['k'] + '\n')
    if args['s'] != 0:
        log.write('Shift: {0}\n'.format(args['s']))
    if args['r']:
        log.write('Reversed\n')

def logpuzzle(args,plain,cipher,key):
    """
    Create a log of the Coronacrypto puzzle

    Parameters
    ----------
    args : dict
        CLI arguments used to generate the puzzle
    plain : str
        plaintext
    cipher : str
        ciphertext
    key : str
        key

    Returns
    -------
    None.

    """
    # timestamp
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d")
    # open log file
    try:
        filename = 'cc-'+args['vnum'][0]+'-'+timestamp+'.txt'
        fullpath = os.path.abspath('series/series1/' + filename)
        log = open(fullpath,'w')
    except OSError:
        sys.exit('Cannot open log for writting buddy.')
        # log header info    
    log.write('Coronacrypto Puzzle\n------------------\n')
    log.write('Series-Puzzle Number: ' + args['vnum'][0] + '\n')
    log.write('Created: ' + now.strftime("%Y-%m-%d %H:%M:%S"))
    log.write('\n\n')
    # log plaintext    
    log.write("Plaintext\n---------\n")
    log.write(plain)
    log.write('\n')
    # log details of the key
    log.write('Key\n---\n')
    logkeygen(log,args)    
    log.write(key)
    log.write('\n')
    # log ciphertext
    log.write('Ciphertext\n----------\n')
    log.write('\n')
    log.write(cipher)
    

if __name__ == '__main__':
    parser = buildparser()
    args = vars(parser.parse_args())
    # open the file, or not
    try:
        plain_path = os.path.abspath(args['fname'][0])
        plain_file = open(plain_path,'r')
    except OSError:
        sys.exit('That is not a file buddy.')
    # cipher seq Order Of Ops: keyword, shift, reverse
    c_seq = string.ascii_uppercase
    if args['k']:
        c_seq = ms.keyword(args['k'])
    if args['s']:
        c_seq = ms.shift(args['s'],c_seq)
    if args['r']:
        c_seq = ms.reverse(c_seq)
    # get that alphabet
    abet = MonoAlphabet(c_seq)
    # and the encipher dictionary
    plaintext = plain_file.read()
    # let's do this
    ciphertext = encipher(plaintext,abet)
    #print(decipher(ciphertext,abet))    
    #log the puzzle
    logpuzzle(args,plaintext,ciphertext,str(abet))
    
        
    
    
    
    
    
        
    
    
        
    
        
    
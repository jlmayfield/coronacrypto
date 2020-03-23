#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A set of monoalphabetic key generation functions

Created on Sun Mar 22 12:35:54 2020
@author: jlmayfield4
"""

import string
import random

def issequence(candidate):
    """
    Check a given candidate to see if it's a sequence, i.e. if it is a permuation
    of ascii_uppercase or ascii_lowercase'

    Parameters
    ----------
    candidate : string
        potential sequence

    Returns
    -------
    True if candidate is a valid sequence.

    """
    return set(list(string.ascii_uppercase)) == set(list(candidate.upper()))
    

def rand():
    """
    Produce a random sequence

    Returns
    -------
    A random, uppercase sequence

    """
    seq = list(string.ascii_uppercase)
    random.shuffle(seq)
    return ''.join(seq)


def shift(steps=0,seq=string.ascii_uppercase):
    """
    Shift a sequence steps places. Postive values move 'A' right where negative
    move it left. By default this does a ceasar shift, i.e. it works on the
    standard sequnce. It can also take an arbitrary sequence and shift it.

    Parameters
    ----------
    steps : Integer
        Number of places to move the first letter in the sequence
    seq : String, optional
        A sequence to be shifted. The default is string.ascii_uppercase.

    Returns
    -------
    String, a shifted sequence

    """
    if steps > 0:
        return seq[-steps:] + seq[0:len(seq)-steps]
    elif steps < 0:
        return seq[-steps:] + seq[0:-steps]
    else: 
        return seq

def keyword(key):
    """
    Compute a keyword/keyphrase based ciphertext sequence. 

    Parameters
    ----------
    key : string
        the desired keyword or keyphrase 

    Returns
    -------
    Keyword-based sequence 

    """
    key_lst = [l for w in [list(w) for w in key.upper().split()] for l in w]
    key_set = set(key_lst)
    diff = [s for s in string.ascii_uppercase if s not in key_set]
    key_nodupe = []
    for k in key_lst:
        if k not in key_nodupe:
            key_nodupe.append(k)    
    return ''.join(key_nodupe + diff)

        
def reverse(seq=string.ascii_uppercase):
    """
    Reverse a given sequence

    Parameters
    ----------
    seq : string
        sequence to be reversed

    Returns
    -------
    reverse of seq

    """
    return seq[len(seq)::-1]




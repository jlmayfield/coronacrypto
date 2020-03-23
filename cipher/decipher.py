#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:37:50 2020

@author: jlmayfield4
"""

import string
import cipher.monoalphabets

def decipher(ciphertext,alphabet):
    """
    Do a text decipherment of the given ciphertext using the given alphabet

    Parameters
    ----------
    ciphertext : str
        ciphertext
    alphabet : MonoAlphabet
        candidate key

    Returns
    -------
    str
    The result of deciphering ciphertext using alphabet as the key

    """
    decipher_key = alphabet.fordecipher()
    groups = [decipher_key[c] for g in ciphertext.split() for c in g]
    plain = ''.join(groups)    
    p_groups = [plain[i:i+30] for i in range(0,len(plain),30)]
    return '\n'.join(p_groups)
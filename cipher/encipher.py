#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:24:11 2020

@author: jlmayfield4
"""

import string

def encipher(plaintext, alphabet, pad='Z', l_group=5, r_group=10):
    """
    Encipher the given plaintext using the given alphabet. Pad characters
    and grouping values can also be provided.
    Parameters
    ----------
    plaintext : str
        Plaintext message
    alphabet : MonoAlphabet
        key
    pad : str, optional
        letter used for padding. The default is 'Z'.
    l_group : int, optional
        size of letter group. The default is 5.
    r_group : int, optional
        size of row groups. The default is 5.
    Returns
    -------
    string
        ciphertext
    """
    cleaned = ''.join([l for l in plaintext.lower() if l in string.ascii_lowercase])
    cipherbet = alphabet.forencipher()
    ciphertext = ''.join([cipherbet[p] for p in cleaned]).upper()
    ciphertext += (pad * ((l_group - len(ciphertext)%l_group) % l_group))
    groups = [ciphertext[i:i+l_group] for i in range(0, len(ciphertext), l_group)]
    rows = [groups[i:i+r_group] for i in range(0, len(groups), r_group)]
    return '\n\n'.join([' '.join(r) for r in rows])
        
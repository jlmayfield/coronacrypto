#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:00:43 2020

@author: jlmayfield4
"""

import string

class MonoAlphabet:
    
    def __init__(self,cipher,plain=string.ascii_lowercase):
        """
        Construct a monoalphabetic substitution key. Cipher sequences are 
        always maintained in uppercase where plaintext sequences are maintained
        in lowercase. 

        Parameters
        ----------
        cipher : string
            ciphertext sequence. 
        plain : string, optional
            plaintext sequence. The default is string.ascii_lowercase.

        Returns
        -------
        None.

        """        
        self.cipher = cipher.upper()
        self.plain = plain.lower()
    
    def __str__(self):
        """
        Give string representation of the key

        Returns
        -------
        string
            lists p: plain-sequence followed by c: cipher-sequence

        """
        return "p: " + self.plain + '\nc: ' + self.cipher + '\n'
    
    def forencipher(self):
        """
        Produces a python dictionary suitable for encipherment using the key

        Returns
        -------
        dict
            encipherment dictionary

        """
        return {self.plain[i]:self.cipher[i] for i in range(26)}
    
    def fordecipher(self):
        """
        Produces a python dictionary suitable for decipherment using the key

        Returns
        -------
        dict
            decipherment dictionary

        """
        return {self.cipher[i]:self.plain[i] for i in range(26)}
        
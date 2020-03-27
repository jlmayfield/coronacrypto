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
    cli_parser = argparse.ArgumentParser(description='Build a CoronaCrypto Puzzle.')
    cli_parser.add_argument('fname', nargs=1,
                            help='Name of file containing plaintext source')
    cli_parser.add_argument('vnum', nargs=1,
                            help='Puzzle Series (S) Number (N) designator as "S.N"')
    cli_parser.add_argument('-s', type=int, default=0,
                            help='Shift amount for the cipher sequence')
    cli_parser.add_argument('-k', type=str, default='',
                            help='Keyword or keyphrase for the cipher sequence')
    cli_parser.add_argument('-r',
                            help='Include if the cipher sequence should be reversed.')
    return cli_parser

def logkeygen(log, cli_args):
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
    if cli_args['k'] != '':
        log.write('Keyword: ' + cli_args['k'] + '\n')
    if cli_args['s'] != 0:
        log.write('Shift: {0}\n'.format(cli_args['s']))
    if cli_args['r']:
        log.write('Reversed\n')

def logpuzzle(cli_args, plain, cipher, key):
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
        srcpath = os.path.split(os.path.abspath(cli_args['fname'][0]))
        filename = 'cc-' + cli_args['vnum'][0] + '-' + timestamp + '.txt'
        log = open(srcpath+'/'+filename, 'w')
        # file for saving ciphertext only
        ctext = open(srcpath + '/' + 'c' + cli_args['vnum'][0] + '.txt', 'w')
    except OSError:
        sys.exit('Cannot open log for writting buddy.')
    # log header info
    log.write('Coronacrypto Puzzle\n------------------\n')
    log.write('Series-Puzzle Number: ' + cli_args['vnum'][0] + '\n')
    log.write('Created: ' + now.strftime("%Y-%m-%d %H:%M:%S"))
    log.write('\n\n')
    # log plaintext
    log.write("Plaintext\n---------\n")
    log.write(plain)
    log.write('\n')
    # log details of the key
    log.write('Key\n---\n')
    logkeygen(log, cli_args)
    log.write(key)
    log.write('\n')
    # log ciphertext
    log.write('Ciphertext\n----------\n')
    log.write('\n')
    log.write(cipher)
    ctext.write(cipher)

def main():
    """
    Runs ccpuzzler app
    Returns
    -------
    None.
    """
    parser = buildparser()
    args = vars(parser.parse_args())
    # open the file, or not
    try:
        plain_path = os.path.abspath(args['fname'][0])
        plain_file = open(plain_path, 'r')
    except OSError:
        sys.exit('That is not a file buddy.')
    # cipher seq Order Of Ops: keyword, shift, reverse
    c_seq = string.ascii_uppercase
    if args['k']:
        c_seq = ms.keyword(args['k'])
    if args['s']:
        c_seq = ms.shift(args['s'], c_seq)
    if args['r']:
        c_seq = ms.reverse(c_seq)
    # get that alphabet
    abet = MonoAlphabet(c_seq)
    # and the encipher dictionary
    plaintext = plain_file.read()
    # let's do this
    ciphertext = encipher(plaintext, abet)
    #log the puzzle
    logpuzzle(args, plaintext, ciphertext, str(abet))

if __name__ == '__main__':
    main()
    
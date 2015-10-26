# coding: UTF-8
import hashlib
import binascii
import struct
from hashlib import sha256
# from block import *

# 58 character alphabet used
alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

if bytes == str:  # python2
    iseq = lambda s: map(ord, s)
    bseq = lambda s: ''.join(map(chr, s))
    buffer = lambda s: s
else:  # python3
    iseq = lambda s: s
    bseq = bytes
    buffer = lambda s: s.buffer


def b58encode(v):
    '''Encode a string using Base58'''

    origlen = len(v)
    v = v.lstrip(b'\0')
    newlen = len(v)

    p, acc = 1, 0
    for c in iseq(v[::-1]):
        acc += p * c
        p = p << 8

    result = ''
    while acc > 0:
        acc, mod = divmod(acc, 58)
        result += alphabet[mod]

    return (result + alphabet[0] * (origlen - newlen))[::-1]


def b58decode(v):
    '''Decode a Base58 encoded string'''

    if not isinstance(v, str):
        v = v.decode('ascii')

    origlen = len(v)
    v = v.lstrip(alphabet[0])
    newlen = len(v)

    p, acc = 1, 0
    for c in v[::-1]:
        acc += p * alphabet.index(c)
        p *= 58

    result = []
    while acc > 0:
        acc, mod = divmod(acc, 256)
        result.append(mod)
    return (bseq(result) + b'\0' * (origlen - newlen))[::-1]

def in_address(in_pubkey):
    in_pubkey_hash256 = hashlib.sha256(in_pubkey.decode('hex')).hexdigest()
    in_pubkey_hash160 = hashlib.new('ripemd160',in_pubkey_hash256.decode('hex')).hexdigest()
    in_verandpubkey_hash160 = "00"+in_pubkey_hash160
    in_verandpubkey_hash160_hash256 = hashlib.sha256(in_verandpubkey_hash160.decode('hex')).hexdigest()
    in_verandpubkey_hash160_hash256_2 = hashlib.sha256(in_verandpubkey_hash160_hash256.decode('hex')).hexdigest()
    in_subaddress = "00"+in_pubkey_hash160+in_verandpubkey_hash160_hash256_2[:8]
    return b58encode(in_subaddress.decode('hex'))
#from inputs script publickey to address



def out_address_25(out_pubkey_hash160):
    out_verandpubkey_hash160 = "00"+out_pubkey_hash160
    out_verandpubkey_hash160_hash256 = hashlib.sha256(out_verandpubkey_hash160.decode('hex')).hexdigest()
    out_verandpubkey_hash160_hash256_2 = hashlib.sha256(out_verandpubkey_hash160_hash256.decode('hex')).hexdigest()
    out_subaddress = "00"+out_pubkey_hash160+out_verandpubkey_hash160_hash256_2[:8]
    out_address =  b58encode(out_subaddress.decode('hex'))
    return out_address
#from outputs script pubkey_hash160 to address


def out_address_67(out_pubkey):
    out_pubkey_hash256 = hashlib.sha256(out_pubkey.decode('hex')).hexdigest()
    out_pubkey_hash160 = hashlib.new('ripemd160',out_pubkey_hash256.decode('hex')).hexdigest()
    out_verandpubkey_hash160 = "00"+out_pubkey_hash160
    out_verandpubkey_hash160_hash256 = hashlib.sha256(out_verandpubkey_hash160.decode('hex')).hexdigest()
    out_verandpubkey_hash160_hash256_2 = hashlib.sha256(out_verandpubkey_hash160_hash256.decode('hex')).hexdigest()
    out_subaddress = "00"+out_pubkey_hash160+out_verandpubkey_hash160_hash256_2[:8]
    return b58encode(out_subaddress.decode('hex'))

# aaa = '044e8a583c892a4524285f13bd02be1305f8c8f70392ef32d3d4c01bf6dfdd742b5923eefae7a4e6e1e27258450bab0234961a213f91fe1ba6ff51f22fdbb93ed9'
# print in_address(aaa)

# bbb = '0489171e2c2cee1e63321fca1caa4e89cae95898ca808e788fd845dd6dd9e7d3e851a3a49dc8bbab18b95668a8690fb2b9954f0d90921dc23b853405d8b9190069'
# print in_address(bbb)

# ccc = '338320deedb51e631961874817645987b60c225f'
# # print out_address(ccc)

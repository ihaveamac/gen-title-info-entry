#!/usr/bin/env python3

# This file is a part of gen-title-info-entry.
#
# Copyright (c) 2019 Ian Burgwin
# This file is licensed under The MIT License (MIT).
# You can find the full license text in LICENSE.md in the root of this project.

# This script is really lazy because I am really lazy. I might make this better eventually.

import argparse
import random

parser = argparse.ArgumentParser(description='Generate Title Info Entry.')
parser.add_argument('-o', '--output', help='output filename', type=argparse.FileType('wb'), required=True)
parser.add_argument('-v', '--version', help='title version', type=int, required=True)
parser.add_argument('-m', '--has-manual', help='has manual', action='store_true')
parser.add_argument('-t', '--tmd-id', help='tmd content id as hexstring', required=True)
parser.add_argument('-c', '--cmd-id', help='cmd content id as hexstring', required=True)
parser.add_argument('-s', '--has-save', help='has SD save data', action='store_true')
parser.add_argument('-e', '--extdata-id', help='extdataid low as hexstring', required=True)
parser.add_argument('-p', '--product-code', help='product code', required=True)

a = parser.parse_args()

data = [
    # title size, putting 0 for now
    (0).to_bytes(8, 'little'),
    # title type, assuming 0x40 as it usually is
    0x40.to_bytes(4, 'little'),
    # title version
    a.version.to_bytes(4, 'little'),
    # flags_0, only checking electronic manual
    (1 if a.has_manual else 0).to_bytes(4, 'little'),
    # tmd content id
    bytes.fromhex(a.tmd_id.rjust(8, '0'))[::-1],
    # cmd content id
    bytes.fromhex(a.cmd_id.rjust(8, '0'))[::-1],
    # flags_1, only checking save data
    (1 if a.has_save else 0).to_bytes(4, 'little'),
    # extdataid low
    bytes.fromhex(a.extdata_id.rjust(8, '0'))[::-1],
    # reserved
    b'\0' * 4,
    # flags_2, only using a common value
    0x100000000.to_bytes(8, 'little'),
    # product code
    a.product_code.encode('ascii').ljust(0x10, b'\0'),
    # reserved
    b'\0' * 0x10,
    # unknown
    random.randint(0, 0xFFFFFFFF).to_bytes(4, 'little'),
    # reserved
    b'\0' * 0x2c
]

result = b''.join(data)
a.output.write(result)
a.output.close()

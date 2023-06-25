#!/usr/bin/env python3

from hashlib import sha256
import string

strings = """252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111
acac86c0e609ca906f632b0e2dacccb2b77d22b0621f20ebece1a4835b93f6f0
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
cd0aa9856147b6c5b4ff2b7dfee5da20aa38253099ef1b4a64aced233c9afe29
021fb596db81e6d02bf3d2586ee3981fe519f275c0ac9ca76bbcf2ebb4097d96
62c66a7a5dd70c3146618063c344e531e6d4b59e379808443ce962b3abd63c5a
3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea
cd0aa9856147b6c5b4ff2b7dfee5da20aa38253099ef1b4a64aced233c9afe29
acac86c0e609ca906f632b0e2dacccb2b77d22b0621f20ebece1a4835b93f6f0
de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7
65c74c15a686187bb6bbf9958f494fc6b80068034a659a9ad44991b08c58f2d2
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6
043a718774c572bd8a25adbeb1bfcd5c0256ae11cecf9f9c3f925d0e52beaf89
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
454349e422f05297191ead13e21d3db520e5abef52055e4964b82fb213f593a1
3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
0bfe935e70c321c7ca3afc75ce0d0ca2f98b5422e008bb31c00c6d7f1f1c0ad6
e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
acac86c0e609ca906f632b0e2dacccb2b77d22b0621f20ebece1a4835b93f6f0
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111
acac86c0e609ca906f632b0e2dacccb2b77d22b0621f20ebece1a4835b93f6f0
ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb
cd0aa9856147b6c5b4ff2b7dfee5da20aa38253099ef1b4a64aced233c9afe29
d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2""".split("\n")

d = {}

for i in string.printable:
    h = sha256()
    h.update(i.encode())
    d[h.digest().hex()] = i

for i in strings:
    print(d[i], end="")

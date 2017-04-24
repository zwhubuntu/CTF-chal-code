import os
import struct
from zlib import crc32

# PNG file format signature
pngsig = '\x89PNG\r\n\x1a\n'


def swap_palette(filename):
    # open in read+write mode
    with open(filename, 'r+b') as f:
        f.seek(0)
        # verify that we have a PNG file
        if f.read(len(pngsig)) != pngsig:
            raise RuntimeError('not a png file!')

        while True:
            chunkstr = f.read(8)
            if len(chunkstr) != 8:
                # end of file
                break

            # decode the chunk header
            length, chtype = struct.unpack('>L4s', chunkstr)
            # we only care about palette chunks
            if chtype == 'PLTE':
                curpos = f.tell()
                paldata = f.read(length)
                # change the 3rd palette entry to cyan
                paldata = paldata[:6] + '\x00\xff\xde' + paldata[9:]

                # go back and write the modified palette in-place
                f.seek(curpos)
                f.write(paldata)
                f.write(struct.pack('>L', crc32(chtype + paldata) & 0xffffffff))
            else:
                # skip over non-palette chunks
                f.seek(length + 4, os.SEEK_CUR)


if __name__ == '__main__':
    filename = 'f:/01.png'
    swap_palette(filename=filename)

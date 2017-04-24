'''
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) {
    if (argc != 3) {
        printf("USAGE: %s input_file output_file\n", argv[0]);
        return 0;
    }
    FILE* input_file  = fopen(argv[1], "rb");
    FILE* output_file = fopen(argv[2], "wb");
    if (!input_file || !output_file) {
        printf("Error\n");
        return 0;
    }
    char key[] = "XXXXXXXXXXXX";
    char p, t, c = 0;
    int i = 0;
    while ((p = fgetc(input_file)) != EOF) {
        c = ((key[i % strlen(key)] ^ t) + (p-t) + i*i ) & 0xff;
        t = p;
        i++;
        fputc(c, output_file);
    }
    return 0;
}

'''
import itertools
import string

p = open('f:/flag/plain.txt', 'rb')
plain = p.read()[0:30]
c = open('f:/flag/ciper.txt', 'rb')
ciper = c.read()[0:30]
lst = string.printable.strip()
key = ''
length = 6

for t in itertools.product(lst, repeat=length):
    key = ''.join(t)
    for i in xrange(len(plain)):
        c_text =

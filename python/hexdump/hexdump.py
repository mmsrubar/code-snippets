# get all printable chars and . (dot) for non-printable chars
HEX_FILTER = ''.join(
[(len(repr(chr(i))) == 3) and chr(i) or '.' for i in range(256)])

# Read a given string (src) and print its hexdump
def hexdump(src, length=16, show=True):
    if isinstance(src, bytes):
        src = src.decode()

    results = list()
    # read 16 chars of the string
    for i in range(0, len(src), length):
        word = str(src[i:i+length])

        # use transform table to get printable chars
        printable = word.translate(HEX_FILTER)
        # get hex representation of the entire word char by char
        hexa = ' '.join([f'{ord(c):02X}' for c in word])
        hexwidth = length*3
        # {i:04x} format number in var i as four digit hex with zeros from left
        results.append(f'{i:04x} {hexa:<{hexwidth}} {printable}')

    if show:
        for line in results:
            print(line)
    else:
        return results

hexdump('python rocks\n and proxies roll\n')

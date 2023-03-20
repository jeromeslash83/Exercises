def to_bcd(n):
    binary = ''
    negative = ''
    if n < 0:
        n = -n
        negative ='-'
        for n in str(n):
            binary = binary + bin(int(n))[2:].zfill(4) + ' '
        
    else:
        for n in str(n):
            #remove 0b and pad with 0s
            binary = binary + bin(int(n))[2:].zfill(4) + ' '
    return (negative + binary).strip()

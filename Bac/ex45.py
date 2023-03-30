def dec_to_bin(nb):
    q,r,=nb // 2, nb %2
    if q == 0 :
        return str(r)
    else:
        return dec_to_bin(q) + str(r)
    
print(dec_to_bin(10))

def bin_to_dec(nb) :
    if nb == '0' :
        return 0 
    elif nb == '1':
        return 1 
    else :
        if nb[-1] == "0":
            bit_d = 0
        else :
            bit_d = 1
        return 2 * bin_to_dec(nb[:-1]) + bit_d

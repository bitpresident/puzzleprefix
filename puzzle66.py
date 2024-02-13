try:
    import random
    from bitcoin import privtopub, encode_pubkey, pubtoaddr, decode_privkey

# If required imports are unavailable, we will attempt to install them!

except ImportError: 
    import subprocess
    subprocess.check_call(["python3", '-m', 'pip', 'install', 'bitcoin'])

while True:  
    low  = 0x20000000000000000
    high = 0x3ffffffffffffffff
    val = str ( hex ( random.randrange( low, high ) ) )[2:]
    result = val.rjust(48 + len(val), '0')
    priv = result
    pub = privtopub(decode_privkey(priv, 'hex'))
    pubkey1 = encode_pubkey(pub, "bin_compressed")
    addr = pubtoaddr(pubkey1)
    n = addr
    if n.startswith('13zb1hQbWV'):
        print ("FOUND!",addr,result)
        k1 = priv
        k2 = pub
        k3 = addr

        file = open('win.txt', 'a')
        file.write("Private key: " + str(k1) + '\n' + "Public key: " + str(k2) + '\n' + "Address: " + str(k3) + '\n\n')    
        file.close()
    else:
        print("Searching...", addr, result, end='\r')

import nbsp_python as nbsp

def enroll ():
    try:
        nbsp.initialize_handle()
        nbsp.open_device()
    except:
        pass

    handle = nbsp.capture("enroll", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    nbsp.terminate_handle()
    return fingerprint_hash

def match (hash_stored):
    handle = nbsp.capture("verify", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    if nbsp.match(hash_stored,fingerprint_hash):
        print('ok')
    else:
        print('not ok')

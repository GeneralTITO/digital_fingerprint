import nbsp_python as nbsp

def enroll ():
    try:
        nbsp.initialize_handle()
        nbsp.open_device()
    except:
        pass

    handle = nbsp.capture("enroll", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    print(fingerprint_hash)
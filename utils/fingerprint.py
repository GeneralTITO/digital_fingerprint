import nbsp_python as nbsp
from utils.handle_data import carregar_pessoas
from utils.verifications import save_verification

def enroll():
    try:
        nbsp.initialize_handle()
        nbsp.open_device()
    except:
        pass

    handle = nbsp.capture("enroll", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    nbsp.terminate_handle()
    return fingerprint_hash


def match(hash_stored):
    handle = nbsp.capture("verify", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    if nbsp.match(hash_stored, fingerprint_hash):
        return True
    else:
        return False


def verify():
    try:
        nbsp.initialize_handle()
        nbsp.open_device()
    except:
        pass

    handle = nbsp.capture("verify", 10000)
    fingerprint_hash = nbsp.extract_fir_text(handle)
    pessoas = carregar_pessoas()
    for pessoa in pessoas:
        if nbsp.match(pessoa[0], fingerprint_hash):
            nbsp.terminate_handle()
            save_verification(pessoa)
            return pessoa
    nbsp.terminate_handle()
    return "Digital não cadastrada"

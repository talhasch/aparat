import hashlib


def md5_checksum(s: str) -> str:
    return hashlib.md5(s.encode('utf-8')).hexdigest()

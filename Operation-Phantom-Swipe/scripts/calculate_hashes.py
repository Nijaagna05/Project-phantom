import hashlib
from pathlib import Path

FILES = [
    "evidence/skimmer/captured_data.csv",
    "evidence/skimmer/device_log.txt",
    "evidence/mobile/messages.txt",
    "evidence/mobile/gps_log.csv",
    "evidence/mobile/transactions.csv"
]


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def main():
    print("OPERATION PHANTOM SWIPE")
    print("SHA-256 HASH REPORT")
    print("=" * 60)

    for file_name in FILES:
        path = Path(file_name)

        if not path.exists():
            print(f"[ERROR] File not found: {file_name}")
            continue

        file_hash = calculate_sha256(path)

        print(f"\nFile: {file_name}")
        print(f"SHA-256: {file_hash}")


if __name__ == "__main__":
    main()
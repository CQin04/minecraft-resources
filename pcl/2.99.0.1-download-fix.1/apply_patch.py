"""Reproduce this exact PCL 2.99.0.1 binary repair using Python 3 only."""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path, help='Original unmodified PCL 2.99.0.1 EXE')
    parser.add_argument('output', type=Path, help='New output EXE; must not exist')
    args = parser.parse_args()
    report = json.loads(Path(__file__).with_name('patch-report.json').read_text(encoding='utf-8'))
    original = args.input.read_bytes()
    if hashlib.sha256(original).hexdigest() != report['original_sha256']:
        parser.error('Input SHA256 does not match the supported original PCL 2.99.0.1')
    patched = bytearray(original)
    for edit in report['edits']:
        offset = edit['file_offset']
        before, after = bytes.fromhex(edit['before']), bytes.fromhex(edit['after'])
        if len(before) != len(after) or original[offset:offset + len(before)] != before:
            parser.error('Unexpected original bytes: ' + edit['reason'])
        patched[offset:offset + len(after)] = after
    if len(patched) != report['size'] or hashlib.sha256(patched).hexdigest() != report['patched_sha256']:
        parser.error('Output verification failed; no output written')
    # Exclusive creation preserves both the original and any existing output file.
    with args.output.open('xb') as stream:
        stream.write(patched)
    print('Created:', args.output)
    print('SHA256:', report['patched_sha256'])


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Restore the complete models directory from the flat GitHub download files.

Uses only the Python standard library. Verifies the flat delivery first, extracts
all family ZIPs into one location, restores renamed 3MF files, then verifies every
original model file. Does not modify different existing files or run a slicer.
"""
from pathlib import Path, PurePosixPath
import argparse
import hashlib
import json
import zipfile

SOURCE = Path(__file__).resolve().parent


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_relative(value):
    relative = PurePosixPath(value)
    if relative.is_absolute() or '..' in relative.parts or '\\' in value:
        raise RuntimeError('Unsafe archive path: ' + value)
    return Path(*relative.parts)


def write_matching(target, data):
    if target.exists() and target.read_bytes() != data:
        raise RuntimeError('Refusing to replace a different existing file: ' + str(target))
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def restore(destination):
    delivery = json.loads((SOURCE / 'web-manifest.json').read_text(encoding='utf-8'))
    for entry in delivery['files']:
        path = SOURCE / safe_relative(entry['path'])
        data = path.read_bytes()
        if len(data) != entry['size'] or digest(data) != entry['sha256']:
            raise RuntimeError('Downloaded file does not match manifest: ' + str(path))
    mapping = json.loads((SOURCE / 'model-file-map.json').read_text(encoding='utf-8'))
    for name in mapping['archives']:
        with zipfile.ZipFile(SOURCE / name) as archive:
            for entry in archive.infolist():
                relative = safe_relative(entry.filename)
                if not relative.parts or relative.parts[0] != 'models' or entry.is_dir():
                    raise RuntimeError('Unexpected archive entry: ' + entry.filename)
                write_matching(destination / relative, archive.read(entry))
    for entry in mapping['direct_3mf']:
        data = (SOURCE / entry['public_name']).read_bytes()
        if digest(data) != entry['sha256']:
            raise RuntimeError('3MF checksum mismatch: ' + entry['public_name'])
        write_matching(destination / 'models' / safe_relative(entry['original_relative_path']), data)
    original = json.loads((SOURCE / 'models-manifest.json').read_text(encoding='utf-8'))
    for entry in original['files']:
        restored = destination / 'models' / safe_relative(entry['path'])
        data = restored.read_bytes()
        if len(data) != entry['size'] or digest(data) != entry['sha256']:
            raise RuntimeError('Restored model does not match original: ' + str(restored))
    if (destination / 'models/manifest.json').read_bytes() != (SOURCE / 'models-manifest.json').read_bytes():
        raise RuntimeError('Restored original manifest differs')
    print('Restored and verified %d original files: %s' % (len(original['files']) + 1, destination / 'models'))
    print('Open models/README.md. Optional STL extraction: python3 models/extract_stl.py')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=SOURCE, help='Destination containing the restored models directory')
    args = parser.parse_args()
    restore(args.output.resolve())


if __name__ == '__main__':
    main()

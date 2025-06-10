import sys

def usage():
    print("Usage: ccwc.py [-c] [-l] [-w] [-m] [FILE]")
    sys.exit(1)

def read_input(filename):
    if filename:
        with open(filename, 'rb') as f:
            data = f.read()
    else:
        data = sys.stdin.buffer.read()
    return data

def main():
    args = sys.argv[1:]
    flags = [a for a in args if a.startswith('-')]
    files = [a for a in args if not a.startswith('-')]

    # Validate command-line arguments
    for f in flags:
        if f not in ('-c', '-l', '-w', '-m'):
            usage()
    if len(files) > 1:
        usage()

    filename = files[0] if files else None
    data = read_input(filename)
    text = data.decode('utf-8', errors='replace')

    # Default behavior when no flags are provided
    if not flags:
        flags = ['-l', '-w', '-c']

    parts = []
    if '-l' in flags:
        parts.append(str(text.count('\n')))
    if '-w' in flags:
        parts.append(str(len(text.split())))
    if '-m' in flags:
        parts.append(str(len(text)))
    if '-c' in flags:
        parts.append(str(len(data)))

    output = "   ".join(parts)
    if filename:
        output += " " + filename
    print(output)

if __name__ == "__main__":
    main()

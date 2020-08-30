def count_lines(file):
    with open(file, 'r') as f:
        f.seek(0)
        return len(f.readlines())

def count_words(file):
    with open(file, 'r') as f:
        f.seek(0)
        return len(f.read().split())

def count_chars(file):
    with open(file, 'r') as f:
        f.seek(0)
        return len(f.read())

def test(file):
    return f'\t{count_lines(file)}\t\t{count_words(file)}\t\t{count_chars(file)} {file}'

# Testing of module, which will not run if module is imported to another program.
if __name__ == '__main__':
    print(count_lines('test_file.txt'))
    print(count_words('test_file.txt'))
    print(count_chars('test_file.txt'))
    print(test('test_file.txt'))
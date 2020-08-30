def read_verse(file_name):
    with open(file_name) as  f:
        for line in f:
            yield line.strip()

def mix_verses(lists):
    list_verses = lists
    my_array_iterators = []
    for num in  list_verses:
        my_array_iterators.append(read_verse(num))
    while  my_array_iterators:
        try:
            for itr in my_array_iterators:
                print(next(itr))
        except StopIteration:
            pass

def full_mix_verses(*args):
    list_verses = args
    mix_verses(list_verses)


def mix_verse(*args):
    all_verses = []
    for fname in args:
        itr = read_verse(fname)
        all_verses.append({'done': False, 'iter': itr})



a = read_verse('verse_1.txt')
b =  read_verse('verse_2.txt')
c = read_verse('verse_3.txt')

all_verses = [
    {'done': False, 'iter': a, },
    {'done': False, 'iter': b, },
    {'done': False, 'iter': c, },
]

def check_list(lst):
    for i in lst:
        if i['done']:
            True
    return False


while check_list(all_verses):
    for struct in enumerate(all_verses):
        if not struct['done']:
            try:
                line = next(struct['iter'])
                print(line)
            except:
                all_verses[pos]['done'] = True
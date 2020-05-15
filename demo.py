record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
# phone_numbers永远是列表，可能空
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


#
def do_bar(s):
    print('bar', s)


#
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
# 丢弃
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record

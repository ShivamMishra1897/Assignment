#Write a Python function to reverses a string if its length is a multiple of 4

def reverse(a):

    if len(a) % 4 ==0:
        return ''.join(reversed(a))
    return a

print(reverse('mathematics'))
print(reverse('poiuuytr'))
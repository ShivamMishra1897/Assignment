#Write a Python program to read last n lines of a file.
def l_line(new_file,n):
    with open(new_file) as file:
        for line in (new_file.readlines) [-n:]:
            print(line,end ='')

if __name__ == '__main__':
    fname = 'new_file'
    n = 3
    try:
        l_line(fname, N)
    except:
        print('File not found')
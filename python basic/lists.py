if __name__ == '__main__':
    N = int(input())
lists = []
for h in range(N):
    command = input().split()
    if command[0] != 'print':
        eval("lists.{}(".format(command[0]) + ',' .join(command[1:]) + ")")
    else:
        print(lists)
word = input()
for i in range(ord('a'), ord('z')+1):
    try:
        print(word.find(chr(i)), end=' ')
    except:
        print(-1, end=' ')
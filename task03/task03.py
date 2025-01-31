def main():
    ip = input("input:")    
    # len of input is at most 99
    if len(ip) > 99:
        ip = ip[:99]
    
    buffer = list(ip)

    for i in range(0, 20, 2):
        if i <len(buffer):
            buffer[i] = chr(ord(buffer[i]) - i)
    
    for j in range(1, 21, 2):
        if j <len(buffer):
            buffer[j] = chr(ord(buffer[j]) + j)

    op = ''.join(buffer)
    print(op)

if __name__ == "__main__":
    main()
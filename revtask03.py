def reverse_transformation(ip):
    buffer = list(ip)
    
    for i in range(0, 20, 2):
        if i < len(buffer):
            buffer[i] = chr(ord(buffer[i]) + i)  

    for j in range(1, 21, 2):
        if j < len(buffer):
            buffer[j] = chr(ord(buffer[j]) - j)  
    og = ''.join(buffer)
    
    return og

#m = ""
m = """WPUbutof1xJj+U%nVB"L"""
og = reverse_transformation(m)
print(og)

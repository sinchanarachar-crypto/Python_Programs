def write(): 
    String = input('Enter the paragraph: ') 
    file = open("C:/Users/Sunchana/OneDrive/Desktop/Coding Related Aspects/Python Programs/PLC ClassRoom CR002/Read and Write File.txt", "w")
    file.write(String) 
    file.close() 

def read(): 
    with open ("C:/Users/Sunchana/OneDrive/Desktop/Coding Related Aspects/Python Programs/PLC ClassRoom CR002/Read and Write File.txt") as file: 
        data = file.read() 
        file.close() 
    print('--------------------------------') 
    print('Original Content') 
    print('--------------------------------') 
    print(data) 
    print('--------------------------------') 
    print('Modified Content') 
    print('--------------------------------') 
    print(data.title()) 
    print('--------------------------------') 
write() 
read()
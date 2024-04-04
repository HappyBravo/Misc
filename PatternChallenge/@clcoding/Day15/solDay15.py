def generate_pattern(size, 
                     pattern_icon = '*', space_icon = ' '):
    size = size//2 + 1
    width = 2 * size - 1 
    pattern = ""
    
    # GENERATING UPPER PART 
    # IT'S BASICALLY AN INVERTED TRAINGLE LIKE PATTERN PROBLEM
    # BUT DO IT TWICE IN A LINE  
    for i in range(1, size):
        pattern += pattern_icon * i + \
                   space_icon * (width - 2 * i) + '*' * i + \
                   pattern_icon * (i-1) + \
                   space_icon * (width - 2 * i) + '*' * i + \
                   '\n'
        
    # GENERATE REMAINING LOWER PART         
    for i in range(size):
        pattern += '*'*(width*2 - 1) + '\n'
    
    return pattern

size = int(input("Enter the size of the pattern: "))
# size = 7
print(generate_pattern(size))


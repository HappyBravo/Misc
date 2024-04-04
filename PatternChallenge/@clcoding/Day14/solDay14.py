def generate_square_pattern_without_base(amplitude, width,
                                         pattern_icon = '* ', space_icon = '  '):
    pattern = ""
    _half_width = width//2
 
    for i in range(amplitude):
        isLast = int(i == amplitude-1)

        if i == 0 :
            pattern += space_icon*(_half_width-2) + \
                       pattern_icon * (_half_width+1) +\
                       space_icon*(_half_width-2) + \
                       "\n"
        else:
            pattern += space_icon*((_half_width-2)*(1-isLast)) + \
                       pattern_icon * (1 + (_half_width-2)*(isLast)) + \
                       space_icon * (_half_width-1) + \
                       pattern_icon * (1 + (_half_width-2)*(isLast)) + \
                       space_icon*((_half_width-2)*(1-isLast)) + \
                       "\n"
    
    return pattern


if __name__ == "__main__":
    amplitude = int(input("Enter Amplitude of wave : "))
    width = int(input("Enter Width of wave : "))
    tot_wave = int(input("Enter Total number of wave : "))

    # amplitude = 4
    # width = 6
    # tot_wave = 3

    print("\n".join(
                [line*tot_wave 
                    for line in generate_square_pattern_without_base(amplitude, width).splitlines()]
                ))

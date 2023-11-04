def split_srt(input_file, part1_start, part1_end, part2_start, part2_end):
    part1_srt = []
    part2_srt = []
    current_srt = part1_srt  # Start with part 1

    with open(input_file, 'rb') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.decode('utf-8').strip()
        if line.isdigit():
            current_srt.append(line)  # Add the subtitle index
        elif '-->' in line:
            start, end = line.split('-->')
            start = start.strip()
            if part1_start <= start <= part1_end:
                current_srt.append(line)  # Add the subtitle timecode
            elif part2_start <= start <= part2_end:
                current_srt = part2_srt  # Switch to part 2
                current_srt.append(line)  # Add the subtitle timecode
            else:
                break
        elif line:  # Add the subtitle text
            current_srt.append(line)

    with open('part1.srt', 'wb') as f:
        f.write('\n'.join(part1_srt).encode('utf-8'))

    with open('part2.srt', 'wb') as f:
        f.write('\n'.join(part2_srt).encode('utf-8'))

if __name__ == "__main__":
    input_file = input("Enter the path to the original SRT file: ")
    part1_start = input("Enter the starting timestamp for part 1 (e.g., 00:00:00,000): ")
    part1_end = input("Enter the ending timestamp for part 1 (e.g., 00:10:00,000): ")
    part2_start = input("Enter the starting timestamp for part 2 (e.g., 00:10:00,000): ")
    part2_end = input("Enter the ending timestamp for part 2 (e.g., 00:20:00,000): ")

    split_srt(input_file, part1_start, part1_end, part2_start, part2_end)
    print("SRT file split into two parts.")

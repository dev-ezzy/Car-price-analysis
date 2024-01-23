# def num_to_bin(num):
#     #convert number to binary
#     binary_num = bin(int(num))
#     #removing the 1
#     gap_binary = binary_num[2:].split("1")
#     #setting gap from 0
#     longest_gap = 0
#     for gap in gap_binary:
#         if len(gap) > longest_gap:
#             print(f"{gap} is the longest gap")
#         else:
#             print("0")
        
# num_to_bin(529)


def num_to_binary(Num):
    binary = bin(Num)
    # Split binary representation by '1' to get a list of binary gaps and omitting "Ob"
    binary_gaps = binary[2:].split('1')
    
    binary_gaps = [g for g in binary_gaps if g]
    # If no binary gaps are found, return 0
    if not binary_gaps:
        return 0
    #longest binary gap
    longest_gap = max(len(g) for g in binary_gaps)
    return longest_gap


print(num_to_binary(529)) 



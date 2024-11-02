# Quinten Reed
# U3L3
# MergeSort

from math import ceil

def merge_sort(num_list):
    if len(num_list) > 2:
        #print(f"A\t{num_list[:ceil(len(num_list)/2)]}\t{num_list[ceil(len(num_list)/2):]}")
        left_list = merge_sort(num_list[:ceil(len(num_list)/2)])
        right_list = merge_sort(num_list[ceil(len(num_list)/2):])
        #print(f"A.1\t{left_list}\t{right_list}")

        # I'm not certain of this
        for item in right_list:
            jndex = 0
            sorted_flag = False

            while sorted_flag == False:
                if jndex >= len(left_list):
                    left_list.append(item)
                    sorted_flag = True
                    #print(f"D\t{left_list}\t{item}\t{jndex}\t{right_list}")

                elif item > left_list[jndex]:
                    jndex += 1
                    #print(f"E\t{left_list}\t{item}\t{jndex}\t{right_list}")

                elif item <= left_list[jndex]:
                    left_list.insert(jndex, item)
                    sorted_flag = True
                    #print(f"F\t{left_list}\t{item}\t{jndex}\t{right_list}")

        #print(f"G\t{left_list}")
        return left_list

    elif len(num_list) == 2:
        #print(f"B\t{num_list}")
        new_list = [-1, -1]

        if num_list[0] > num_list[1]:
            new_list[0] = num_list[1]
            new_list[1] = num_list[0]
        else:
            new_list[0] = num_list[0]
            new_list[1] = num_list[1]

        #print(f"C\t{new_list}\t{num_list}")
        return new_list

    elif len(num_list) == 1:
        return num_list

def main():
    nums1 = [6,2,5,8,3,4,8]
    nums2 = [1,2,3,4,5,6,7,8]
    nums3 = [8,2,6,0,1,3]

    for num_list in [nums1, nums2, nums3]:
        print(f"\nOriginal: {num_list}")
        new = merge_sort(num_list)
        print(f"Sorted: {new}\n")

if __name__ == "__main__":
    main()


# def simple_bubble(unsorted):
#     """***Thought process***
#     - We compare two pairs of the elements in the list switching them if the first is greatr than the 2nd pair
#     - we therefore run through the list until we reach the second last element since there is no more pairs
#     - we initialize a sorted variable to false. this will help break out od the loop in case we have a fully sorted list
#     - we will use while loop to until the sorted is true
#     - in the while loop, we immediatly set sorted to true by default
#     - then create a for loop through the list, them compare elements at index and index+1
#     - if they need swaping, we do the swap, set sorted to false and continue in the loop
#     - If there are no more swaps needed, we set sorted to true and exit the will loop
#     - return the list

#     """
#     i_length = len(unsorted) - 1
#     is_sorted = False
#     while is_sorted == False:
#         is_sorted = True
#         for i in range(0, i_length):
#             if unsorted[i] > unsorted[i+1]:
#                 is_sorted = False
#                 unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
#     return unsorted
                    



# def students_list( scores, student_ids):

#     """Thought process 
#     We map student ids against  their corresponding scores
#     We come up with a dictionary where each id has a list of scores
#     we iterate the dictionary items and sort the values indipendently
#     we later join the sorted lists returned by the bubble sort


#     """

#     list_dict = {}
#     for student_id, score in zip(student_ids, scores):
#         if student_id in list_dict:
#             list_dict[student_id].append(score)
#         else:
#             list_dict[student_id] = [score]
 

#     sorted_list = []
#     for key, value in list_dict.items():
#         sorted_list.extend(simple_bubble(value))

    
    
#     return print(sorted_list)

            
                
# ### TESTING 

# # unsorted =  [1,3,7,4,8,10,2,2,1]
# # simple_bubble(unsorted=unsorted)
# scores = [50, 40, 60, 30, 70, 20]
# student_ids = [1, 1, 1, 2, 2, 2]
# students_list(scores=scores, student_ids=student_ids)



# """
# A function to do bubble sort takes in a list/array of integers to be sorted(or whatever)
# iterates on the list
# the iteration is supposed to stop at the second last element, since we are picking pairs. 
# We pick a pair on each iteration, compare the two elements and rearrange them

# """

# def bubbleSort(lst: list):
#     current_index = 1

#     for i in range((len(lst) - 1)):
#         pass


def palindrome(num:list | str):
    if num[::-1] == num:
        print("Yes")
    else:
        print("no")
    
    
pal = palindrome([333])

## with two pointers technique

def twoPointerPal(num):
    left = 0
    right = len(num)-1

    for i in range(len(num)):
        if num[left] != num[right]:
            return False
        right -=1
        left +=1
    return True
        
print(twoPointerPal("racecar"))
    
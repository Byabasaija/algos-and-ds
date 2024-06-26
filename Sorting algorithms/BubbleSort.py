

def simple_bubble(unsorted):
    """***Thought process***
    - We compare two pairs of the elements in the list switching them if the first is greatr than the 2nd pair
    - we therefore run through the list until we reach the second last element since there is no more pairs
    - we initialize a sorted variable to false. this will help break out od the loop in case we have a fully sorted list
    - we will use while loop to until the sorted is true
    - in the while loop, we immediatly set sorted to true by default
    - then create a for loop through the list, them compare elements at index and index+1
    - if they need swaping, we do the swap, set sorted to false and continue in the loop
    - If there are no more swaps needed, we set sorted to true and exit the will loop
    - return the list

    """
    i_length = len(unsorted) - 1
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(0, i_length):
            if unsorted[i] > unsorted[i+1]:
                is_sorted = False
                unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
    return print(unsorted)
                    



def students_list(self, scores, student_ids):

    """Thought process 
    we have a list of students scores
    We have a list of student ids which sort of like group the scores
    for each score, we look at the group it falls into(the student id, ) if the group is the same, we go ahead and sort 


    """
    pass
    # current_id = 0
    # for id in student_ids:
    #     while current_id == id:
    #          i = 0
    #          for score in scores:
    #              if score[i]> score[i+1]:
                         

unsorted =  [1,3,7,4,8,10,2,2,1]
simple_bubble(unsorted=unsorted)
'''
divvier3b, Snapshot1

'Divvier' series objective: Split a collection of numbers (which may 
include replicates) in two, as evenly as possible.

divvier3 approach: Using iterative superset generation approach to make a 
collection of subcollections from which to choose closest-summing pair. 
It will, however, have replicate subcollections, but though 
inefficient, it does allow a deterministic split for the 'Divvier' problem, 
to replace the original tool which used random sampling to process
larger arrays, so could not guarentee an optimal split.

divvier3b: This new version modifies divvier3 Snapshot15 by reverting to my  
original multi-line snippet from its Snapshot1 for making the subcollections 
so that I can do the checks for perfect split and exit early if found, 
without making the whole subcollections list first. 
Also keeps track of subcollection representing best-split-so-far as I go,
so that even if the whole thing is made, it does not have to be traversed again. 

TODO: 
- Tidy up, restore GUI use.
- Attempt some comparisons of run speed for various inputs with divvier3.
- (Maybe add a Clear button to GUI.)
- Make an executable.
'''

import re

# If using CLI/IDE
def divvy(nums: list[float]) -> str: 

# If using GUI
# def divvy(): 
#     text = input_field.get("1.0",'end').strip() 
#     output_field.configure(state='normal') # Note1a
#     output_field.delete('1.0', END) # clear any existing output
#     try:
#         nums: list[float] = [float(x) for x in re.split(r"[,\s]+", text)]
#     except ValueError: 
#         output_field.insert("end", 'Invalid input - please enter only numbers\n'
#         '(separated only by whitespace and/or commas)')

    if len(nums) < 2: 
        return 'Input lists smaller than 2 numbers are not relevant.\n'

    subcolls: list[list[float]] = [[]]

    total = sum(nums)
    half = total / 2
    min_offset = float('inf') # minimum offset from half 
    firsthit: list[float] = []
    firsthit_sum = 0

    for num in nums:
        new = [sublist[:] for sublist in subcolls]
        for i in range(len(new)):
            new[i].append(num)
            subcoll = new[i]
            subcoll_sum = sum(subcoll)

            offset = abs(subcoll_sum - half)
            if not offset: # it is 0, cannot get better, so short-circuit
                firsthit = subcoll
                firsthit_sum = subcoll_sum
                break
            elif offset < min_offset: # better than previous, update best
                firsthit = subcoll
                firsthit_sum = subcoll_sum
                min_offset = offset

        subcolls.extend(new)


    # for num in nums:
    #     subcolls += [subcoll + [num] for subcoll in subcolls]
    # # Discard first (empty) item and complement (full input); Note2
    # subcolls = subcolls[1 : len(subcolls) - 1]
    # # print('subcolls', subcolls) # temp check

    # subcoll_sums = []
    # for subcoll in subcolls:
    #     subcoll_sums.append(sum(subcoll))
    # # print('subcoll_sums', subcoll_sums) # temp check

    # total = sum(nums)
    # half = total / 2
    # # print('total', total, '  half', half) # temp check

    # min_offset = float('inf') # minimum offset from half 

    # # ioffm = 0 # index of (first found) minimum offset (from half); Note3
    # for i, subcoll_sum in enumerate(subcoll_sums):
    #     offset = abs(subcoll_sum - half)
    #     if not offset: # it is 0, cannot get better, so short-circuit
    #         ioffm = i
    #         break 
    #     elif offset < min_offset:
    #         ioffm = i
    #         min_offset = offset 
    # # print('min_offset is', min_offset, 'for subcoll', subcolls[ioffm])

    # firsthit = subcolls[ioffm] # --added for transition to new code

    complement = nums.copy() # Note4
    for e in firsthit: # Note5
        complement.remove(e)
    sum_complement = sum(complement)
 
    # report = ('Smallest difference found: ' + str(abs(subcoll_sums[ioffm] - sum(complement))) + '\n' +
    # 'between subcollection ' + str(firsthit) + '\n' +
    # '(totalling ' + str(subcoll_sums[ioffm])  + ')\n' +
    # 'and complement        ' + str(complement) + '\n' 
    # '(totalling ' + str(sum(complement))  + ')\n' +
    # '(Other combinations may exist.)\n')

    report = ('Smallest difference found: ' + str(abs(firsthit_sum - sum_complement)) + '\n' +
    'between subcollection ' + str(firsthit) + '\n' +
    '(totalling ' + str(firsthit_sum)  + ')\n' +
    'and complement        ' + str(complement) + '\n' 
    '(totalling ' + str(sum_complement)  + ')\n' +
    '(Other combinations may exist.)\n')

    # If using CLI/IDE
    return report

    # If using GUI
    # output_field.insert("end", report)
    # output_field.configure(state='disabled') # optional, Note1b

'''
Note1a: Needed to reset between runs if using 'disabled' (Note1b)   
at end of function to prevent output being manually edited.
Note2: This would need to be removed if single-element inputs 
are possible, and the handling of these with an 'error message'
were not present at the beginning of the function.
Note3: ...Conversely, this would need to be put back.
Note4: Making copy in case we need to avoid modifying the input list.
Shallow copy is sufficient as elements are primitives.
Note5: This is of course time-inefficient.
'''


# Some tests, with smallest difference noted 
print(divvy([])) # Input lists smaller than 2 numbers are not relevant.
print(divvy([1])) # Input lists smaller than 2 numbers are not relevant.
print(divvy([3,3,7,5,9])) # 1 
print(divvy([1,2,3])) # 0
print(divvy([1,2])) # 1 
print(divvy([1,2,1,2])) # 0 
print(divvy([78, 93, 44, 27, 58, 25, 27, 73, 55, 32])) # 0 
print(divvy([880, 953, 229, 77, 96, 37, 7, 30, 18, 2])) # 1 
print(divvy([378, 222, 1, 83, 704, 6, 129, 455, 22, 97])) # 5
print(divvy([378, 222, 1, 83, 704, 378, 222, 1, 83, 704])) # 0
print(divvy([378, 222, 1, 83, 704, 378, 222, 1, 83, 704, 378, 222, 1, 83, 704])) # 10
print(divvy([1.5,2.5,0.5,4.5])) # 0.0
print(divvy([1,-2,-1,2])) # 0 


# GUI...

# from tkinter import *
# from tkinter.scrolledtext import ScrolledText
# root_widget = Tk()
# root_widget.title("divvier3 splits a collection of numbers in two as evenly as possible")
# root_widget.geometry("690x570") # provisional width, height GUI

# Label(root_widget, text = 'Enter list of numbers separated by commas and/or whitespace').grid(row=0, column=0) 

# input_field = ScrolledText(root_widget, width = 80, fg = 'blue', font=("Courier", 10), height=15) 
# input_field.grid(row=1, column=0, padx=15) 

# output = StringVar()

# submit_button = Button(root_widget, text = 'Submit', command = lambda: divvy(), bg='#C8C8C8')
# submit_button.grid(row=2, column=0)

# output_field = ScrolledText(root_widget, width = 80, fg = 'blue', font=("Courier", 10), height=15) 
# output_field.grid(row=3, column=0) 

# root_widget.mainloop()
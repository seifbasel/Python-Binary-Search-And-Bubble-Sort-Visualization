from tkinter import *
import time

# bubble sort algorithm
def bubble(list, drawData, timer):

    # length of elements
    n = len(list)

    # compare every two elements
    for i in range(n):
        for j in range(0, n-i-1):

            # swap if not sorted (left>right)
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

                # if swapped then color becomes Green else stays Red
                drawData(list, ['Green' if x == j +
                         1 else 'Red' for x in range(len(list))])
                time.sleep(timer)

            # calculate execution time
            end_time = time.time()
            complete_time = round(end_time-start_time)
            # third row is to display execution time
            Label(Mainframe, text=f"time to excute {complete_time} sec", bg='white').grid(
                row=2, column=1, padx=5, pady=5, sticky=W)

    # sorted elements assigned with Green color
    drawData(list, ['Blue' for x in range(len(list))])


# initialize root class for Tkinter
root = Tk()
# window name
root.title("Bubble Sort Visualizer")

# window size,color
root.maxsize(900, 600)
root.config(bg="Black")
select_alg = StringVar()
list = []

# function to generate the data values by accepting a given range
def generate():
    # list to be sorted
    global list
    list = [1, 69, 2, 36, 3, 78, 4, 33, 5, 61, 6, 44, 7]
    drawData(list, ['Red' for x in range(len(list))])

start_time = time.time()

# function to create the data bars and add their characteristics
def drawData(list, colorlist):
    canvas.delete("all")
    can_height = 380
    can_width = 550
    x_width = can_width/(len(list) + 1)
    offset = 30
    spacing = 10
    # optimize data for rescalling real-valued numeric data within
    # the range of list
    normalized_data = [i / max(list) for i in list]
    for i, height in enumerate(normalized_data):

        # top left corner
        x0 = i*x_width + offset + spacing
        y0 = can_height - height*340

        # bottom right corner
        x1 = ((i+1)*x_width) + offset
        y1 = can_height

        # data bars are generated as Red colored vertical rectangles
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorlist[i])
        canvas.create_text(x0+2, y0, anchor=SE, text=str(list[i]))
    root.update_idletasks()

# function to initiate the sorting process by
# calling the extension code


########################################################################################################
#binary search
def binarySearch(item, list, l=None, r=None):
    # Returns index of the item in the list if present, else -1
    if l is None and r is None:
        l = 0
        r = len(list) - 1
    if r >= l:
        mid = l + (r - l) // 2
        if list[mid] == item:
            #to make mid green mid if it = item
            drawData(list, ['Red' for x in range(mid)]+[ 'Green']+['Red' for x in range(mid, len(list))]) 
            time.sleep(2)
            return mid
        elif list[mid] > item:
            #to make mid red mid if it != item in left side
            drawData(list, ['Blue' for x in range(mid)]+['Red']+['Blue' for x in range(mid, len(list))])
            time.sleep(2)
            return binarySearch(item, list, l, mid-1)   # search in the left sublist
        else:
            #to make mid red mid if it != item in right side
            drawData(list, ['Blue' for x in range(mid)]+['Red']+['Blue' for x in range(mid, len(list))])
            time.sleep(2)
            return binarySearch(item, list, mid+1, r)   # search in the right sublist
    else:   # Element is not present in the array
        return -1



#function to start binary and buble functions
def start_algorithm():
    #call sort function
    bubble(list, drawData, speedbar.get())
    #call search function
    binarySearch(33, list)


# creating main user interface frame and
# basic layout by creating a frame
Mainframe = Frame(root, width=600, height=500, bg="lightGrey")
Mainframe.grid(row=0, column=0, padx=10, pady=5)

canvas = Canvas(root, width=550, height=380, bg="lightGrey")
canvas.grid(row=1, column=0, padx=10, pady=5)

# creating user interface area in grid way like rows and columns

# first row is title
Label(Mainframe, text="bubble sort and binary search", bg='white').grid(
    row=0, column=0, padx=5, pady=5, sticky=W)


# creating Start Button to start the sorting visualization
Button(Mainframe, text="START", bg="green", command=start_algorithm).grid(
    row=1, column=3, padx=5, pady=5)

# creating Speed Bar using scale
speedbar = Scale(Mainframe, from_=0.10, to=2.0, length=100, digits=2,
                 resolution=0.2, orient=HORIZONTAL, label="Select Speed")
speedbar.grid(row=0, column=2, padx=5, pady=5)

# creat generate button
Button(Mainframe, text="Generate", bg="Red", command=generate).grid(
    row=0, column=3, padx=5, pady=5)

# automatic window termination to stop
root.mainloop()
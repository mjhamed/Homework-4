#Mohamed Hamed
#1644926
def selection_sort_descend_trace(numbers):
    for e in range(len(numbers) - 1):
        up  = e
        for z in range(e + 1,len(numbers)):
           if numbers[z] > numbers[up]:
                up = z
        numbers[e], numbers[up]  = numbers[up], numbers[e]
        for email in (numbers):
            print(email, end=' ')
        print()
    return numbers
if __name__== "__main__":
    later_time = []
    later_time = [int(email) for email in input().split()]
    selection_sort_descend_trace(later_time)
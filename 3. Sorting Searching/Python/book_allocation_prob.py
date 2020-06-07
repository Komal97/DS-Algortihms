'''
Given :
N books which has P pages (Pi <= Pj if i<j) -----> means pages are in sorted order
assign N books to M students such that each student has subsegment of books and 
maximum number of pages assigned to a student is minimized.

Example - 
4 Books with 10, 20, 30, 40 pages
Students - 2
Output - 
out of ((10,90), (30,70), (60,40)) ---> minimum of maximum number of pages is 60 (out of 90, 70, 60)
'''

def is_valid_config(no_of_students, pages, mid):

    student_count = 1
    current_page_count = 0

    for i in range(len(pages)):
        if (current_page_count + pages[i]) > mid:
            current_page_count = pages[i]
            student_count += 1
            if student_count > no_of_students:
                return False
        else:
            current_page_count += pages[i]
    return True

def book_allocation(no_of_books, no_of_students, pages):

    total_pages = 0
    start = 0
    end = 0
    
    # sum of all pages
    for i in range(no_of_books):
        total_pages += pages[i]
        start = max(start, pages[i])
    end = total_pages
    final_ans = start

    while(start <= end):
        mid = int((start + end)/2)

        # if sum id valid then check for left part too else move to right part
        if is_valid_config(no_of_students, pages, mid):
            end = mid - 1
            final_ans = mid
        else:
            start = mid + 1
    return final_ans


def main():
    no_of_students = int(input())
    no_of_books = int(input())
    pages = list(map(int, input().split()))

    print(book_allocation(no_of_books, no_of_students, pages))

main()  
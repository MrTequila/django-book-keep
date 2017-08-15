from django.shortcuts import render
from Bookeep.models import Book

import Bookeep.foo as foo


def index(request):
    book_list = Book.objects.order_by('-start_date')
    context_dict = {'book_list': book_list}
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    y = [0]*12

    for book in book_list:
        book.time_read = book.finish_date - book.start_date
        y[book.finish_date.month-1] += book.time_read.days

    foo.generate_image(x, y)
    return render(request, 'Bookeep/index.html', context_dict)




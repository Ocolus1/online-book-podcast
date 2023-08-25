from django.shortcuts import render, get_object_or_404
from .models import BookChapter, Book 
from itertools import groupby
from operator import attrgetter
from django.db.models import Max


def group_by_category(chapters):
    # Ensure the chapters are sorted by category_id
    sorted_chapters = sorted(chapters, key=attrgetter('category_id'))
    
    # Group the chapters by category_id
    grouped = {key: list(group) for key, group in groupby(sorted_chapters, key=attrgetter('category_id'))}
    
    return grouped


def home(request, id):
    chapters = BookChapter.objects.filter(book__book_id=id).order_by('sequence_number')
    grouped_chapters = group_by_category(chapters)

    content = {
        'book': get_object_or_404(Book, book_id=id),
        'grouped_chapters': grouped_chapters,
        'id': id
    }
    return render(request, "content/book/home.html", content)


def section_detail(request, id, chapter_slug):
    book = get_object_or_404(Book, book_id=id)
    chapter = BookChapter.objects.filter(book=book).filter(slug=chapter_slug).first()
    
    chapters = BookChapter.objects.filter(book__book_id=id).order_by('sequence_number', 'category_id')
    grouped_chapters = group_by_category(chapters)
    
    # Get all the chapters within the current category
    chapters_in_category = BookChapter.objects.filter(category_text=chapter.category_text).order_by('sequence_number')
    
    # Calculate progress percentage
    total_chapters = chapters_in_category.count()
    current_chapter_position = list(chapters_in_category).index(chapter) + 1 # +1 because index starts from 0
    progress_percentage = (current_chapter_position / total_chapters) * 100
    
    # Get max category_id
    max_category_id = chapters.aggregate(Max('category_id'))['category_id__max']
    
    category_flex_values = {}
    for i in range(1, max_category_id + 1): # loop through all category_ids
        category_flex_values[str(i)] = chapters.filter(category_id=i).count()

    range_categories = range(1, max_category_id + 1)
    
    context = {
        'id': id,
        'book': book,
        'chapter': chapter,
        'grouped_chapters': grouped_chapters,
        'progress_percentage': progress_percentage,
        'max_category_id': max_category_id,
        'category_flex_values': category_flex_values,
        'range_categories': range_categories
    }
    return render(request, 'content/book/section_detail.html', context)


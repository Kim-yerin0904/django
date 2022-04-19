from django.shortcuts import render, get_object_or_404, redirect
from goodplace.models import MatZip, Review

def main(request):
    all_board = MatZip.objects.all().order_by('-MatZip_review_count', '-MatZip_rating')
    context = {
        'posts': all_board
    }
    return render(request, 'main.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from goodplace.models import MatZip, Review
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def list_map(request):
    if 'q' in request.GET:
        query = request.GET.get('q', '')
        all_board = MatZip.objects.all().filter(Q(MatZip_Address__contains=query) | Q(MatZip_Name__contains=query)).distinct()
        paginator = Paginator(all_board, 5)
        page = int(request.GET.get('page', 1))
        board_list = paginator.get_page(page)
        context = {
            'query': query,
            'board_list': board_list
        }
    else:
        all_board = MatZip.objects.all().order_by('id')
        paginator = Paginator(all_board, 5)
        page = int(request.GET.get('page', 1))
        board_list = paginator.get_page(page)

        context = {
            'board_list': board_list
        }
    return render(request, 'goodplace/list.html',context)

def detail(request, matzip_id):
    matzip = get_object_or_404(MatZip, pk=matzip_id)
    reviews = Review.objects.filter(Q(r_restaurant_id=matzip_id))
    context = {
        'matzip': matzip,
        'reviews': reviews,
    }
    return render(request, 'goodplace/DetailReviewP.html', context)


def mypage(request):
    review = Review.objects.filter(Q(r_author_id=request.user.id)).order_by('-r_time')
    context = {
        'reviews': review
    }
    return render(request, 'goodplace/mypage.html', context)

def reviewwrite(request, matzip_id):
    review = Review()
    review.r_content = request.POST['r_content']
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    review.r_author = user
    review.r_rating = request.POST['score']
    review.r_restaurant_id = matzip_id
    review.save()

    matzip = get_object_or_404(MatZip, pk=matzip_id)
    matzip.MatZip_review_count += 1
    matzip.MatZip_rating += int(request.POST['score'])
    matzip.save()

    return HttpResponseRedirect(reverse('goodplace:detail', args=(matzip_id,)))

def reviewP(request, matzip_id):
    if request.user.is_authenticated:
        matzip = get_object_or_404(MatZip, pk=matzip_id)
        context = {
            'matzip': matzip,
        }
        return render(request, 'goodplace/ReviewWrite.html', context)
    else:
        return redirect('users:login')
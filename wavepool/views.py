from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs, code_review_defs, code_design_defs
from django.conf import settings


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    # gets cover story
    cover_story = NewsPost.objects.filter(is_cover_story=True)
    # gets 3 most recent posts
    top_stories = NewsPost.objects.filter(is_cover_story=False).order_by('-publish_date')[:3]
    # gets rest of posts
    other_stories = NewsPost.objects.filter(is_cover_story=False).order_by('-publish_date')[3:]

    # if there is a cover story pass the index 0, else pass empty query set
    if len(cover_story) > 0:
        context = {
            'cover_story': cover_story[0],
            'top_stories': top_stories,
            'archive': other_stories,
        }
    else:
        context = {
            'cover_story': cover_story,
            'top_stories': top_stories,
            'archive': other_stories,
        }
    return HttpResponse(template.render(context, request))


def newspost_detail(request, newspost_id=None):
    template = loader.get_template('wavepool/newspost.html')
    newspost = NewsPost.objects.order_by('?').first()
    context = {
        'newspost': newspost
    }

    return HttpResponse(template.render(context, request))


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')

    context = {
        'code_exercise_defs': code_exercise_defs,
        'code_design_defs': code_design_defs,
        'code_review_defs': code_review_defs,
        'show_senior_exercises': settings.SENIOR_USER,
    }
    return HttpResponse(template.render(context, request))

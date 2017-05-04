from el_pagination import (
    settings,
    utils,
)
from django import template

register = template.Library()


@register.inclusion_tag("catalogue/show_more_tag.html", takes_context=True)
def show_more_with_counts(context, per_page_count, total_count, first_page_count=0,
                          verb='enteries', loading=settings.LOADING, show_total_in_end=True):
    # This template tag could raise a PaginationError: you have to call
    # *paginate* or *lazy_paginate* before including the showmore template.
    data = utils.get_data_from_context(context)
    page = data['page']
    # show the template only if there is a next page
    if page.has_next():
        request = context['request']
        page_number = page.next_page_number()
        # Generate the querystring.
        querystring_key = data['querystring_key']
        querystring = utils.get_querystring_for_page(
            request, page_number, querystring_key,
            default_number=data['default_number'])
        curr_page_num = int(request.GET.get(querystring_key, 1))
        if curr_page_num == 1:
            if first_page_count:
                start = first_page_count + 1
            else:
                start = per_page_count + 1
        else:
            if first_page_count:
                start = (curr_page_num * per_page_count) - first_page_count
            else:
                start = (curr_page_num * per_page_count) + 1
        end = (per_page_count + start) - 1
        if end > total_count:
            end = total_count
        label = 'Load %(start)s to %(end)s of %(total)s %(verb)s' % {
            'start': start, 'end': end, 'total': total_count, 'verb': verb}
        return {
            'label': label,
            'loading': loading,
            'path': data['override_path'] or request.path,
            'querystring': querystring,
            'querystring_key': querystring_key,
            'request': request,
            'show_total_in_end': show_total_in_end,
        }
    else:
        if total_count > 0:
            return {
                'label': 'Showing %(start)s of %(end)s %(verb)s' % \
                         {'start': total_count, 'end': total_count, 'verb': verb},
                'show_total_in_end': show_total_in_end,
            }
        else:
            return {}

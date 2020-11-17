from collections import OrderedDict


def custom_response(node, data, **kwargs):
    return OrderedDict([(node.page_query_param, node.page_number),
                        (node.page_size_query_param, node.page_size),
                        (node.count_param, node.page.paginator.count),
                        (node.results_param, data)])

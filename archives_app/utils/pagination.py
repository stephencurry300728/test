"""
自定义分页组件
"""

from django.utils.safestring import mark_safe

class Pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset:查询的数据，符合条件的数据对这个进行分页处理 
        :param page_size:每页显示多条数据
        :param page_param:在URL中传递获取分页的参数 列如:/?page=12 这里参数是page
        :param plus:显示当前页的，前、后几页（页码）
        """
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param

        page = request.GET.get(page_param, "1")  # 把request获取前端get请求的方法，封装到page中，页码
        if page.isdecimal():  # 处理页码，判断页码是否是正常传入数字，而不是字符串
            page = int(page)
        else:
            page = 1  # 前端传入页码不规范，则默认为1
        self.page = page
        self.page_size = page_size
        # 计算分页页码，sql值
        self.start = (page - 1) * page_size
        self.end = page * page_size

        self.page_queryset = queryset[self.start: self.end]  # 分完页的数据

        # total_count = models.PrettyNum.objects.filter(**data_dict).order_by("-price").count()
        total_count = queryset.count()  # 数据总条数

        total_page_count, div = divmod(total_count, page_size)  # 总页码 = 数据总条数/每页显示数据条数

        if div:
            total_page_count += 1

        self.total_page_count = total_page_count
        self.plus = plus  # 显示前后页码条数

    def html(self):
        """
          页码、页码搜索
          """
        # 计算出，显示当前页的前5页、后5页
        if self.total_page_count <= 2 * self.plus + 1:
            # 数据库中的数据比较少，都没有达到11页。
            start_page = 1
            end_page = self.total_page_count
        else:
            # 数据库中的数据比较多 > 11页。

            # 当前页<5时（小极值）
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1
            else:
                # 当前页 > 5
                # 当前页+5 > 总页面
                if (self.page + self.plus) > self.total_page_count:
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))

        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 页面
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)

        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        page_string = mark_safe("".join(page_str_list))
        
        return page_string


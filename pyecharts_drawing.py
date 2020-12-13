from pyecharts.charts import Map, Geo
import pyecharts.options as opts
from pyecharts.charts import Bar
from pyecharts.charts import Page
from pyecharts.charts import Line
from pyecharts.charts import Boxplot
from pyecharts.charts import Pie
import request_data

'''
01 项目成功和失败中的top5资源种类数
'''


def draw_success_resource_category_bar():
    print("This is 01_success")
    row_dict = request_data.get_state_projection_resource_category()
    return_code = row_dict['code']
    if return_code == 0:  # 返回有效数据
        success_projection_resource_category_bar = (
            Bar()
                .add_xaxis(row_dict['stateResourceCategory']['state']['success']['top5_cat'])
                .add_yaxis("项目数目", row_dict['stateResourceCategory']['state']['success']['num'])
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-60), is_scale=True),
                title_opts=opts.TitleOpts(title="成功项目", subtitle='top5资源类型'),
                # yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}")),
                # legend_opts=opts.LegendOpts(is_show=False)
            )
        )
        return success_projection_resource_category_bar
    else:  # code ==1,数据请求失败，返回的数据为null
        return 0


def draw_failed_resource_category_bar():
    print('This is 01_failed')
    row_dict = request_data.get_state_projection_resource_category()
    # print(row_dict)
    return_code = row_dict['code']
    if return_code == 0:  # 返回有效数据
        failed_projection_resource_category_bar = (
            Bar()
                .add_xaxis(row_dict['stateResourceCategory']['state']['failed']['top5_cat'])
                .add_yaxis("项目数目", row_dict['stateResourceCategory']['state']['failed']['num'])
                .set_global_opts(
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-60), is_scale=True),
                title_opts=opts.TitleOpts(title="失败项目", subtitle='top5资源类型'),
                # yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value}")),
                # legend_opts=opts.LegendOpts(is_show=False)
            )
        )
        return failed_projection_resource_category_bar
    else:  # code ==1,数据请求失败，返回的数据为null
        return 0


'''
02 成功项目和失败项目的词云图
'''

'''
03 文章长度和标题长度对项目成功失败的影响【就差这一个了】
'''

'''
04 查看成功项目和失败项目在不同发布年份的数目分布
折线图
'''
def draw_project_num_by_year_line():
    row_dict = request_data.get_project_publication_num_by_year()
    return_code = row_dict['code']
    if return_code == 0:  # 返回有效数据
        # x轴数组中的元素类型必须是字符型，不能是整数型，整数型的折线显示不出来
        x_original = row_dict['stateProjectPublication']['state']['success']['publicationYear']
        x =[]
        for i in x_original:
            x.append(str(i))
        y1 = row_dict['stateProjectPublication']['state']['success']['publicationNum']
        y2 = row_dict['stateProjectPublication']['state']['failed']['publicationNum']
        print(x_original)
        print(x)
        print(y1)
        print(y2)
        success_failed_projects_publication_by_year_line = (
            Line()
                .add_xaxis(xaxis_data=x)
                .add_yaxis(series_name="Success", y_axis=y1, symbol="arrow", is_symbol_show=True)
                .add_yaxis(series_name="Failed", y_axis=y2)
                .set_global_opts(title_opts=opts.TitleOpts(title="项目数量上的变化"))

                # .render("line.html")
        )

        return success_failed_projects_publication_by_year_line
    else:
        return 0


'''
05 项目花费：箱线图。成功和失败
y_data是一个数组：[min, Q1, median (or Q2), Q3, max]
'''
def draw_project_cost_boxplot():
    row_dict = request_data.get_project_cost()
    return_code = row_dict['code']
    if return_code == 0:
        x_data = ['Success', 'Failed']
        success_data = row_dict['stateProjectCost']['state']['success']
        y_data1 = [[success_data['min'], success_data['25%'], success_data['mean'], success_data['75%'],
                   success_data['max']]]
        failed_data = row_dict['stateProjectCost']['state']['failed']
        y_data2 = [[failed_data['min'], failed_data['25%'], failed_data['mean'], failed_data['75%'], failed_data['max']]]

        print('boxplot')
        print(x_data)
        print(y_data1)
        print(y_data2)
        project_cost_boxplot = Boxplot()
        project_cost_boxplot.add_xaxis(x_data)
        project_cost_boxplot.add_yaxis("成功项目", y_data1)
        project_cost_boxplot.add_yaxis("失败项目", y_data2)

        project_cost_boxplot.set_global_opts(title_opts=opts.TitleOpts(title="项目花费"))
        return project_cost_boxplot
    else:
        return 0


'''
06 学校所在地区的类型及数目:
可以计算每种类型的占比，然后用饼状图显示
'''
def draw_success_and_failed_school_type_pie():
    row_dict = request_data.get_school_type()
    return_code = row_dict['code']
    if return_code == 0:
        pie = Pie().set_global_opts(title_opts=opts.TitleOpts(title="地区类型"))
        success_type = row_dict['stateSchoolType']['state']['success']['schoolType']
        success_num = row_dict['stateSchoolType']['state']['success']['num']

        pie.add("", [list(x) for x in zip(success_type, success_num)],center=[250,300], radius=[30, 75], rosetype='radius')

        failed_type = row_dict['stateSchoolType']['state']['failed']['schoolType']
        failed_num = row_dict['stateSchoolType']['state']['failed']['num']
        print(type(failed_num))  # < class 'list'>

        pie.add("", [list(y) for y in zip(failed_type, failed_num)],center=[600, 300], radius=[30, 75], rosetype='area')
        pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{d}%"))
        print("pies")
        print(type(pie))
        return pie
    else:
        return 0


'''
07 年级信息
'''


def draw_grade_info_bar():
    row_dict = request_data.get_grade_info()
    return_code = row_dict['code']
    if return_code == 0:
        grade_info_bar = (Bar().add_xaxis(row_dict['stateSchoolType']['state']['success']['GradeName'])
                          .add_yaxis('成功项目', row_dict['stateSchoolType']['state']['success']['num'])
                          .add_yaxis('失败项目', row_dict['stateSchoolType']['state']['failed']['num'])
                          .set_global_opts(title_opts=opts.TitleOpts(title="年级信息")))
        return grade_info_bar
    else:
        return 0


if __name__ == "__main__":
    main_page = Page(layout=Page.DraggablePageLayout)  # 指定布局中的每个模块都可以被人为地拖拽
    success_resource_category_bar = draw_success_resource_category_bar()
    failed_resource_category_bar = draw_failed_resource_category_bar()
    project_num_by_year_line = draw_project_num_by_year_line()
    project_cost_boxplot = draw_project_cost_boxplot()
    success_and_failed_school_type_pie = draw_success_and_failed_school_type_pie()
    main_page.add(success_resource_category_bar)
    main_page.add(failed_resource_category_bar)
    main_page.add(project_num_by_year_line)
    main_page.add(project_cost_boxplot)
    main_page.add(success_and_failed_school_type_pie)

    # draw_grade_info_bar()

    main_page.render('main_page_temp.html')
    # Page.save_resize_html('main_page_temp.html', cfg_file='./config_json/main_page.json',
    #                       dest='./templates/main_page.html')

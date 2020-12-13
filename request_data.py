import requests
import json

findResourceCategory_api_url = 'http://81.68.67.118:8000/api/firstpart/findResourceCategory'
'''
    01 该州成功和失败项目分别最常用的一些资源
'''
def get_state_projection_resource_category():
    '''
    获取后台服务，接受传过来的数据：
    该州成功和失败项目分别最常用的一些资源
    :return :is a dictionary
    如果成功，code=0
    {'code': 0, 'stateResourceCategory':
    {'state':
    {'success': {'top5_cat': ['Supplies', 'Technology', 'Books', 'Trips', 'Computers & Tablets'], 'num': [41052, 34038, 20630, 2664, 2300]},
     'failed': {'top5_cat': ['Technology', 'Supplies', 'Books', 'Trips', 'Computers & Tablets'], 'num': [15945, 11635, 3959, 671, 193]}
     }}}
     如果失败，code=1，并且数据=null
    '''
    data = {
        'stateName':'California',
        'year':'[2011,2013]'
            }
    response = requests.get(findResourceCategory_api_url,params=data)
    print(response.status_code)
    api_dict = response.json()
    # api_dict = response.content.decode()
    api_status_code = response.status_code
    if api_status_code ==200: # 如果请求成功,返回传过来的dict数据
        return api_dict
    else:
        return api_status_code
#print(get_state_projection_resource_category())
'''
04 查看不同年份成功项目和失败项目的数目变化情况
'''
findProjectPublicationNumByYear_api_url = 'http://81.68.67.118:8000/api/firstpart/findprojectPublicationNumByYear'
def get_project_publication_num_by_year():
    data = {
        'stateName':'California',
    }
    response = requests.get(findProjectPublicationNumByYear_api_url, params=data)
    print(response.status_code)
    api_dict = response.json()
    print("project publication num by year \n")
    # api_dict = response.content.decode()    # response.content这样获取的数据是二进制数据，可以用于下载图片或者视频
    print(api_dict)
    api_status_code = response.status_code
    if api_status_code == 200:  # 如果请求成功,返回传过来的dict数据
        return api_dict
    else:
        return api_status_code

'''
05 项目花费：用箱线图（或者称盒式图）展示中位数，上下限啥的
'''
findProjectCost_api_url = 'http://81.68.67.118:8000/api/firstpart/findProjectCost'
def get_project_cost():
    data = {
        'stateName': 'California',
    }
    response = requests.get(findProjectCost_api_url, params=data)
    print(response.status_code)
    api_dict = response.json()
    api_status_code = response.status_code
    if api_status_code == 200:  # 如果请求成功,返回传过来的dict数据
        return api_dict
    else:
        return api_status_code
'''
06 学校所在地区的类型及数目:
可以计算每种类型的占比，然后用饼状图显示
'''
findSchoolType_api_url = 'http://81.68.67.118:8000/api/firstpart/findSchoolType'
def get_school_type():
    data = {
        'stateName': 'California',
    }
    response = requests.get(findSchoolType_api_url, params=data)
    # print(response.status_code)
    api_dict = response.json()
    api_status_code = response.status_code
    if api_status_code == 200:  # 如果请求成功,返回传过来的dict数据
        return api_dict
    else:
        return api_status_code

'''
07 年级信息
'''
findGradeInfo_api_url = 'http://81.68.67.118:8000/api/firstpart/findGradeInfo'
def get_grade_info():
    data = {
        'stateName': 'California',
    }
    response = requests.get(findGradeInfo_api_url, params=data)
    # print(response.status_code)
    api_dict = response.json()
    api_status_code = response.status_code
    if api_status_code == 200:  # 如果请求成功,返回传过来的dict数据
        return api_dict
    else:
        return api_status_code



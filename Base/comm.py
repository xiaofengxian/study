__author__ = 'Administrator'
class http_commom:
    list_arg = []
    request_num = []
    response_time = []
    dct_arg = {'ytitle': '响应时间', 'xtitle': '请求数量', 'title': '登陆'}
    count = 5 #请求总数
    base_url = '119.29.57.169'
    http_api = '/QiXun/index.php/QiXunManager/Interface/UserLogin?userName=ywy002&password=123456'
    method = 'get'
    mat = "plot" #pie bar,plot
    xlim = 5 # 曲线设置横x轴的上下限
    ylim = 3 # 曲线设置横y轴的上下限
    sum_03 = 0
    sum_5 = 0
    sum_1 = 0
    sum_other = 0
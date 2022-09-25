from rest_framework.exceptions import APIException
from rest_framework.views import Response


def APIResponse(msg, data=None):
    """接口常规响应封装"""

    if data is None:
        return Response(msg)
    if isinstance(data, dict):
        data["msg"] = str(msg)
        return Response(data)
    elif isinstance(data, list):
        return Response({"msg":str(msg),"list_data":data})
    else:
        return Response(msg)


class APIError(APIException):
    """接口错误响应封装"""

    status_code = 200
    default_detail = "接口请求失败"
    default_code = 999

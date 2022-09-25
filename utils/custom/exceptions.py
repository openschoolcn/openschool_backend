from rest_framework.views import exception_handler
from rest_framework.views import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # 这个循环是取第一个错误的提示用于渲染
    for index, value in enumerate(response.data):
        if index == 0:
            key = value
            value = response.data[key]

            if isinstance(value, str):
                error_msg = value
            else:
                error_msg = key + value[0]

    if response is None:
        # print(exc)  # 错误原因   还可以做更详细的原因，通过判断exc信息类型
        # print(context)  # 错误信息
        # print("1234 = %s - %s - %s" % (context["view"], context["request"].method, exc))
        return Response(
            {
                "error_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "error_msg": "服务器未知错误",
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            exception=True,
        )

    else:
        # response不为None，说明是drf可以处理的异常
        # print('123 = %s - %s - %s' % (context['view'], context['request'].method, exc))
        error_code = 999 if response.status_code == 200 else response.status_code
        return Response(
            {"error_code": error_code, "error_msg": error_msg},
            status=response.status_code,
            exception=True,
        )

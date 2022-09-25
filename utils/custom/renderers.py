from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):
    """自定义JSON数据返回类"""

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            res = dict()
            if isinstance(data, dict):
                res["code"] = data.get("code", 1000)
                res["msg"] = data.pop("msg", "success")
                res["data"] = data
                if "list_data" in list(data.keys()):
                    res["data"] = data.pop("list_data",[])
                if "error_msg" in list(data.keys()):
                    res["code"] = (
                        data["error_code"] if "error_code" in list(data.keys()) else 999
                    )
                    res["msg"] = data["error_msg"]
                    del res["data"]
            elif isinstance(data, str):
                res["code"] = 1000
                res["msg"] = data
            else:
                res["code"] = 1000
                res["msg"] = "success"
            return super().render(res, accepted_media_type, renderer_context)
        else:
            return super().render(data, accepted_media_type, renderer_context)

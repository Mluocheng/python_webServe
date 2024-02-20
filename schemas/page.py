from pydantic import BaseModel


class PageSchema(BaseModel):
    """ 分页查询参数 """
    page: int = 1
    page_size: int = 10
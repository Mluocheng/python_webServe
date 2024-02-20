# from fastapi import FastAPI

# app = FastAPI() # 创建 api 对象

# @app.get("/") # 根路由
# def root():
#     return {"武汉": "加油！！！"}

# @app.get("/say/{data}")
# def say(data: str,q: int = None):
#     return {"data": data, "item": q}



#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @desc : 用户接口
from fastapi import APIRouter
from starlette.responses import Response

# from common.depends import GetDB, CheckCookie, PageQuery
from common.result import ResultSchema, Result
from common.route_log import LogRoute
# from core.security import rsa_decrypt_password, verify_password
# from crud import resource_crud, user_crud, role_crud
# from models import LocalUser
# from schemas import MenuOut, UserOut, UserLogin
# from common.custom_exc import UserErrors
# from utils.handle_cookie import clear_cookie, set_cookie
# from utils.handle_menu import generate_tree_menu

router = APIRouter(route_class=LogRoute)


# @router.get("/") # 根路由
# def root():
#     return {"武汉": "加油！！！"}

@router.get("/say") 
def say(data: str,q: int = None):
    # return {"data": data, "item": q}
    return Result.success(data={"data": data, "item": q})

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @desc : 注册路由
from fastapi import FastAPI, Depends

# from apis import public, user, sys_log, upload, echarts, role, resource
from apis.controller import test
from common.depends import check_permission
from core.config import settings


def register_router(app: FastAPI):
    """ 注册路由 """

    app.include_router(test.router, prefix=settings.API_PREFIX, tags=["Test"])

    # app.include_router(echarts.router, prefix=settings.API_PREFIX, tags=["Echarts"],
    #                    dependencies=[Depends(check_permission([]))])

    # app.include_router(user.router, prefix=settings.API_PREFIX + "/user", tags=["User"],
    #                    dependencies=[Depends(check_permission([]))])

    # app.include_router(role.router, prefix=settings.API_PREFIX + "/role", tags=["Role"],
    #                    dependencies=[Depends(check_permission([]))])

    # app.include_router(resource.router, prefix=settings.API_PREFIX + "/resource", tags=["Resource"],
    #                    dependencies=[Depends(check_permission([]))])

    # app.include_router(sys_log.router, prefix=settings.API_PREFIX + "/log", tags=["Log"],
    #                    dependencies=[Depends(check_permission([]))])

    # app.include_router(upload.router, prefix=settings.API_PREFIX + "/upload", tags=["Upload"])
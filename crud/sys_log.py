#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @desc : 日志表的增删改查
from crud.base import CRUDBase
from models._init_ import SysLog
from schemas._init_ import SysLogIn


class CRUDUserRole(CRUDBase[SysLog, SysLogIn, SysLogIn]):
    pass


sys_log_crud = CRUDUserRole(SysLog)
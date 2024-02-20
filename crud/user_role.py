#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @desc : 用户角色表的增删改查
from crud.base import CRUDBase
from models._init_ import UserRole
from schemas._init_ import UserRoleIn


class CRUDUserRole(CRUDBase[UserRole, UserRoleIn, UserRoleIn]):
    pass


user_role_crud = CRUDUserRole(UserRole)
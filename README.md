# fastapi 框架 启动一个web服务
    

## 文件说明
	-- api									    # 接口文件夹
    -- common                   # 公共文件夹
    -- core                     # 核心文件夹
        -- config.py              # 配置文件夹
    -- crud                     # 数据库增删改查文件夹
    -- models                   
        -- database               # mysql 表模型
        -- redis                  # redis 表模型
    -- register                 # 注册中心
    -- schemas                  # 模型文件夹 (Java中的实体类或者VO视图类)
    -- static                   # 静态文件夹
    -- utils                    # 工具文件夹
    -- Dockerfile               # 后端服务部署文件
    -- main.py                  # 项目启动文件

## 安装
    pip install fastapi 
    pip install uvicorn

    需要配置mysql 和 redis


## 启动
    uvicorn main:app --reload
    python main.py
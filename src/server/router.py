from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import *


routers = (
    RouterManager(
        database_model=database_models.User,
        pydantic_model=pydantic_models.User,
        prefix='/user',
        tags=['User']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.AuthData,
        pydantic_model=pydantic_models.AuthData,
        prefix='/auth_data',
        tags=['AuthData']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Staff,
        pydantic_model=pydantic_models.Staff,
        prefix='/staff',
        tags=['Staff']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.FiredStaff,
        pydantic_model=pydantic_models.FiredStaff,
        prefix='/fired_staff',
        tags=['FiredStaff']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Menu,
        pydantic_model=pydantic_models.Menu,
        prefix='/menu',
        tags=['Menu']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Orders,
        pydantic_model=pydantic_models.Orders,
        prefix='/orders',
        tags=['Orders']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.UserAddress,
        pydantic_model=pydantic_models.UserAddress,
        prefix='/user_address',
        tags=['UserAddress']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.ProductOrders,
        pydantic_model=pydantic_models.ProductOrders,
        prefix='/product_orders',
        tags=['ProductOrders']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Product,
        pydantic_model=pydantic_models.Product,
        prefix='/product',
        tags=['Product']
    ).fastapi_router,

)

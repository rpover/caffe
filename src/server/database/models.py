import peewee
import settings

db: peewee.SqliteDatabase = peewee.SqliteDatabase(f'{settings.DATABASE_PATH}{settings.DATABASE_NAME}')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class User(BaseModel):
    name: peewee.CharField = peewee.CharField(null=False, default='')


class AuthData(BaseModel):
    login: peewee.CharField = peewee.CharField(default="")
    password: peewee.CharField = peewee.CharField(default="")
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='auth_data_user_id', default=0)


class Staff(BaseModel):
    name: peewee.CharField = peewee.CharField(default='')


class FiredStaff(BaseModel):
    staff_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Staff, related_name='fired_staff_id')


class Orders(BaseModel):
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_order_user_id', default=0)
    menu_position_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Menu, related_name='orders_menu_position_id', default=0)


class Menu(BaseModel):
    name: peewee.CharField = peewee.CharField(default='')
    price: peewee.IntegerField = peewee.IntegerField(default=0)
    cooking_time: peewee.FloatField = peewee.FloatField(default=0)


class UserAddress(BaseModel):
    address: peewee.CharField = peewee.CharField(null=False, default="")
    user_id: peewee.ForeignKeyField = peewee.ForeignKeyField(User, related_name='user_address_user_id', default=0)


class ProductOrderds(BaseModel):
    product_id: peewee.ForeignKeyField = peewee.ForeignKeyField(Product, related_name='user_discount_product_id', default=0)
    count: peewee.IntegerField = peewee.IntegerField(null=False, default=0)


class Products(BaseModel):
    count: peewee.IntegerField = peewee.IntegerField(default=0)
    name: peewee.CharField = peewee.CharField(default='')



db.create_tables([
    User,
    AuthData,
    Staff,
    FiredStaff,
    UserOrder,
    Discount,
    UserAddress,
    ProductOrderds,
    Menu,
])

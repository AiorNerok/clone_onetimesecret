import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi


class MongoTools:
    __client = AsyncIOMotorClient(
        "mongodb+srv://root:iamroot@onetimesecret.qp62kjq.mongodb.net/",
        server_api=ServerApi("1"),
    )

    @classmethod
    async def get(cls):
        print(dir(cls.__client))

asyncio.run(MongoTools.get())

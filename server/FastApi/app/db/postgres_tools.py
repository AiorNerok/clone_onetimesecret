# https://console.neon.tech/

from sqlmodel import SQLModel, Field, create_engine, Session


engine = create_engine('postgresql://AiorNerok:3f1FzvRLKdoH@ep-curly-mouse-546339.eu-central-1.aws.neon.tech/neondb')

def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

class PostgresTool:
    __client = create_engine('')
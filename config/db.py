from sqlalchemy import create_engine, MetaData

engine =  create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format('root', '12345678', "localhost", "3306",'test'))

meta = MetaData()

conn = engine.connect()
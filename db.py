from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

meta = MetaData()

hosts = Table(
    'Hosts', meta,

    Column('id', Integer, primary_key=True),
    Column('host_name', String(200), nullable=False),
    Column('host_addr', String(200), nullable=False),
    Column('host_cpu', String(200), nullable=False),
    Column('host_ram', String(200), nullable=False)
)

logs = Table(
    'Logs', meta,

    Column('id', Integer, primary_key=True),
    Column('host_id', Integer, nullable=False),
    Column('last_up', Date, nullable=False),
    Column('last_hash', String(200), nullable=False),

    Column('host_id',
           Integer,
           ForeignKey('Hosts.id', ondelete='CASCADE'))
)
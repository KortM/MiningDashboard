import os
import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)
from sqlalchemy.orm import sessionmaker, relationship

basedir =os.path.abspath(os.path.dirname(__file__))
name = '/BD.db'
engine = create_engine("sqlite:///"+basedir+name)
Base = declarative_base()
Session =sessionmaker(bind= engine)

meta = MetaData()

class Hosts(Base):
    __tablename__ = 'Hosts'
    id = Column(Integer, primary_key=True)
    host_name = Column(String(200), nullable=False)
    host_addr = Column(String(200), nullable=False)
    host_cpu = Column(String(200), nullable=False)
    host_ram = Column(String(200), nullable=False)
    host_status = Column(String(1), nullable = False)
    
    def __init__(self, host_name, host_addr, host_cpu, host_ram, host_status):
        self.host_name = host_name
        self.host_addr = host_addr
        self.host_cpu = host_cpu
        self.host_ram = host_ram
        self.host_status = host_status

    def __repr__(self):
        return 'Name: {}, Addr: {}, CPU: {}, RAM: {}, Status: {}'\
        .format(self.host_name, self.host_addr, self.host_cpu, self.host_ram, self.host_status)

class Logs(Base):
    __tablename__ = 'Logs'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, nullable=False)
    last_up = Column(Date, nullable=False)
    last_hash = Column(String(200), nullable=False)
    relationship('Hosts', foreign_keys='Hosts.id')

    def __init__(self, host_id, last_up, last_hash):
        self.host_id = host_id
        self.last_up = last_up
        self.last_hash = last_hash
    
    def __repr__(self):
        return 'Host_ID: {}, UP: {}, Hash: {}'.format(self.host_id, self.last_up, self.last_hash)

def sample_data():
    host = Hosts('Test', '192.168.1.9', '200GC', '8000', 'L')
    logs = Logs(1, datetime.datetime.now(), '2000h')
    s = Session()
    s.add(host)
    s.add(logs)
    s.commit()
    print(s.query(Hosts).all())
    print(s.query(Logs).all())

Base.metadata.create_all(engine)

if __name__ == '__main__':
    sample_data()
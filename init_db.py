import os
import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)
from sqlalchemy.orm import sessionmaker, relationship
from werkzeug.security import check_password_hash, generate_password_hash
import random

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

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key = True)
    email = Column(String(200), nullable=False)
    passwd_hash = Column(String(200), nullable=False)
    login = Column(String(200), nullable=False)
    api_key = Column(String(200))

    def __init__(self, email, login):
        self.email = email
        self.login = login
    
    def __repr__(self):
        return 'Email: {}, PWD: {}'.format(self.email, self.passwd_hash)
    
    def set_password(self, password):
        self.passwd_hash = generate_password_hash(password)

    def check_passwd(self, passwd):
        return check_password_hash(self.passwd_hash, passwd)
    
    def set_apikey(self):
        self.api_key = random.getrandbits(128)
    
    def check_apikey(self, key):
        if self.api_key == key:
            return True
        else:
            return False

def sample_data():
    host = Hosts('Test', '192.168.1.9', '200GC', '8000', 'L')
    logs = Logs(1, datetime.datetime.now(), '2000h')
    user = User('cort202@gmail.com', 'kort')
    user.set_password('mar02031812')
    s = Session()
    s.add(host)
    s.add(logs)
    s.add(user)
    s.commit()
    print(s.query(Hosts).all())
    print(s.query(Logs).all())
    print(s.query(User).all())

Base.metadata.create_all(engine)

if __name__ == '__main__':
    sample_data()
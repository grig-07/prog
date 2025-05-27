from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Поставщик(Base):
    __tablename__ = 'поставщики'
    id = Column(Integer, primary_key=True)
    название = Column(String, nullable=False)
    товары = relationship('Товар', back_populates='поставщик')

    def __repr__(self):
        return f"<Поставщик(id={self.id}, название='{self.название}')>"

class Склад(Base):
    __tablename__ = 'склады'
    id = Column(Integer, primary_key=True)
    местоположение = Column(String, nullable=False)
    товары = relationship('Товар', back_populates='склад')

    def __repr__(self):
        return f"<Склад(id={self.id}, местоположение='{self.местоположение}')>"

class Товар(Base):
    __tablename__ = 'товары'
    id = Column(Integer, primary_key=True)
    название = Column(String, nullable=False)
    склад_id = Column(Integer, ForeignKey('склады.id'), nullable=False)
    поставщик_id = Column(Integer, ForeignKey('поставщики.id'), nullable=False)
    склад = relationship('Склад', back_populates='товары')
    поставщик = relationship('Поставщик', back_populates='товары')

    def __repr__(self):
        return f"<Товар(id={self.id}, название='{self.название}', склад_id={self.склад_id}, поставщик_id={self.поставщик_id})>"

# Создание соединения с базой данных
engine = create_engine('sqlite:///warehouse.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
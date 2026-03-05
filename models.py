from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class MileageRecord(Base):
    __tablename__ = 'mileage_records'
    id = Column(Integer, primary_key=True)
    mileage = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    photo_path = Column(String, nullable=True)
    fuel_fills = relationship('FuelFill', back_populates='mileage_record')

class FuelFill(Base):
    __tablename__ = 'fuel_fills'
    id = Column(Integer, primary_key=True)
    liters = Column(Float, nullable=False)
    cost = Column(Float, nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    mileage_record_id = Column(Integer, ForeignKey('mileage_records.id'))
    mileage_record = relationship('MileageRecord', back_populates='fuel_fills')

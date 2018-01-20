from sqlalchemy import Column, Integer, String, Boolean

from cellphonedb.extensions import db


class Multidata(db.Model):
    __tablename__ = 'multidata'
    id_multidata = Column(Integer, nullable=False, primary_key=True)

    name = Column(String, nullable=False, unique=True)

    receptor = Column(Boolean)
    receptor_highlight = Column(Boolean)
    receptor_desc = Column(String)
    adhesion = Column(Boolean)
    other = Column(Boolean)
    other_desc = Column(String)
    transporter = Column(Boolean)
    secreted_highlight = Column(Boolean)
    secreted_desc = Column(String)
    transmembrane = Column(Boolean)
    secretion = Column(Boolean)
    peripheral = Column(Boolean)
    iuhpar_ligand = Column(Boolean)
    cytoplasm = Column(Boolean)
    extracellular = Column(Boolean)
    integrin_interaction = Column(Boolean)
    is_complex = Column(Boolean)
    is_cellphone_receptor = Column(Boolean)
    is_cellphone_ligand = Column(Boolean)

    protein = db.relationship('Protein', backref='protein', lazy='subquery')
    complex = db.relationship('Complex', backref='complex', lazy='subquery')

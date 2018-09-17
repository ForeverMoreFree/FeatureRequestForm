from featurerequest import db

## Our one database
class Feature(db.Model):
    __tablename__ = 'features'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    client = db.Column(db.Text)
    client_priority = db.Column(db.Integer)
    target_date = db.Column(db.Text)
    product_area = db.Column(db.Text)

    def __init__(self,title,description,client,client_priority,target_date,product_area):
        self.title = title
        self.description = description
        self.client = client
        self.client_priority = client_priority
        self.target_date = target_date
        self.product_area = product_area


 #id,name ,description,tags,stock,price,category
class Product:
    def __init__(self,id,name,description,category,tags,stock,price):
        self.id=id
        self.name=name
        self.description=description
        self.category=category
        self.tags=tags
        self.stock=stock
        self.price=price
    def __str__(self):
        return f'[id={self.id},name={self.name},description={self.description},category={self.category},tags={self.tags},stock={self.stock},price={self.price}]'
    def __repr__(self):
        return self.__str__()
    
mobile_vivo=Product(1001,'vivo v21','Good Camera Quality.','mobile','mobile,electronics ,smart phone,android phone',10,21000)
print(mobile_vivo) 

mobile_samsung=Product(1002,'samsung s24 ultra','Good Camera Quality.','mobile','mobile,electronics ,smart phone,android phone',10,130000)

print(mobile_samsung)
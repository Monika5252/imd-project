from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

## History Table

class trs(models.Model):
    kdno=models.CharField(max_length=255)
    sors_sink=models.CharField(max_length=255)
    ref1=models.CharField(max_length=255)
    ref2=models.CharField(max_length=255)
    ref3=models.CharField(max_length=255)
    unit_cost=models.CharField(max_length=255)
    iss_srs=models.IntegerField()
    trs_type=models.IntegerField()
    qty_trs=models.IntegerField()
    balance=models.IntegerField()

    def __str__(self):
        return self.kdno

    class Meta:
        db_table = 'trs'


class Category(models.Model):
    category=models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Subcategory(models.Model):
    subcategory=models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_consumable=models.BooleanField(default=False)




    def __str__(self):
        return self.subcategory



class Description(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.description





class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    address = models.TextField()
    email = models.EmailField(max_length=100)
    gstin = models.CharField(max_length=15, unique=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)




class Consumer(models.Model):
    STATUS_CHOICES=[
        ('FS','FS'),
        ('LB','LB'),
        ('MI','MI'),
        ('PS','PS'),
    ]
    id = models.AutoField(primary_key=True)
    U_Type=models.CharField(max_length=50,choices=STATUS_CHOICES)
    name=models.CharField(max_length=255)
    phone = models.CharField(max_length=12 ,default="")
    address = models.TextField()
    email = models.EmailField(max_length=100)
    gstin = models.CharField(max_length=15, unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)



class Stock(models.Model):

    CONDITION = [
        ('GOOD', 'GOOD'),
        ('TORN', 'TORN'),
        ('DAMAGED', 'DAMAGED'),
    ]
    MODE_OF_DELEVERY = [
        ('BY-HAND', 'BY-HAND'),
        ('COURIER', 'COURIER'),
        ('OTHER', 'OTHER'),

    ]

    STATUS_UNIT = [
        ('Mtr', 'Mtr'),
        ('Cm', 'Cm'),
        ('Mm', 'Mm'),
        ('Kg', 'Kg'),
        ('Gm', 'Gm'),
        ('Ltr', 'Ltr'),
        ('SqMtr', 'SqMtr'),
        ('SqCm', 'SqCm'),
        ('CuM', 'CuM'),
        ('Ream', 'Ream'),
        ('Doz', 'Doz'),
        ('Pkts', 'Pkts'),
        ('Pairs', 'Pairs'),
        ('Rolls', 'Rolls'),
    ]



    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    description=models.ForeignKey(Description,on_delete=models.CASCADE)
    name=models.ForeignKey(Consumer,on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=STATUS_UNIT)
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    Mode_of_delivery = models.CharField(max_length=50, choices=MODE_OF_DELEVERY)  # received by
    label_code = models.CharField(max_length=20, default="")
    condition = models.CharField(max_length=50, choices=CONDITION)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subcategory)

#noncpnsumable




class NonCategory(models.Model):
    category=models.CharField(max_length=255)
    def __str__(self):
        return self.category


class NonSubcategory(models.Model):
    subcategory=models.CharField(max_length=255)
    category = models.ForeignKey(NonCategory, on_delete=models.CASCADE)
    is_consumable=models.BooleanField(default=False)
    def __str__(self):
        return self.subcategory




class NonDescription(models.Model):
    category = models.ForeignKey(NonCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(NonSubcategory, on_delete=models.CASCADE)
    description=models.TextField(max_length=255)

    def __str__(self):
        return self.description








class NonStock(models.Model):

    CONDITION = [
        ('GOOD', 'GOOD'),
        ('TORN', 'TORN'),
        ('DAMAGED', 'DAMAGED'),
    ]
    MODE_OF_DELIVERY = [
        ('BY-HAND', 'BY-HAND'),
        ('COURIER', 'COURIER'),
        ('OTHER', 'OTHER'),

    ]

    STATUS_UNIT = [
        ('Mtr', 'Mtr'),
        ('Cm', 'Cm'),
        ('Mm', 'Mm'),
        ('Kg', 'Kg'),
        ('Gm', 'Gm'),
        ('Ltr', 'Ltr'),
        ('SqMtr', 'SqMtr'),
        ('SqCm', 'SqCm'),
        ('CuM', 'CuM'),
        ('Ream', 'Ream'),
        ('Doz', 'Doz'),
        ('Pkts', 'Pkts'),
        ('Pairs', 'Pairs'),
        ('Rolls', 'Rolls'),
    ]



    category=models.ForeignKey(NonCategory,on_delete=models.CASCADE)
    subcategory=models.ForeignKey(NonSubcategory,on_delete=models.CASCADE)
    description=models.ForeignKey(NonDescription,on_delete=models.CASCADE)
    name=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    unit = models.CharField(max_length=50, choices=STATUS_UNIT)
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField(default=1)
    Mode_of_delivery = models.CharField(max_length=50, choices=MODE_OF_DELIVERY)  # received by
    label_code = models.CharField(max_length=20, default="")
    condition = models.CharField(max_length=50, choices=CONDITION)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.subcategory)


class PurchaseBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE, related_name='purchaseconsumer')

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return PurchaseItem.objects.filter(billno=self)

    def get_total_price(self):
        purchaseitems = PurchaseItem.objects.filter(billno=self)
        total = 0
        for item in purchaseitems:
            total += item.totalprice
        return total



class PurchaseBillDetails(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, related_name='purchasedetailsbillno')
    total = models.CharField(max_length=50, blank=True, null=True)
    is_deleted=models.BooleanField(default=False)


    def __str__(self):
        return "Bill no: " + str(self.billno.billno)

class PurchaseItem(models.Model):
    billno = models.ForeignKey(PurchaseBill, on_delete=models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.subcategory


#nonconsumable
class NonPurchaseBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='nonpurchasesupplier')

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return NonPurchaseItem.objects.filter(billno=self)

    def get_total_price(self):
        nonpurchaseitems = NonPurchaseItem.objects.filter(billno=self)
        total = 0
        for item in nonpurchaseitems:
            total += item.totalprice
        return total



class NonPurchaseBillDetails(models.Model):
    billno = models.ForeignKey(NonPurchaseBill, on_delete=models.CASCADE, related_name='nonpurchasedetailsbillno')
    total = models.CharField(max_length=50, blank=True, null=True)
    is_deleted=models.BooleanField(default=False)


    def __str__(self):
        return "Bill no: " + str(self.billno.billno)

class NonPurchaseItem(models.Model):
    billno = models.ForeignKey(NonPurchaseBill, on_delete=models.CASCADE, related_name='nonpurchasebillno')
    nonstock = models.ForeignKey(NonStock, on_delete=models.CASCADE, related_name='nonpurchaseitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)
    is_deleted=models.BooleanField(default=False)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.nonstock.subcategory



class NonSaleBill(models.Model):
    CONDITION = [
        ('GOOD', 'GOOD'),
        ('TORN', 'TORN'),
        ('DAMAGED', 'DAMAGED'),
    ]
    MODE_OF_DELIVERY = [
        ('BY-HAND', 'BY-HAND'),
        ('COURIER', 'COURIER'),
        ('OTHER', 'OTHER'),

    ]

    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    category = models.ForeignKey(NonCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(NonSubcategory, on_delete=models.CASCADE)
    description = models.ForeignKey(NonDescription, on_delete=models.CASCADE)
    Mode_of_delivery = models.CharField(max_length=50, choices=MODE_OF_DELIVERY)  # received by
    label_code = models.CharField(max_length=20, default="")
    issued_to = models.CharField(max_length=50)
    gstin = models.CharField(max_length=15, unique=True)
    # condition = models.CharField(max_length=50, choices=CONDITION)
    is_deleted=models.BooleanField(default=False)




    def __str__(self):
        return str(self.name)



    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return NonSaleItem.objects.filter(billno=self)

    def get_total_price(self):
        saleitems = NonSaleItem.objects.filter(billno=self)
        total = 0
        for item in saleitems:
            total += item.totalprice
        return total


# contains the sale stocks made
class NonSaleItem(models.Model):
    billno = models.ForeignKey(NonSaleBill, on_delete=models.CASCADE, related_name='nonsalebillno')
    nonstock = models.ForeignKey(NonStock, on_delete=models.CASCADE, related_name='nonsaleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    # def __str__(self):
    #     return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    def __str__(self):
        return "Bill no: " + str(self.billno.billno)

        # return  "Bill no: " + str(self.billno.billno),"Stock Name: " + str(self.stock.subcategory)




# contains the other details in the sales bill
class NonSaleBillDetails(models.Model):
    billno = models.ForeignKey(NonSaleBill, on_delete=models.CASCADE, related_name='nonsaledetailsbillno')

    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)





class SaleBill(models.Model):

    CONDITION = [
        ('GOOD', 'GOOD'),
        ('TORN', 'TORN'),
        ('DAMAGED', 'DAMAGED'),
    ]
    MODE_OF_DELIVERY = [
        ('BY-HAND', 'BY-HAND'),
        ('COURIER', 'COURIER'),
        ('OTHER', 'OTHER'),

    ]

    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    Mode_of_delivery = models.CharField(max_length=50, choices=MODE_OF_DELIVERY)  # received by
    label_code = models.CharField(max_length=20, default="")
    issued_to = models.CharField(max_length=50)
    gstin = models.CharField(max_length=15, unique=True)

    # condition = models.CharField(max_length=50, choices=CONDITION)
    is_deleted=models.BooleanField(default=False)




    def __str__(self):
        return str(self.name)



    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return SaleItem.objects.filter(billno=self)

    def get_total_price(self):
        saleitems = SaleItem.objects.filter(billno=self)
        total = 0
        for item in saleitems:
            total += item.totalprice
        return total


# contains the sale stocks made
class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.IntegerField(default=1)
    totalprice = models.IntegerField(default=1)

    # def __str__(self):
    #     return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.name
    def __str__(self):
        return "Bill no: " + str(self.billno.billno)

        # return  "Bill no: " + str(self.billno.billno),"Stock Name: " + str(self.stock.subcategory)




# contains the other details in the sales bill
class SaleBillDetails(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='saledetailsbillno')

    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)




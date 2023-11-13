#from dataclasses import dataclass
from pydantic import BaseModel, field_validator

#from .dto.ItemOrigin import ItemOrigin
#from .dto.InventoryItem import InventoryItem
from dto import ItemOrigin, InventoryItem

def main():
    item_origin = ItemOrigin(country="Ethiopia", production_date="10th Aug 2000")
    my_item1 = InventoryItem(name="printer", quantity=1, serial_number="XHSD1234", origin=item_origin)
    print(my_item1.__dict__)
    my_serialised_object = my_item1.__dict__
    print(my_serialised_object)
    my_item2 = InventoryItem(**my_serialised_object)
    print(my_item2.__dict__)    

if __name__ == "__main__":
    main()
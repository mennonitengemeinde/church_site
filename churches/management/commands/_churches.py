from churches.models import Church


def create_churches():
    Church.objects.create(name='Church 1', street='7642 S. High Road', city='Westland', province_state='Michigan',
                          country='US')
    Church.objects.create(name='Church 2', street='46 Shadow Brook Street', city='Naples', province_state='Florida',
                          country='US')
    Church.objects.create(name='Church 3', street='13 San Carlos St.', city='Christiansburg', province_state='Virginia',
                          country='US')
    Church.objects.create(name='Church 4', street='489 Maple Ave.', city='Frankfort', province_state='Kentucky',
                          country='US')

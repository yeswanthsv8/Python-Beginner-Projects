"""
CH: Country History
RO: Region Origin
Phonenumbers is one of the modules that provides numerous features 
like providing basic information of a phone number, validation of a phone number etc. 
Geocoder: is to know the location on the earth's surface.

Modules:
phonenumbers
parse
geocoder
carrier
test
Number
"""

from phonenumbers import parse,geocoder,carrier
from Test import number

phoneNumber=parse(number,'CH')
print(geocoder.description_for_number(phoneNumber,'en'))

phoneNumber=parse(number,'RO')
print(carrier.name_for_number(phoneNumber,'en'))
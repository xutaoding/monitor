from django.test import TestCase
import re

# Create your tests here.
s = ''
pk = re.compile(r'id=(?P<pk>.*)').search(s)
print pk.groupdict()

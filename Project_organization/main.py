
"""     CASE 1
from connections import wifi

wifi.connect_wifi()
"""

""" CASE 2
from connections.wifi import connect_wifi

connect_wifi()
"""

""" CASE 3
import connections.wifi as w

w.connect_wifi()
"""

""" CASE 4
from connections.bl import * # *: import all

connect_bl()
"""

""" CASE 5
from connections import *

bl.connect_bl()
connect_wifi()
"""
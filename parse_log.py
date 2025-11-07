from dataclasses import dataclass
import re



"""
her bir satirda lps22df_pattern eslesmesi olup olmadigini arastiracak
eger eslesme olursa
'GetPressure -> Temperature:\s*([\d.]+)\s*C'

"""
@dataclass
class parse_into_single_telemetry:
    device : str
    lps22df_pattern : re.Pattern

    file_path = device + f'.txt'

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            






import re
class Utils:
    @staticmethod
    def remove_cpf_mask(cpf):
        numbers = ''
        numbers = ''.join(re.findall(r'\d', str(cpf)))
        return numbers
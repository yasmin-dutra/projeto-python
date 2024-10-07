from datetime import datetime

print('-'*77)
print('-'*31, 'DATA DE HOJE!', '-'*31)
print('-'*77)

hoje = datetime.now()

print(f'Data de hoje: {hoje:%d/%m/%y}')
print(f'Horário: {hoje:%H:%M %p}')

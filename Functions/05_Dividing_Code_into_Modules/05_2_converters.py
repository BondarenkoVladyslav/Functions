# Program główny testujący funkcje z modułu converters.
import converters

print('### Test funkcji przeliczających jednostki ###')
print(f'Trzy metry to {converters.m_to_cm(3)}cm')
print(f'250cm to {converters.cm_to_m(250)}m')
print(f'50cm to {converters.cm_to_inch(50):.2f} cali')
print(f'6 stóp i 2 cale to {converters.feet_inches_to_cm(6, 2):.2f}cm')
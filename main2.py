logi = (
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
    ('2020-12-10 09:07:58.075061', 'WARNING'),
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075060', 'WARNING'),
    ('2020-12-10 09:07:57.075064', 'WARNING'),
    ('2020-12-10 09:07:55.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:52.075064', 'ERROR'),
    ('2020-12-10 09:07:52.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075066', 'INFO'),
    ('2020-12-10 09:07:58.075066', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
    ('2020-12-10 09:07:58.075064', 'WARNING'),
)
# czyszecnie danych czyli duplikaty
clear_dane = []

for dane in logi:
    if dane not in clear_dane:
        clear_dane.append(dane)

def sprawdzanie_logow(dane, logi_do_spr):
    for log in logi_do_spr:
        if log not in dane:
            return False
    return True

logi_do_sprawdzenia = (
    ('2020-12-10 09:07:58.075064', 'INFO'),
    ('2020-12-10 09:07:58.075064', 'ERROR'),
)

print(sprawdzanie_logow(clear_dane, logi_do_sprawdzenia))

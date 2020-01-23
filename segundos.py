seg = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int(seg)

minutos = total_segs // 60
segs_restantes_final = total_segs % 60
horas = minutos // 60
minutos_restantes = minutos % 60
dias = horas // 24
hora_restante = horas %24
print (dias, "dias", hora_restante, "horas", minutos_restantes, "minutos e ", segs_restantes_final, "segundos.") 
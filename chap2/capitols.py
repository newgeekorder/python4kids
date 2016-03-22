
#  'Brazil' : 'Brasília',
captiols_sa = { 'Argentina' : 'Buenos Aires',
'Bolivia' : 'La Paz',
'Chile' : 'Santiago',
'Colombia' : 'Bogotá',
'Ecuador' : 'Quito',
'French Guiana (France)' : 'Cayenne (Préfecture)',
'Guyana' : 'Georgetown',
'Paraguay' : 'Asunción',
'Peru' : 'Lima',
'Suriname' : 'Paramaribo',
'Uruguay' : 'Montevideo',
'Venezuela' : 'Caracas'
}

print ("the captitol of Bolivia is " + captiols_sa['Bolivia'])

# change the capitol of Colombia
print ("the old capitol of Colombia is "  + captiols_sa["Colombia"])
captiols_sa["Colombia"] = "TracyTown"
print ("the new capitol of Colombia is " + captiols_sa["Colombia"])
print ("=======================")
# print all data
print ( captiols_sa )

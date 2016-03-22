print ("this provides an example of a python map .. it maps a key to a value")

#Brazil : Brasilia
captiols_sa = { 'Argentina' : 'Buenos Aires',
'Bolivia' : 'La Paz',
'Chile' : 'Santiago',
'Colombia' : 'Bogota',
'Ecuador' : 'Quito',
'French Guiana' : 'Cayenne',
'Guyana' : 'Georgetown',
'Paraguay' : 'Asuncion',
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
print ( "Our data", captiols_sa )
print ("We have " +  str( len(captiols_sa) ) +  " items in our map" )
# now delete one
del ( captiols_sa['Bolivia'])
print ("We now have " + str( len(captiols_sa) ) + " items in our map"  )

## for an exercise add a new country 




#Datos obtenidos de simulacion , teniendo en cuenta dos ejemplos

data1 = [
		[[-38.6999799615129, -72.56795282564521], [-38.69776942571914, -72.55975720755227], [-38.70523808268831, -72.5616452033433]], #C1
        [[-38.6999799615129, -72.56795282564521], [-38.70687907318969, -72.56885391454547], [-38.70523808268831, -72.5616452033433]], #C2
        [[-38.71016094120664, -72.5614735673623], [-38.70687907318969, -72.56885391454547], [-38.70523808268831, -72.5616452033433]]  #C3
        ]

data2 = [
		 [[-38.7007502836905, -72.56602192085892], [-38.69817134639991, -72.55422194716488], [-38.70694605159385, -72.55701103185619]], #C1
         [[-38.7007502836905, -72.56602192085892], [-38.71029489180327, -72.5688053041597], [-38.70694605159385, -72.55701103185619]],  #C2
         [[-38.713777519220855, -72.55790641936593], [-38.71029489180327, -72.5688053041597], [-38.70694605159385, -72.55701103185619]],#C3
         [[-38.70409941408546, -72.57786548288983], [-38.7007502836905, -72.56602192085892], [-38.70694605159385, -72.55701103185619]]  #C4
         ]

data = [
		[[-38.69807086644145, -72.56512083195864], [-38.69636268555, -72.55653903290843], [-38.70286025412059, -72.55872739166622]], 
		[[-38.69807086644145, -72.56512083195864], [-38.703295637095714, -72.56610773884941], [-38.70286025412059, -72.55872739166622]], 
		[[-38.69931010939652, -72.55186195242607], [-38.69636268555, -72.55653903290843], [-38.70286025412059, -72.55872739166622]], 
		[[-38.693750094689406, -72.56237552607382], [-38.69807086644145, -72.56512083195864], [-38.70286025412059, -72.55872739166622]]
		]









while (i < len(data)):

	fila = data[i]

	#Realiza la comparacion respecto al siguiente si existe 
	if(i+1 < len(data)):
		fila_sig = data[i+1]

		for coord in fila : 
			for coord_sig in fila_sig:
				if(coord == coord_sig):

					print("Estoy en %s y soy el vecino %s" %(i+1,i+2))


	i+=1






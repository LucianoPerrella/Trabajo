package sextoEjercicio;

import List.LinkedList;

public class TempMinEstacion {
	
	LinkedList <Float> lista;
	
	//----------Constructor----------
	
	public TempMinEstacion(int cantidadTemperaturas) {
		for(int i = 0;i < cantidadTemperaturas;i++) {
			if(i==0) {
			this.lista.addFirst(0f);
		}else {
			
			this.lista.addLast(0f);
		}
	}
		
		
		
	

}
	//----------Consultas----------
	public void establecerTempMin(int index, float elem) {
		
		 	lista.First();
		 	float aux = lista.getCurrent().se;
		 	for(int i = 0; i < index; i++) {
		 		lista.advance();
		 		aux = lista.getCurrent();
		 	}
		
		
	}
	
}

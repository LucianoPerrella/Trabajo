package sextoEjercicio;

import List.LinkedList;

public class Main {

	public static void main(String[] args) {
		
		TempMinEstacion estacion = new TempMinEstacion(5);
		estacion.establecerTempMin(0, 3f);
		estacion.establecerTempMin(1, 4f);
		
		estacion.establecerTempMin(2, 56f);
		estacion.establecerTempMin(3, 57f);
		estacion.establecerTempMin(4, -1f);
		System.out.println(estacion.primeroMayor(60f));
	}
	

}

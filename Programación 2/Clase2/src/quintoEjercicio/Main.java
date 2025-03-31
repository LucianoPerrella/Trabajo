package quintoEjercicio;

public class Main {

	public static void main(String[] args) {
		
		TemperaturasEstacion estacion1 = new TemperaturasEstacion(6);
		TemperaturasEstacion estacion2 = new TemperaturasEstacion(3);
//		estacion2.establecerTempMin(0, 32);
//		estacion2.establecerTempMin(1, 1);
//		estacion2.establecerTempMin(2, 37);
//		estacion2.establecerTempMin(3, 54);
//		estacion2.establecerTempMin(4, -6);
//		
		// TODO Auto-generated method stub
		estacion1.establecerTempMin(0, 1);
		estacion1.establecerTempMin(1, 102);
		estacion1.establecerTempMin(2, 37);
		estacion1.establecerTempMin(3, 4);
		estacion1.establecerTempMin(4, -6);
		estacion1.establecerTempMin(5, 32);
		
//		TemperaturasEstacion estacion3 = estacion1.invertir();
//		System.out.println(estacion1.menorTemperatura());
//		System.out.println(estacion1.posMenor());
//		System.out.println(estacion1.todosPositivos());
//		
//		System.out.println(estacion1.contarCoincidencias(estacion2));
		
//		for (int i = 0; i<estacion3.getListaTemperaturas().length;i++) {
//			
//			System.out.println(estacion3.getListaTemperaturas()[i]);
//		
//	}
		
//		estacion1.reemplazar(32, 5);
//		for (int i = 0; i < estacion1.getListaTemperaturas().length; i++) {
//			System.out.println(estacion1.getListaTemperaturas()[i]);
//		}
////		
//		estacion1.intercambiar(2, 4);
//		for (int i = 0; i < estacion1.getListaTemperaturas().length; i++) {
//			System.out.println(estacion1.getListaTemperaturas()[i]);
//		}
		
		estacion1.invertirMe();
		for (int i = 0; i < estacion1.getListaTemperaturas().length; i++) {
			System.out.println(estacion1.getListaTemperaturas()[i]);
		}
		

	}

}

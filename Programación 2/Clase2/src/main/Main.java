package main;

import primerEjercicio.CajaDeAhorro;
import segundoEjercicio.Flor;
import tercerEjercicio.*;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		--------------Ejercicio 1--------------
//		CajaDeAhorro primerCaja = new CajaDeAhorro(20);
//		CajaDeAhorro segundaCaja = new CajaDeAhorro();
//		
//		
//		System.out.println(primerCaja.getNumCaja());
//		System.out.println(segundaCaja.getNumCaja());
//		
//		System.out.println(primerCaja.getSaldo());
//		
//		primerCaja.setDeposito(20);
//		System.out.println(primerCaja.getSaldo());
//		
//		primerCaja.setExtraccion(50);
//		System.out.println(primerCaja.getSaldo());
		
		
//		--------------Ejercicio 2--------------
		
//		Flor primerFlor = new Flor();
//		System.out.println(primerFlor.getNombre());
//		System.out.println(primerFlor.getNumPetalos());
//		System.out.println(primerFlor.getPrecio());
//		
//		primerFlor.setNombre("Petunia");
//		primerFlor.setPrecio(50.0f);
//		primerFlor.setNumPetalos(25);
//		System.out.println(primerFlor.getNombre());
//		System.out.println(primerFlor.getNumPetalos());
//		System.out.println(primerFlor.getPrecio());

		
//		--------------Ejercicio 3--------------
		
//		Creación
		Jugador messi = new Jugador("Messi");
		Jugador ronaldo = new Jugador("Ronaldo");
		Jugador modric = new Jugador("Modric");
		
		Equipo chacarita = new Equipo("chacarita",messi);
		Equipo boca = new Equipo("Boca", ronaldo);
		Equipo racing = new Equipo("Racing", modric);
		
//		Partidos
		chacarita.incrementarPartidosGanados(false);
//		chacarita.incrementarPartidosGanados(true);
		chacarita.incrementarGolesAFavor(3,2);
		chacarita.incrementarPartidosEmpatados(true);
		chacarita.incrementarGolesAFavor(1, 1);
		chacarita.incrementarPartidosPerdidos(true);
		chacarita.incrementarGolesEnContra(7);
		
		boca.incrementarPartidosEmpatados(true);
		boca.incrementarGolesAFavor(5, 3);
		boca.incrementarPartidosPerdidos(true);
		boca.incrementarGolesEnContra(2);
		boca.incrementarPartidosGanados(true);
		boca.incrementarGolesAFavor(1, 1);
		
		racing.incrementarPartidosPerdidos(true);
		racing.incrementarGolesEnContra(2);
		racing.incrementarGolesAFavor(1, 1);
		racing.incrementarPartidosEmpatados(false);
		racing.incrementarGolesAFavor(1, 0);
		
		Jugador goleador = chacarita.jugadorConMasGoles(boca);
		System.out.println("El jugador con mas goles es: " + goleador.getNombre());
		
		
		
		
	}

}

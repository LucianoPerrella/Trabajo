package tercerEjercicio;

import java.util.Random;

public class Equipo {
	
//	En un campeonato de fútbol por cada partido ganado se obtienen 3 puntos y por cada
//	empate se logra 1. Cada equipo tiene un nombre, un capitán, una cantidad de partidos
//	ganados, otra de empatados y otra de perdidos, una cantidad de goles a favor y otra de
//	goles en contra. El capitán es un jugador que tiene un nombre, un año de nacimiento,
//	un número de camiseta, un número que representa la posición en la que juega, la
//	cantidad de partidos jugados y la cantidad de goles convertidos en el campeonato.
//	Para un jugador se desea calcular el promedio de goles de un jugador por partido y dado
//	otro jugador, cuál es el que hizo más goles. Para un equipo se desea calcular los partidos
//	jugados y los puntos obtenidos. Además, para otro equipo dado es necesario decidir cuál
//	es el equipo con mayor puntaje y cuál es el capitán con más goles. Si dos equipos tienen
//	los mismos puntos, se devuelve el que tiene mayor cantidad de goles a favor y si también
//	hay coincidencia se consideran los goles en contra. Si hay coincidencia se devuelve uno
//	cualquiera. 
//	
//	1. A partir del diagrama de clases en UML y la especificación de requerimientos
//	implemente dos clases en Java encapsulando atributos y comportamiento para
//	modelar la situación planteada. Incluya dentro del comportamiento los
//	comandos para modificar cada atributo y las consultas para devolver cada
//	atributo.
//	2. Elabore una clase que permita testear el modelo.
	
	private String nombre;
	private Jugador capitan;
	private int partidosGanados;
	private int partidosEmpatados;
	private int partidosPerdidos;
	private int golesAFavor;
	private int golesEnContra;
	
	//--------------Constructores--------------
	
	public Equipo(String nombre,Jugador capitan) {
		
	}
	
	//--------------Getter--------------
	public String getNombreCapitan() {
		return capitan.getNombre();
	}
	
	
	//--------------Comandos--------------
	
	public void incrementarPartidosGanados(boolean jugoElCapitan) {
		if (jugoElCapitan) {
			capitan.aumentarUnPartido();
			partidosGanados++;
		}else {
			partidosGanados++;
		}
	}
	
	public void incrementarPartidosEmpatados(boolean jugoElCapitan) {
		if(jugoElCapitan) {
			capitan.aumentarUnPartido();
			partidosEmpatados++;
		}else {
			partidosEmpatados++;}
		}
		
	public void incrementarPartidosPerdidos (boolean jugoElCapitan) {
		if(jugoElCapitan) {
			capitan.aumentarUnPartido();
			partidosPerdidos++;
		}else {
			partidosPerdidos++;
		}
		
	}
		
	public void incrementarGolesAFavor(int total, int golesDelCapitan) {
		if(golesDelCapitan > 0) {
			capitan.aumentarGoles(golesDelCapitan);
			golesAFavor += total;
		}else {
			golesAFavor += total;
		}
	}
		
	public void incrementarGolesEnContra(int total) {
		golesEnContra += total;
	}
		
	//--------------Consultas--------------
	
	public int partidos() {
		int totalPartidos = partidosEmpatados + partidosGanados + partidosPerdidos;
		return totalPartidos;
	}
		
	
    public int puntos() {
    	int totalPuntos = (partidosGanados * 3) + partidosEmpatados;
    	return totalPuntos;
    }
    
    public Equipo equipoMejorPuntaje(Equipo contrincante) {
    	if (this.puntos() > contrincante.puntos()) { //Si el primer equipo tiene mas puntos, se retorna
    		return this;
    	}else if (this.puntos() == contrincante.puntos()) {//En caso de que tengan la misma cantidad de puntos, se evaluan los goles a favor
    		if(this.golesAFavor > contrincante.golesAFavor) {//Si el primer equipo tiene mas goles a favor, se retorna
    			return this;
    		}else if(this.golesAFavor == contrincante.golesAFavor) {
    			if (this.golesEnContra < contrincante.golesEnContra) {
    				return this;
    			}else if(this.golesEnContra == contrincante.golesEnContra) {//Si coinciden tanto en goles a favor como goles en contra, se devuelve uno al azar
    				 Random rand = new Random();
    			     int numeroAleatorio = rand.nextInt(2) + 1;
    			     if (numeroAleatorio == 1) {
    			    	 return this;
    			     } else {
    			    	 return contrincante;
    			     }
    			}else {
    				return contrincante;
    			}
    		}else {
    			return contrincante;
    		}
    	
    	}else {
    		return contrincante;
    	}
    }
	
    public Jugador jugadorConMasGoles(Equipo contrincante) {
    	if (capitan.jugadorConMasGoles(contrincante.capitan)) {
    		return this.capitan;
    	}else {
    		return contrincante.capitan;
    	}
    	
    }
	
	
}


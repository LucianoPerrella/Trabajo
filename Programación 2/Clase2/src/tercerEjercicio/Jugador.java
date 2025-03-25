package tercerEjercicio;

public class Jugador {
	
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
	private int nroCamiseta;
	private int posicion;
	private int golesConvertidos;
	private int partidosJugados;
	
	//--------------Constructores--------------
	
	public Jugador(String nombre) {
		this.nombre = nombre;
		
	}
	
	//--------------Getter--------------
    public String getNombre() {
    	return nombre;
    }
	
	
	//--------------Comandos--------------
	
	public void aumentarGoles(int goles) {
		golesConvertidos += goles;
	}
	
	public void aumentarUnPartido() {
		partidosJugados++;
	}
	
	//--------------Consultas--------------
	
	public int promedioGolesPartido() {
		int promedio = golesConvertidos / partidosJugados;
		return promedio;
	}
	
	public boolean jugadorConMasGoles(Jugador jugador) {
		if (this.golesConvertidos > jugador.golesConvertidos) {
			return true;
		}else {
			return false;
		}
	}


}

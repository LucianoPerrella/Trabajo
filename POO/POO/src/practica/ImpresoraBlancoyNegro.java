package practica;

public class ImpresoraBlancoyNegro extends Impresora {
	private float cantidadTinta;
	private int cantidadHojas;
	private int contadorImpresiones;
	
//	---------Constructor---------
	public ImpresoraBlancoyNegro() {
		
	}
	
	public ImpresoraBlancoyNegro(float cantidaTinta, int cantidadHojas) {
		this.cantidadHojas = cantidadHojas;
		this.cantidadTinta = cantidaTinta;
	}
	
//	---------Getters---------

	public float getCantidadTinta() {
		return cantidadTinta;
	}

	
	public int getCantidadHojas() {
		return cantidadHojas;
	}

	
	
//	---------Setters---------
	
	
	
	public void setCantidadHojas(int cantidadHojas) {
		this.cantidadHojas = cantidadHojas;
	}
	
	public void setCantidadTinta(float cantidadTinta) {
		this.cantidadTinta = cantidadTinta;
	}

//	---------Métodos---------
	
	@Override
	private boolean puedeImprimir(Documento docu) {
		
	}

}

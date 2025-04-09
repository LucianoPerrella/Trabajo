package practica;

public class Documento {
	private int cantidadPaginas;
	private float consumoCian;
	private float consumoMagenta;
	private float consumoAmarillo;
	private float consumoNegro;
	private boolean fueImpreso = false;
	
	
//	---------Constructor---------
	public Documento() {
		
	}
	
	public Documento(int cantidadPaginas, float consumoCian, 
			float consumoMagenta, float consumoAmarillo, float consumoNegro, boolean fueImpreso) {
		this.cantidadPaginas = cantidadPaginas;
		this.consumoAmarillo = consumoAmarillo;
		this.consumoCian = consumoCian;
		this.consumoNegro = consumoNegro;
		this.fueImpreso = fueImpreso;
	}
	
	
//	---------Getters---------
	public int getCantidadPaginas() {
		return cantidadPaginas;
	}

	public float getConsumoCian() {
		return consumoCian;
	}

	public float getConsumoMagenta() {
		return consumoMagenta;
	}

	public float getConsumoAmarillo() {
		return consumoAmarillo;
	}

	public float getConsumoNegro() {
		return consumoNegro;
	}

	public boolean isFueImpreso() {
		return fueImpreso;
	}


	
	
	
//	---------Setters---------
public void setCantidadPaginas(int cantidadPaginas) {
	this.cantidadPaginas = cantidadPaginas;
}

public void setConsumoCian(float consumoCian) {
	this.consumoCian = consumoCian;
}

public void setConsumoMagenta(float consumoMagenta) {
	this.consumoMagenta = consumoMagenta;
}

public void setConsumoAmarillo(float consumoAmarillo) {
	this.consumoAmarillo = consumoAmarillo;
}

public void setConsumoNegro(float consumoNegro) {
	this.consumoNegro = consumoNegro;
}

public void setFueImpreso(boolean fueImpreso) {
	this.fueImpreso = fueImpreso;
}


	
	
//	---------Métodos---------
	public boolean seImprimio() {
		return this.fueImpreso;
	}
	
}

	
	
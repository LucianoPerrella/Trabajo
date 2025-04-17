package practica;

public class Impresora {
	private int cantidadHojas;
	private float porcentajeCian;
	private float porcentajeMagenta;
	private float porcentajeAmarillo;
	private float porcentajeNegro;
	
	
//	---------Constructor---------
	public Impresora() {
	
	}

	public Impresora(int cantidadHojas, float porcentajeCian, float porcentajeMagenta
			,float porcentajeAmarillo, float porcentajeNegro) {
		
		this.cantidadHojas = cantidadHojas;
		this.porcentajeCian = porcentajeCian;
		this.porcentajeMagenta = porcentajeMagenta;
		this.porcentajeAmarillo = porcentajeAmarillo;
		this.porcentajeNegro = porcentajeNegro;
	}
	
	
//	---------Getters---------
	public int getCantidadHojas() {
		return cantidadHojas;
	}

	public float getPorcentajeCian() {
		return porcentajeCian;
	}

	public float getPorcentajeMagenta() {
		return porcentajeMagenta;
	}

	public float getPorcentajeAmarillo() {
		return porcentajeAmarillo;
	}

	public float getPorcentajeNegro() {
		return porcentajeNegro;
	}
	
//	---------Setters---------
	public void setCantidadHojas(int cantidadHojas) {
		this.cantidadHojas = cantidadHojas;
	}

	public void setPorcentajeCian(float porcentajeCian) {
		this.porcentajeCian = porcentajeCian;
	}

	public void setPorcentajeMagenta(float porcentajeMagenta) {
		this.porcentajeMagenta = porcentajeMagenta;
	}

	public void setPorcentajeAmarillo(float porcentajeAmarillo) {
		this.porcentajeAmarillo = porcentajeAmarillo;
	}

	public void setPorcentajeNegro(float porcentajeNegro) {
		this.porcentajeNegro = porcentajeNegro;
	}
	
	
	
	
//	---------Métodos---------
	protected boolean puedeImprimir(Documento docu) {
		return meAlcanzanLasHojas(docu)
				&& meAlcanzanLasTinta(docu);
	
	}
	
	protected boolean meAlcanzanLasHojas(Documento docu) {
		return this.getCantidadHojas() >= docu.getCantidadPaginas();
	}
	
	
	
	
	protected boolean meAlcanzanLasTinta(Documento docu) {
		return docu.getConsumoAmarillo() <= this.getPorcentajeAmarillo()
				&& docu.getConsumoCian() <= this.getPorcentajeCian()
				&& docu.getConsumoMagenta() <= this.getPorcentajeMagenta()
				&& docu.getConsumoNegro() <= this.getPorcentajeNegro();
		
	}
	
	

	

	public Documento imprimirDocumento(Documento docu) {
		
		if (this.puedeImprimir(docu)) {
			this.setCantidadHojas(getCantidadHojas() - docu.getCantidadPaginas()); 
			this.setPorcentajeAmarillo(getPorcentajeAmarillo() - docu.getConsumoAmarillo()); 
			this.setPorcentajeCian(getPorcentajeCian() - docu.getConsumoCian());
			this.setPorcentajeMagenta(getPorcentajeMagenta() - docu.getConsumoMagenta());
			this.setPorcentajeNegro(getPorcentajeNegro() - docu.getConsumoNegro()); 
			docu.setFueImpreso(true);}
			
		
		return docu;
	}
	
	public void recargarTintas() {
		this.setPorcentajeAmarillo(100);
		this.setPorcentajeCian(100);
		this.setPorcentajeMagenta(100);
		this.setPorcentajeNegro(100);
	}
	
	public void recargarHojas(int cuantas) {
		this.setCantidadHojas(cuantas);
	}
}

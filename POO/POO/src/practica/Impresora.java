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
	private boolean puedeImprimir(Documento docu) {
		return docu.getCantidadPaginas() <= this.cantidadHojas
				&& docu.getConsumoAmarillo() <= this.getPorcentajeAmarillo()
				&& docu.getConsumoCian() <= this.getPorcentajeCian()
				&& docu.getConsumoMagenta() <= this.getPorcentajeMagenta()
				&& docu.getConsumoNegro() <= this.getPorcentajeNegro();
	
	}
	
	

	

	public Documento imprimirDocumento(Documento docu) {
		boolean sePuede = this.puedeImprimir(docu);
		if (sePuede) {
			this.setCantidadHojas(getCantidadHojas() - docu.getCantidadPaginas()); 
			this.setPorcentajeAmarillo(getPorcentajeAmarillo() - docu.getConsumoAmarillo()); 
			this.setPorcentajeCian(getPorcentajeCian() - docu.getConsumoCian());
			this.setPorcentajeMagenta(getPorcentajeMagenta() - docu.getConsumoMagenta());
			this.setPorcentajeNegro(getPorcentajeNegro() - docu.getConsumoNegro()); 
			docu.setFueImpreso(true);
			System.out.println("Imprimiendo amigo");
			
		}else {
			System.out.println("No hay recursos querido, recargame");
		}
		return docu;
	}
	

}

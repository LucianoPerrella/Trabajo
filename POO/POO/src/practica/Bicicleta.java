package practica;

public class Bicicleta {
	
	private String color;
	private int anioDeFabricacion;
	private String materialDeFabricacion;
	private int peso;
	private boolean cadenaAceitada = false;
	private boolean pataActivada = true;
	
	
	
	//-----------Constructores-----------
	
	public Bicicleta() {
		
	}
	
	public Bicicleta(String color, int anioDeFabricacion, String materialDeFabricacion, int peso, boolean cadenaAceitada, boolean pataActivada) {
		this.color = color;
		this.anioDeFabricacion = anioDeFabricacion;
		this.materialDeFabricacion = materialDeFabricacion;
		this.peso = peso;
		this.cadenaAceitada = cadenaAceitada;
		this.pataActivada = pataActivada;
	}
	
	
	
	//-----------Getters-----------
	

	
	public String getColor() {
		return color;
	}


	public int getAnioDeFabricacion() {
		return anioDeFabricacion;
	}


	public String getMaterialDeFabricacion() {
		return materialDeFabricacion;
	}


	public int getPeso() {
		return peso;
	}


	public boolean isCadenaAceitada() {
		return cadenaAceitada;
	}
	
	public boolean getPataTrabada () {
		return pataActivada;
	}


	
	//-----------Setters-----------
	
	public void setColor(String color) {
		this.color = color;
	}


	public void setAnioDeFabricacion(int anioDeFabricacion) {
		this.anioDeFabricacion = anioDeFabricacion;
	}


	public void setMaterialDeFabricacion(String materialDeFabricacion) {
		this.materialDeFabricacion = materialDeFabricacion;
	}


	public void setPeso(int peso) {
		this.peso = peso;
	}
	
	public void setCadenaAceitada (boolean aceitada) {
		this.cadenaAceitada = aceitada;
	}
	
	public void destrabarPata () {
		this.pataActivada = false;
	}
	
	public void trabarPata() {
		this.pataActivada = true;
	}



	
	
	
	//-----------Métodos----------- 	
	
	public void arrancar() {
		boolean pataActiva = this.getPataTrabada();
		if (pataActiva) {
			System.out.println("Probá sacando la pata que traba.");
		} else {
			System.out.println("Andando ando");
		}
		this.destrabarPata();
	}
	
	public void estacionar() {
		boolean pataActiva = this.getPataTrabada();
		if (!pataActiva) {
			System.out.println("Probá activando la pata");
		} else {
			System.out.println("Estacionando ando");
		}
		this.trabarPata();
	}
	
}
	 
	

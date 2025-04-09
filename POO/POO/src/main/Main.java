package main;

import practica.Bicicleta;
import practica.Documento;
import practica.Impresora;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
//		Bicicleta bici = new Bicicleta();
//		bici.arrancar();
//		bici.destrabarPata();
//		bici.arrancar();
//		bici.estacionar();
//		bici.trabarPata();
//		bici.estacionar();
//		public static void main(String[] args) {
        // Crear una impresora con recursos iniciales
        Impresora impresora = new Impresora(
                15,     // hojas disponibles
                40.0f,  // porcentaje cian
                40.0f,  // porcentaje magenta
                40.0f,  // porcentaje amarillo
                40.0f   // porcentaje negro
        );

        // Crear un documento que SÍ puede imprimirse
        Documento doc1 = new Documento();
        doc1.setCantidadPaginas(5);
        doc1.setConsumoCian(5.0f);
        doc1.setConsumoMagenta(3.0f);
        doc1.setConsumoAmarillo(4.0f);
        doc1.setConsumoNegro(6.0f);
        mostrarEstadoImpresora(impresora);

        System.out.println("Intentando imprimir doc1...");
        impresora.imprimirDocumento(doc1);
        System.out.println("¿Fue impreso doc1? " + doc1.seImprimio());
        mostrarEstadoImpresora(impresora);

        // Crear un documento que NO puede imprimirse (no hay tinta suficiente)
        Documento doc2 = new Documento();
        doc2.setCantidadPaginas(10);
        doc2.setConsumoCian(50.0f);  // más de lo que queda
        doc2.setConsumoMagenta(5.0f);
        doc2.setConsumoAmarillo(5.0f);
        doc2.setConsumoNegro(5.0f);

        System.out.println("\nIntentando imprimir doc2...");
        impresora.imprimirDocumento(doc2);
        System.out.println("¿Fue impreso doc2? " + doc2.seImprimio());
        mostrarEstadoImpresora(impresora);
    }

    public static void mostrarEstadoImpresora(Impresora impresora) {
        System.out.println("----- Estado de la impresora -----");
        System.out.println("Hojas restantes: " + impresora.getCantidadHojas());
        System.out.println("Cian: " + impresora.getPorcentajeCian() + "%");
        System.out.println("Magenta: " + impresora.getPorcentajeMagenta() + "%");
        System.out.println("Amarillo: " + impresora.getPorcentajeAmarillo() + "%");
        System.out.println("Negro: " + impresora.getPorcentajeNegro() + "%");
        System.out.println("----------------------------------");
    }
	}



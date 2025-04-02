package clases;

import interfaces.InterfaceQueue;

public class Queue<Elemento> implements InterfaceQueue<Elemento> {
	private int f;
	private int r;
	private int size;
	private Elemento[] q;
	
	
	//-----------Constructor-----------
	
	public Queue(int tamanio) {
		f=0;
		r=0;
		size=0;
		q = (Elemento[])new Object[tamanio];
		
	}

	@Override
	public void enqueue(Elemento elemento) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public Elemento dequeue() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Elemento front() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean isEmpty() {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public int size() {
		// TODO Auto-generated method stub
		return 0;
	}

	
}

package clases;

import interfaces.InterfaceDictionary;

public class LinkedDictionary<K,V> implements InterfaceDictionary<K,V> {
	private DNode<Entry<K,LinkedList<V>>> head;
	private DNode<Entry<K,LinkedList<V>>> tail;
	private int size;

//	----------Constructor----------
	public LinkedDictionary() {
		head = null;
		tail = null;
		size = 0;
	}
	

	@Override
	public int size() {
		return size;
	}

	@Override
	public boolean isEmpty() {
		return size == 0;
	}

	@Override
	public Iterable<V> get(K k) {
		if(size == 0) {
			return null;
		}
		DNode<Entry<K,LinkedList<V>>> actual = head;
		while(actual != null && actual.getElement().getKey() != k) {
			actual = actual.getNext();
		}
		if(actual != null) {
			LinkedList<V> listaValores = actual.getElement().getValue();
			LinkedList<V> copia = new LinkedList<V>();
			listaValores.First();
			while(!listaValores.atEnd()) {
				copia.addLast(listaValores.getCurrent());
				listaValores.advance();
			}
			return copia;
		}
		else {
			return null;
		}
	}

	@Override
	public void put(K k, V v) {
		if (size == 0) {
			LinkedList<V> listaValores = new LinkedList<V>();
			listaValores.addFirst(v);
			
		}
		
	}

	@Override
	public Iterable<V> remove(K k) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public V remove(K k, V v) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Iterable<K> keys() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Iterable<Entry<K, Iterable<V>>> entries() {
		// TODO Auto-generated method stub
		return null;
	}

}

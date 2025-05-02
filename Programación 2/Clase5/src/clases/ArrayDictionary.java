package clases;

import interfaces.InterfaceDictionary;

public class ArrayDictionary<K,V> implements InterfaceDictionary<K,V>{
	
	private Entry<K,V[]>[] array;
	private int size;
	
//	----------Constructor----------
	public ArrayDictionary() {
		array = (Entry<K,V[]>[]) new Object[100];
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
	
}

@Override
public void put(K k, V v) {
	// TODO Auto-generated method stub
	
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

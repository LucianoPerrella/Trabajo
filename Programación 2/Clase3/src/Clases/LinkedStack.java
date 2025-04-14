package Clases;

import Excepciones.MyException;
import Interfaces.Stack;

public class LinkedStack<T> implements Stack<T> {
	private Node<T> top;
	private int size;

	@Override
	public void push(T item) {
		Node<T> nodo = new Node<T>(item,top);
		top = nodo;
		size++;
	}

	@Override
	public T pop() throws MyException {
		if(top == null) {
			throw new MyException("La lista está vacía.");
		}
		Node<T> nodoAEliminar = top;
		T ultimoElemento = nodoAEliminar.getElement();
		
		top = top.getNext();
		nodoAEliminar.setNext(null);
		size--;
		return ultimoElemento;
	}

	@Override
	public T top() throws MyException {
		if(top == null) {
			throw new MyException("La lista está vacía");
		}
		return top.getElement();
	}

	@Override
	public boolean isEmpty() {
		return size == 0;
	}

	@Override
	public int size() {
		return size;
	}

}

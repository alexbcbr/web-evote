package com.chaosengineering.thread;

//Example extracted https://blog.ycrash.io/category/chaos-engineering/

public class ThreadLeakDemo {
	public static void start() {

		while (true) {

			new ForeverThread().start();
		}
	}
	
	public static void main(String[] args) {
		ThreadLeakDemo a = new ThreadLeakDemo();
		a.start();
	}
}

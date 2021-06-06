package com.chaosengineering.thread;

public class ForeverThread extends Thread {

	@Override
	public void run() {

		// Put the thread to sleep forever, so they don't die.
		while (true) {

			try {

				// Sleeping for 10 minutes repeatedly
				Thread.sleep(10 * 60 * 1000);
			} catch (Exception e) {}
		}
	}
}


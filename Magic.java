//Yining Hua

// Objective: write a Java program that reads in a yes/no question 
//from the user and returns a random prediction.

import java.util.Scanner;
import random;

public class Magic {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);  // Reading from System.in
		System.out.println("Question: ");
		String question = reader.nextInt(); // Scans the next token of the input as an int.
		Random n = new Random();
		reader.close();
		if(n%2) {
		System.out.println("No");
		}else {
		println("Yes");
		}
    }

}

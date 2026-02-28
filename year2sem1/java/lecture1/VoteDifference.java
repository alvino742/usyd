import java.util.Scanner;

public class VoteDifference{
    public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String input1 = sc.nextLine();
		String input2 = sc.nextLine();
		int n1 = 0;
		int n2 = 0;
		try {
			n1 = Integer.parseInt(input1);
			n2 = Integer.parseInt(input2);
		} catch(NumberFormatException e) {
			System.out.println("Bad input");
			return;
		}


		
		if (n1 > 0 && n2 > 0){
			if (n1 == n2) {
				System.out.println("The poll is a tie");
			}
			if (n1 > n2) {
				int difference = n1 - n2;
				System.out.printf("The poll is won by %d votes\n", difference);
			}
			if (n1 < n2) {
				int difference = n2 - n1;
				System.out.printf("The poll is won by %d votes\n", difference);
			}
		} else {
				System.out.println("Bad input");
		}
    }
}

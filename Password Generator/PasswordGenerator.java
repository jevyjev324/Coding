import java.util.Scanner;

public class PasswordGenerator
{
	public static Scanner scan = new Scanner(System.in);
	
	public static void main(String[] args)
	{
		int choice = 0;
		boolean finished = false;
		
		while(!finished)
		{
			String input = "";
			
			System.out.println("\n-----------------------------");
			System.out.println("|  Password Generator Menu  |" +
										"\n-----------------------------" +
										"\n\t1. Random Password" +
										"\n\t2. Strengthen Phrase" +
										"\n\t3. Quit");
			
			System.out.print("\nPlease choose from the menu: ");
			choice = scan.nextInt();
			
			while(choice <= 0 || choice > 3)
			{
				System.out.print("Please choose from the menu: ");
				choice = scan.nextInt();
			}
			
			scan.nextLine(); //Consumes the \n left from the nextInt

			switch(choice)
			{
				case 1:
				{
					RandomPassword();
					break;
				}
				case 2:
				{
					StrengthenPhrase();
					break;
				}
				case 3:
				{
					System.exit(0);
					break;
				}
			}
										
			System.out.print("\nDo you want to generate another password (Y or N): ");
			input = scan.nextLine();
		
			if(input.charAt(0) == 'N' || input.charAt(0) == 'n')
				finished = true;
		}
	}
	
	public static void RandomPassword()
	{
		System.out.println("How many characters does your password need? ");
		
		//Choose a length 
		//Create a rand variable to randomly select letters and change letters to symbol and nums
	}
	
	public static void StrengthenPhrase()
	{
		String input = "";
		char[] passArray;
		
		System.out.println("\n-------------------------------" +
									"\n|  Passphrase Strengthener  |" +
										"\n-------------------------------");
		System.out.print("\nPlease enter a phrase to be strengthend: ");
		input = scan.nextLine();
		
		System.out.print("\nThe phrase you entered: " + input);
		
		passArray = input.toCharArray();
		
		if(passArray.length == 0)
		{
			System.out.println("Passphrase is empty");
			return;
		}
		
		passArray = typeOfSpace(addSymbols(addNumbers(passArray)));
		
		System.out.println("Your strengthend passphrase is: " + String.valueOf(passArray));
		
		System.out.println();
	}
		
	public static char[] addNumbers(char[] pass)
	{
		for(int i = 0; i < pass.length; i++)
		{
			switch(pass[i])
			{
				case 'O':
				case 'o':
					pass[i] = '0';
					break;
				case 'l':
				case 'L':
					pass[i] = '1';
					break;
				case 'E':
				case 'e':
					pass[i] = '3';
					break;
				case 'H':
				case 'h':
					pass[i] = '4';
					break;
				case 'r':
				case 'R':
					pass[i] = '7';
					break;				
			}
		}
		return pass;
	}
	
	public static char[] addSymbols(char[] pass)
	{
		for(int i = 0; i < pass.length; i++)
		{
			switch(pass[i])
			{
				case 'i':
				case 'I':
					pass[i] = '!';
					break;
				case 'A':
				case 'a':
					pass[i] = '@';
					break;
				case 's':
				case 'S':
					pass[i] = '$';
					break;
				case 'n':
				case 'N':
					pass[i] = '^';
					break;
			}
		}
		return pass;
	}
	
	public static char[] typeOfSpace(char[] pass)
	{
		int choice = 0;
		System.out.println("\nPlease choose your spacing character: "+
									"\n\t1. \'#\'" +
									"\n\t2. \'%\'" +
									"\n\t3. \'&\'" +
									"\n\t4. \'*\'" +
									"\n\t5. \'_\'" +
									"\n\t6. \'=\'");
									
		System.out.print("\nPlease choose from the menu: ");
		choice = scan.nextInt();
			
			while(choice <= 0 || choice > 6)
			{
				System.out.print("Please choose from the menu: ");
				choice = scan.nextInt();
			}
			
		for(int i = 0; i < pass.length; i++)
		{
			if(pass[i] == ' ')
			{
				switch(choice)
				{
					case 1:
						pass[i] = '#';
						break;
					case 2:
						pass[i] = '%';
						break;
					case 3:
						pass[i] = '&';
						break;
					case 4:
						pass[i] = '*';
						break;
					case 5:
						pass[i] = '_';
						break;
					case 6:
						pass[i] = '=';
						break;
				}
			}
		}
		scan.nextLine();
		return pass;
	}
 
}
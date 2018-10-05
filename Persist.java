class Persist {
	public static int persistence(long n) {
		// your code
    
    int index = 0, length = 0, o = 1;
	String sNum = String.valueOf(n);
	length = sNum.length();
	
     if(length == 1)
      return 0;
    else
	{
		while(length > 1)
		{
			o=1;
			index++;
			int[] k = new int[sNum.length()];
			for(int i = 0; i < k.length;i++)
			{
				k[i] = sNum.charAt(i) - '0';
			}
			for(int i = 0; i < k.length;i++)
				o *= k[i];
			
			sNum = String.valueOf(o);
			length = sNum.length();
		}
	}
      return index;
    
	}
	public static void main(String[] args)
	{
		System.out.println("m-"+persistence(39));
		System.out.println("m-"+persistence(4));
	}
}
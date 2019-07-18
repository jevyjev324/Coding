public class EvenArray {
	public static void main(String[] args)
	{
		int[] arr = {1,2,3,4,3,2,1};
		
		System.out.println("Index = " + findEvenIndex(arr));
	}
  public static int findEvenIndex(int[] arr) {
    // your code
    
    int sumL = 0, sumR = 0;
    
    for(int index = 0; index < arr.length; index++)
    {
		sumL = sumR = 0;
		System.out.print("\nSumL:");
      if(index == 0)
      {  
        sumL = 0; 
		System.out.print(sumL+",");
      }
      else 
      {
        for(int i = 0; i < index; i++)
        {
          sumL += arr[i];
		  System.out.print(sumL +",");
        }
      }
      System.out.print("\nSumR:");
      if(index+1 == arr.length)
	  {
        sumR = 0;
		System.out.print(sumR+",");
	  }
      else
	  {
		  for(int j = index+1; j < arr.length; j++)
        {
          sumR += arr[j];
		  System.out.print(sumR+",");
        }
	  }
        System.out.println(sumL + " " + sumR);
      if(sumR == sumL)
      {
        return index;
      }
    }
    return -1;
  }
}

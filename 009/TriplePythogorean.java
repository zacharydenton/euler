public class TriplePythogorean {
	public static void main(String[] args) {
	    for (int a=1;a<=1000/2;a++)
	    {
	        int b=0;
	        for (b=a+1;b<=1000/2;b++)
	        {
	            int c=1000-b-a;
	            if (c*c==a*a+b*b)
	               System.out.println(a*b*c);
	        }
	    }

	}
}

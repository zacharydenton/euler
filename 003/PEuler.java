public class PEuler2{

     public static void main(String []args){
     	
        long number =600851475143L;
        long i=2L;
        for(;i<number;i++){
            if(number%i==0&&isPrime(number/i))
                break;
        }
		System.out.println(number/i);
	}
  
	public static boolean isPrime(long n){
	    
	    for(int i=2;i<Math.sqrt(n);i++)
	        if(n%i==0)
	            return false;
	   return true;
	    
	}
}

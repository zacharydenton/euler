import java.math.*;
public class SumOfPrimes {
	public static boolean  isPrime(long number) {
		long sqr=(long)Math.sqrt(number);
		for(long i=2;i<=sqr;i++) {
			if (number%i==0) {
				return false;
			}
			
		}
		return true;
	}
	public static void main(String[] args) {
		long limit=2000000;
		long sum=0;
		for(long i=2;i<limit;i++) {
			if (i==2) {
				sum+=i;
			}else if(isPrime(i)) {
				sum+=i;
			}
		}
		System.out.println(sum);
	}
}

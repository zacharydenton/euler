import java.math.*;
public class PrimeOFThousand {
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
		long count=0;
		for(long i=2;;i++) {
			if (i==2) {
				count+=1;
			}else if(isPrime(i)) {
				count+=1;
			}
			if (count==10001) {
				System.out.println(i);
				break;

			}
		}
	}
}

import java.math.*;
public class TriangleDivisors {
	public static long  numberOfDivisors(long number) {
		long count=0;
		for (long i=1;i<(number/2)+1;i++) {
			if (number%i==0) {
				count++;
			}
		}
		return count;
	}
	public static long triangleNumber(long number) {
		long sum=0;
		for (long a=1;a<=number;a++) {
			sum+=a;
		}
		return sum;
	}
	public static void main(String[] args) {
		long sum=0;
		for(long i=2;;i++) {
			long a=triangleNumber(i);
			long temp=numberOfDivisors(a);
			if (temp>=500) {
				sum=i;
				System.out.println(sum);
				System.exit(0);
			}
		}
	}
}

public class PEuler6{

    public static void main(String []args){
        int sumSquares=0, squareSum=0;
 	
        for(int i = 1; i <= 100; i++ ){
            sumSquares += i * i;
            squareSum += i;
        }

        squareSum *= squareSum;
        System.out.println(squareSum - sumSquares);
	    
	}
}

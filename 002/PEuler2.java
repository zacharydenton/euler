public class PEuler2{

    public static void main(String []args){
        int pre=1,post=1,sum=0 ;

        while (post<=4000000){
            if(post%2==0)
                sum+=post;
            post=pre+post;
            pre=post-pre;
        }
        System.out.println(sum);
	    
	}
}

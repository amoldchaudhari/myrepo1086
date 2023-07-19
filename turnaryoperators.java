// if ((a > b) && (a > c)) {
//             greatestNum = a;
//         }else if((b>a) && (b>c)){
//              greatestNum = b;
//         }else{
//              greatestNum = c;
//         }
public class turnaryoperators{
    public static void main(String[] args) {
        int numOne = 45;
        int numTwo = 20;
        int numThree = 25;
        int gretestNo = (numOne < numTwo) ? numTwo : numOne;
        int gretestNum = (gretestNo < numThree) ? numThree : gretestNo;
        System.out.println("the gretest number is : " + gretestNum);

    }
}
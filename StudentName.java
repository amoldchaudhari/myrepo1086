import java.util.Scanner;


public class StudentName {
    public static void main(String[] args) {
        String [] studentName = new String[3];
        Scanner sc = new Scanner(System.in);
        int index = 0;
        while(index < studentName.length){
        System.out.print("enter the student name : " + index);
        studentName[index] = sc.nextLine();
// id name and Marks
// take int array for multipal no find out small and average and acending order
        index++;
        
        }
        for (index=0;index<studentName.length;index++){
        System.out.println("Student Name  " + studentName[index] );
        }  
        sc.close();
        }
    
}


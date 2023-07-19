public class numSwap {
    public static void main(String[] args) {
        int[] newArray = {8,2,6,5,};
        System.out.println("number in assry before sorting");
        
        for (int i = 0 ; i< newArray.length; i++){
              System.out.println(newArray[i]);
        }
        for (int i = 0;i<newArray.length; i++){
            for (int j = 0; j< newArray.length; j++){
                if (newArray[i] > newArray[j]){
                    int temp = newArray[i];
                    newArray[i] = newArray [j];
                    newArray[j]= temp;
                }
            }
        }
        for (int i = 0; i < newArray.length; i++){
            System.out.println(newArray[i]);
        }

        
    }
    
}

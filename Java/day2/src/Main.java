import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;


public class Main {
    public static void main(String[] args) {
        FileOps fileOps = new FileOps();

        ArrayList<String> data = fileOps.read("day2\\src\\input.txt");

        Integer total = 0;
        
        for (String d : data) {
            ArrayList<String> splited = new ArrayList<>(Arrays.asList(d.split(" ")));
            ArrayList<Integer> toIntegers = splited.stream().map(Integer::parseInt).collect(Collectors.toCollection(ArrayList::new));

            if (check(toIntegers)){
                total += 1;
            } 
            //Part 2
            else {
                boolean valid = false;
                int index = 0;
                while (index < toIntegers.size() && !valid){ 
                    ArrayList<Integer> temp = new ArrayList<>(toIntegers);
                    temp.remove(index);

                    if (check(temp)){
                        valid = true;
                    }

                    index += 1;
                }
                if (valid) {
                    total += 1;
                }

            }
            //End 
        }
        System.out.println(total);

    }

    public static boolean check(ArrayList<Integer> array) {
        boolean valid = true;
        boolean increasing = array.get(0) < array.get(1);
        int index = 0;
        while (index < array.size()-1 && valid){

            int delta = array.get(index+1) - array.get(index);
            if (! ((increasing && delta >= 1 && delta <= 3) || (!increasing && delta <= -1 && delta >= -3))) {
                valid = false;
            }
            
            index += 1;
        }

        return valid;
    } 
}

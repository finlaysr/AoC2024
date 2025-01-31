import java.util.ArrayList;
import java.util.Collections;

public class Main {
    
    public static void main(String[] args) {
        FileOps fileOps = new FileOps();

        ArrayList<String> data = fileOps.read("day1\\src\\input.txt");
        //System.out.println(data);

        ArrayList<Integer> line1 = new ArrayList<>();
        ArrayList<Integer> line2 = new ArrayList<>();

        for (String i : data) {
            String[] temp = i.split("   ");
            line1.add(Integer.parseInt(temp[0]));
            line2.add(Integer.parseInt(temp[1]));
        }
        line1.sort(null);
        line2.sort(null);


        Integer total = 0;
        for (int i = 0; i < line1.size(); i++) {
            Integer d = line1.get(i) - line2.get(i);
            if (d < 0) {
                total -= d;
            } else {
                total += d;
            }
        }

        System.out.println("Part 1: " + total);
        
        //Part 2
        total = 0;
        for (Integer i : line1) {
            total += i * Collections.frequency(line2, i);
        }

        System.out.println("Part 2: " + total);

    }

}


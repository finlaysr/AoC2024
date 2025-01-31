import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        FileOps fileOps = new FileOps();
        String data = fileOps.read(".\\day3\\src\\input.txt").toString();
        //System.out.println(data);
           
        final String regex = "mul\\([0-9]{1,3},[0-9]{1,3}\\)";
        
        final Pattern pattern = Pattern.compile(regex, Pattern.MULTILINE);
        final Matcher matcher = pattern.matcher(data);

        ArrayList<String> matches = new ArrayList<>();
        
        while (matcher.find()) {
            matches.add(matcher.group(0));
        }
        //System.out.println(matches);

        int total = 0;

        
        for (String m : matches) {
            ArrayList<Integer> nums = new ArrayList<>();
            nums.add(Integer.parseInt(m.substring(m.indexOf("(", 0)+1, m.indexOf(",", 0))));
            nums.add(Integer.parseInt(m.substring(m.indexOf(",", 0)+1, m.indexOf(")", 0))));
            //System.out.println(nums);
            total += nums.get(0) * nums.get(1);
        }
        System.out.println(total);

        String s = "mul(1,2)";
        s.length();
        s.charAt(total);

       

    }

    public Map<String, String> pairs(String[] strings) {
        Map<String, String> map = new HashMap<String, String>();
        for (String s : strings) {

        map.put(s.chara(0,1), substring(s.length()-1));
        }
    return map;
}
}
        

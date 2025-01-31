import java.io.*;
import java.util.ArrayList;


public class FileOps {

    public ArrayList<String> read(String path) {
        ArrayList<String> a = new ArrayList<>();

        try {
            BufferedReader buffRead = new BufferedReader(new FileReader(path));
            
            String str;
            while ((str = buffRead.readLine()) != null) {
                a.add(str);
            }
            
            buffRead.close();

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }

        return a;
    }
}

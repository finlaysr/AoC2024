import java.io.*;
import java.util.ArrayList;

/**
 * Some useful file operations
 */
public class FileOps {

    /**Read a file at the specified path
     * @param path path of file to read
     * @return An ArrayList of String with each new line as an element in the array
     */
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

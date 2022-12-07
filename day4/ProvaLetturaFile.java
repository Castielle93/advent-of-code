package day4;

import java.io.*;
import java.util.ArrayList;
class ProvaLetturaFile{

    public static void main(String[] args) {
        ArrayList<String> mArrayList = new ArrayList<String>();
        try {
            // Create a BufferedReader to read the file
            BufferedReader reader = new BufferedReader(new FileReader("day4\\input.txt"));
      
            // Read the file line by line
            String line = reader.readLine();
            
            while(line != null){
                mArrayList.add(line.strip());
                line = reader.readLine();
            
            }

            
            

      
            // Close the reader
            reader.close();
          } catch (IOException e) {
            e.printStackTrace();
          }
          mArrayList.forEach(n -> System.out.println(n));
        }
}
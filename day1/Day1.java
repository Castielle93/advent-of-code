package day1;

import java.io.*;
import java.util.*;

public class Day1 {
    // 1) Find the Elf carrying the most Calories. 
    //    How many total Calories is that Elf carrying?
    // --------------------------------------------------------
    // 2) Find the top three Elves carrying the most Calories.
    //    How many Calories are those Elves carrying in total?
    public static void main(String[] args) {
        ArrayList<Integer> mCalories = new ArrayList<Integer>();
        String currentLine = "";
        int somma = 0;
        try {
            File file = new File("C:\\Users\\marme\\Desktop\\advent of code\\day1\\input1.txt");
            BufferedReader mBufferedReader = new BufferedReader(new FileReader(file));

            currentLine = mBufferedReader.readLine();
            
            while (currentLine != null){   

                if(currentLine.equals("")){
                    mCalories.add(somma);
                    somma = 0;
                } else{
                    somma += Integer.valueOf(currentLine);
                }
                currentLine = mBufferedReader.readLine();

            }

            mBufferedReader.close();

            Collections.sort(mCalories, Collections.reverseOrder());

            int tot = 0;

            for(int i = 0; i < 3; i++){
                tot += mCalories.get(i);
            }

            //System.out.println(mCalories);

            System.out.println(Collections.max(mCalories)); 

            System.out.println(tot);

        } catch (Exception e) {
            System.out.println(e);
        }
        

    }
}

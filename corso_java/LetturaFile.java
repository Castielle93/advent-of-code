package corso_java;

import java.io.*;
import java.util.Scanner;

import javax.swing.filechooser.FileView;


public class LetturaFile {

    public static void main(String[] args) {

        String login = "", pwd = "";

        Scanner mScanner = new Scanner(System.in);

        try {
            System.out.print("Inserisci username da ricercare: " );
            login = mScanner.next();

            System.out.print("Inserisci password da ricercare: " );
            pwd   = mScanner.next();
        } catch (Exception e) {
            System.out.println(e);
        } finally{
            mScanner.close();
        }


        // Split (guardare anche charat, indexof, substring
        try {
            BufferedReader file_lettura = new BufferedReader(new FileReader("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\inputLogin.txt"));
            
            //Scriviamo le credenziali se le troviamo in un file di scrittura
            FileWriter fileWriter = new FileWriter("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\outputLogin.txt");
            


            String riga;

            boolean loginTrovato = false, 
                    pwdTrovata   = false,
                    trovatoTutto = false;

            int i = 1;
            riga = file_lettura.readLine();  //leggo prima riga

            // System.out.println(riga.strip()); //tolgo spazi in testa e in coda eventuali
            

            while(riga != null && (!trovatoTutto) ) {
                
                //System.out.println(riga);
                if(!loginTrovato && riga.strip().equals(login)){
                    loginTrovato = true;
                    System.out.println("trovato login: " + riga + " alla riga "+i);
                    fileWriter.write("Login detected!    --> " + i + ": "+ riga + "\n");

                }
                else if (!pwdTrovata && riga.strip().equals(pwd)) {
                    pwdTrovata = true;
                    System.out.println("trovata password: " + riga + " alla riga "+i);
                    fileWriter.write("Password detected! --> " + i + ": "+ riga + "\n"); 

                }

                if(loginTrovato && pwdTrovata){
                    trovatoTutto = true;
                }

                riga = file_lettura.readLine();
                i++;
            }

            if(trovatoTutto){
                System.out.println("Ho trovato tutto, ho letto fino alla riga " + i);
                
            } else if(loginTrovato){
                System.out.println("ho trovato solo il login");
            } else if(pwdTrovata){
                System.out.println("ho trovato solo la password");
            } else{
                System.out.println("non ho trovato niente");
            }
            
            file_lettura.close(); 
            fileWriter.close();
        } 
        catch(IOException e){
            System.out.println(e);
        }   
    }  
}

/********************************************************************
// Prima modalità
// lettura di file un carattere alla volta
        try {    
            FileInputStream file_lettura = new FileInputStream("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\input.txt");    

            int i = file_lettura.read();  
            System.out.print((char)i);    
  
            file_lettura.close();    
          } catch(Exception e){
              System.out.println(e);
          }    
    }  
*/

/********************************************************************
// Seconda modalità
        // lettura di file un carattere alla volta FINO a fine file
        try {    
            FileInputStream file_lettura = new FileInputStream("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\input.txt");    
            int i = 1; 
            while((i = file_lettura.read())!= -1){ 
                System.out.print((char)i);    
            }    
            
            file_lettura.close();    
            
          } catch(Exception e){
              System.out.println(e);
          }    
    }  
*/

/********************************************************************
// Terza modalità
        // Lettura di una riga del file
        try {    
            BufferedReader file_lettura = new BufferedReader(new FileReader("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\input.txt"));
            String riga;
            riga = file_lettura.readLine();
            
            while(riga != null) {                       //se riga==null -> file finito
                System.out.println(riga);
                riga = file_lettura.readLine();
            }
            
            file_lettura.close();

        } catch(Exception e){
              System.out.println(e);
        } 
    }       
        
*/

/********************************************************************
// Lettura file con sostituzione di caratteri a video
        try {
            BufferedReader file_lettura = new BufferedReader(new FileReader("C:\\Users\\marme\\Desktop\\advent of code\\corso_java\\input.txt"));
            
            String riga;
            
            riga = file_lettura.readLine();
            
            while(riga != null) {
                System.out.println(riga.replaceAll(";", " - "));
                riga = file_lettura.readLine();
            }  
            file_lettura.close(); 
        } 
        catch(IOException e){
            System.out.println(e);
        }        
*/
/********************************************************************
// Split (guardare anche charat, indexof, substring
        try {
            BufferedReader file_lettura = new BufferedReader(new FileReader("C:\\temp\\catalogoprodotti.txt"));
        
            String riga;
                       
            riga = file_lettura.readLine();  //leggo prima riga
            
            String var_riga_array []; //split  prima riga
            //splitta la riga letta - è brutto ripetere la stessa istruzione, 
            //in questo momento, per spiegare la split, la teniamo
            var_riga_array = riga.split(";");    
            
            while(riga != null) {
                
                System.out.println("riga:" + riga + "<");
                var_riga_array = riga.split(";");    //splitta la riga letta

                //System.out.println("quantità:" + var_riga_array[3] + "<");
                
                for (String var_temp_elemento: var_riga_array) {
            
                    System.out.println("il valore:" + var_temp_elemento + "<");
                }
                riga = file_lettura.readLine();
            }
            
            file_lettura.close(); 
        } 
        catch(IOException e){
            System.out.println(e);
        }   
    }  
*/
/********************************************************************



/********************************************************************
// OPZIONE DO WHILE
        // Lettura file con sostituzione dicaratteri a video
        try {
            BufferedReader file_lettura = new BufferedReader(new FileReader("C:\\temp\\catalogoprodotti.txt"));
            
            String riga;
            
            do {
                riga = file_lettura.readLine();
                if (riga != null) {
                    System.out.println(riga.replaceAll(";", " - "));
                }
                
            } while (riga != null);
            
            file_lettura.close(); 
        } 
        catch(IOException e){
            System.out.println(e);
        }    
    }  
*/
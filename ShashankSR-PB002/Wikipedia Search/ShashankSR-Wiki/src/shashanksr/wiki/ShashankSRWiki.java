/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package shashanksr.wiki;

import com.sun.jersey.api.client.Client;
import com.sun.jersey.api.client.ClientResponse;
import com.sun.jersey.api.client.WebResource;
import java.io.PrintWriter;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;

/**
 *
 * @author shashank
 */
public class ShashankSRWiki {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
                Scanner user_input = new Scanner( System.in );
                
                System.out.print("Use default file ? Y/N");
                String filename;
                if("N".equals(user_input.next()) ){
                    System.out.println("Enter file name"); 
                       filename = user_input.next();
                }else{
                 filename = "wiki.log";
                }
                  
                System.out.print("Enter search term ");
                String query = user_input.next( );
                
                while(!"Q".equals(query)){
                    PrintWriter out = new PrintWriter(filename);
                    Client client = Client.create();
                    WebResource webResource = client
                       .resource("https://en.wikipedia.org/w/api.php?"
                               + "format=json&action=opensearch&search="+query
                               + "&limit=1");
                    ClientResponse response = webResource.accept("json")
                       .get(ClientResponse.class);
                    if (response.getStatus() != 200) {
                       throw new RuntimeException("Failed : HTTP error code : "
                            + response.getStatus());
                    }
                    String output = response.getEntity(String.class);
                    
// ---------- HACK. Unable to get JSON response. Needs improvement ------------

                    Pattern p = Pattern.compile(".*,\\s*(.*)");
                    Matcher m = p.matcher(output);
                    if (m.find() )
                        System.out.println(m.group(1));
                    out.println(m.group(1));
//-----------------------------------------------------------------------------

                    System.out.print("Enter search term. Press 'Q' to quit. ");
                    query = user_input.next( );
                  
                }
	  } catch (Exception e) {
		e.printStackTrace();
                
	  }
	}
        // TODO code application logic here
    }
    


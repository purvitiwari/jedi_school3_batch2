// Usage java wikis <name_of_movie> 
// Example java wikis Terminator
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.URL;
import java.net.URLConnection;
import java.util.logging.FileHandler;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;


public class wikis {

public static void main(String args[])
{
    if(args.length==0)
    {
        System.out.println("Usage: java wikis <name_of_movie>"); 
        System.out.println("Example java wikis Terminator");
        System.exit(0);
    }
    BufferedReader rd;
    OutputStreamWriter wr;
    Logger logger = Logger.getLogger("MyLog");  
    FileHandler fh; 
    String search = String.join(" ", args);

try
{
	String urlString = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + search + "&limit=1&namespace=0&format=json";
    URL url = new URL(urlString);
    URLConnection conn = url.openConnection();
    conn.setDoOutput(true);
    wr = new OutputStreamWriter(conn.getOutputStream());
    wr.flush();
    rd = new BufferedReader(new InputStreamReader(conn.getInputStream()));
    StringBuilder jsonLine = new StringBuilder();
    String line; 
    while ((line = rd.readLine()) != null) {
       jsonLine = jsonLine.append(line);	
    }

    fh = new FileHandler("./MyLogFile.log");  
    logger.addHandler(fh);
    SimpleFormatter formatter = new SimpleFormatter();  
    fh.setFormatter(formatter);  
    String[] tokens = jsonLine.toString().split("],");
    System.out.println("Writing wiki link to the file ... ");
    logger.info(tokens[2]);
    
}

catch (Exception e) {
        System.out.println(e.toString());
        System.out.println("Please try again !!!!");
        logger.info(e.toString());
    }
  }
 }

import java.io.*;
import java.net.*;
import org.json.*;

public class Wiki{
	
	public String wikiSearch(String searchTerm){
		String result;
		try{
			URL url = 
			new 
			URL("https://en.wikipedia.org/w/api.php?action=opensearch&search="
				+ searchTerm + "&limit=1&format=json");
         	URLConnection urlConnection = url.openConnection();
         	HttpURLConnection connection = null;
         	if(urlConnection instanceof HttpURLConnection){
            	connection = (HttpURLConnection) urlConnection;
         	}
         	else
         	{
            	System.out.println("Please enter an HTTP URL.");
            	result = "error";
            	return result;
         	}
         	BufferedReader in = new BufferedReader(new InputStreamReader
         		(connection.getInputStream()));
         	String urlString = "";
         	String current;
         	current = in.readLine();
         	JSONArray arr = new JSONArray(current);
         	JSONArray arr1 = arr.getJSONArray(1);
         	JSONArray arr2 = arr.getJSONArray(3);
         	System.out.println("Title : " + arr1.getString(0));
         	System.out.println("URL : " + arr2.getString(0));
         	result = arr1.getString(0) + "    " + arr2.getString(0);
         	
		}
		catch(Exception e){
			result = "error";
			e.printStackTrace();
		}
		return result;
	}

	public void writeToFile(String fileName, String result){
		FileWriter fw = null;
		BufferedWriter bw = null;
		PrintWriter out = null;
		try{
			fw = new FileWriter(fileName, true);
			bw = new BufferedWriter(fw);
			out = new PrintWriter(bw);

			out.println(result);
			out.close();
			bw.close();
			fw.close();

		}
		catch(Exception e){
			e.printStackTrace();
		}
	}

	public static void main(String args[]){
		String searchTerm = new String();
		String fileName = new String();
		String result;
		if(args.length > 1){
			searchTerm = args[0];
			fileName = args[1];
			Wiki wiki = new Wiki();
			result = wiki.wikiSearch(searchTerm);
			if(result.equals("error")){
				System.out.println("There was some error!!");
				return;
			}
			wiki.writeToFile(fileName, result);
		}
		else{
			try{
				System.out.println("Enter item to search : ");
				BufferedReader br = new BufferedReader
				(new InputStreamReader(System.in));
				searchTerm = br.readLine();
				System.out.println("Enter log file name : ");
				fileName = br.readLine();
				if(br != null)
					br.close();
				Wiki wiki = new Wiki();
				result = wiki.wikiSearch(searchTerm);
				if(result.equals("error")){
					System.out.println("There was some error!!");
					return;
				}
				wiki.writeToFile(fileName, result);
			}
			catch(Exception e){
				e.printStackTrace();
			}
		}
	}

}
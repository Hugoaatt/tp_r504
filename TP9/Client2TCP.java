import java . io . * ;
import java . net . * ;

public class Client1TCP
{
  public static void main( String[] args )
  {

    try
    {
      // ClientTCP2.java
      Socket socket = new Socket("localhost", 2016);
      DataOutputStream dOut = new DataOutputStream (socket.getOutputStream());
      dOut.writeUTF(args [0] );
      socket.close();
    }
    catch ( Exception ex )
    {
      System.out.println ( "Erreur!" ) ;
    }
  }
}

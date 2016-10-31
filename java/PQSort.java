import java.util.Comparator;

/**
 * Created by dexter on 10/30/16.
 */
public class PQSort implements Comparator {

    public int compare(Object a, Object b) {
        if(a instanceof String && b instanceof String) {
            return ((String)a).compareToIgnoreCase((String) b);
        }
        if(a instanceof Integer && b instanceof Integer) {
            return (Integer)a>=(Integer)b?1:-1;
        }

        return -1;
    }
}



import com.sun.deploy.util.StringUtils;

/**
 * Created by dexter on 10/22/16.
 */
public class StringBufferVsStringBuilder {
    public boolean gmailEmail() {
        return true;
    }

    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer();
        sb.append("whre are you!!!");
        System.out.println(sb.length());
        sb.insert(2,"kumar");
        System.out.println(sb);

        //TODO:
        //String builder functions

        StringBuilder sbuilder = new StringBuilder();
        sbuilder.append("Kumar and his friends!!");

        System.out.println(sbuilder.substring(3,9));


    }


}

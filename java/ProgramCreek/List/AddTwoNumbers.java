package ProgramCreek.List;

import DataStructure.ListNode;

/**
 * Created by dexter on 11/9/16.
 */
public class AddTwoNumbers {
    ListNode result = new ListNode(0);

    public ListNode calculateSum(ListNode n1, ListNode n2) {

        ListNode temp1 = n1;
        ListNode temp2 = n2;
        int carry = 0;
        ListNode temp = result;
        while(n1!= null && n2 != null) {

            int num = n1.a + n2.a + carry ;

            temp.next = new ListNode(num%10);
            temp = temp.next;

            if(num > 9) {
                carry = 1;
            }
            else {
                carry =0;
            }
            n1 = n1.next;
            n2 = n2.next;
        }

        if(n1 != null) {
            temp.next = n1;
        }

        if(n2 != null) {
            temp.next = n2;
        }

        while(carry!=0) {
            temp = temp.next;
            int tempvar =  temp.a+carry;

            temp.a = tempvar %10;

            carry = tempvar > 9 ?1:0;
        }
        return result.next;

    }

}

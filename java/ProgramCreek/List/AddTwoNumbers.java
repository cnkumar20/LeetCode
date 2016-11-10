package ProgramCreek.List;

import DataStructure.ListNode;

/**
 * Created by dexter on 11/9/16.
 */
public class AddTwoNumbers {
    ListNode result = new ListNode(0);

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry =0;

        ListNode newHead = new ListNode(0);
        ListNode p1 = l1, p2 = l2, p3=newHead;

        while(p1 != null || p2 != null){
            if(p1 != null){
                carry += p1.a;
                p1 = p1.next;
            }

            if(p2 != null){
                carry += p2.a;
                p2 = p2.next;
            }

            p3.next = new ListNode(carry%10);
            p3 = p3.next;
            carry /= 10;
        }

        if(carry==1)
            p3.next=new ListNode(1);

        return newHead.next;
    }

}

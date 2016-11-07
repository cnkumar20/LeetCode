package GeeksForGeeks.LinkedList;

import GeeksForGeeks.DataStructure.ListNode;
import GeeksForGeeks.DataStructure.TreeNode;

import java.util.List;

/**
 * Created by dexter on 11/7/16.
 */
public class InsertSortedInLinkedList {
    ListNode head;

    InsertSortedInLinkedList(ListNode h) {
        this.head = h;
    }



    public ListNode insertInSortedListNode(ListNode node) {

        ListNode cur = head;
        ListNode temp = null;

        if(node.a < cur.a) {
            node.next = cur;
            head = node;
            return head;
        }

        while(cur!=null) {
            temp = cur;
            cur = cur.next;
            if(cur != null && node.a < cur.a) {
                temp.next = node;
                node.next = cur;
                return head;
            }
        }
        temp.next = node;
        return head;
    }

}
